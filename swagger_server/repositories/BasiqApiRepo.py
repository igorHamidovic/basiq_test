from swagger_server.settings import Settings
from requests.adapters import HTTPAdapter, Retry
from requests import Session
from http_exceptions import BadRequestException, UnauthorizedException, HTTPException
from swagger_server.DTOs.basiq_transaction import BasiqTransaction
from typing import List


class BasiqApiRepo:
    _settings: Settings
    _request_session: None
    _api_token: None

    def __init__(self):
        self._settings = Settings()
        self._request_session = Session()
        self._request_session.mount('https://', HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.2)))
        self.setup_repo()

    def setup_repo(self):
        headers = {
            "Authorization": f"Basic {self._settings.basiq_api_key}",
            "Content-Type": "application/x-www-form-urlencoded",
            "basiq-version": self._settings.basiq_api_version
        }
        url = f"{self._settings.basiq_api_base_url}/token"
        response = self._request_session.post(url, headers=headers)

        if response.status_code == 403:
            raise UnauthorizedException(message=response.json()['data'][0]['detail'])
        elif response.status_code == 200:
            self._api_token = response.json()['access_token']
        else:
            raise BadRequestException(message=response.json()['data'][0]['detail'])

    def get_transactions(self, next_id=None) -> (List[BasiqTransaction], str):
        headers = {
            "Authorization": f"Bearer {self._api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "basiq-version": self._settings.basiq_api_version
        }
        url = f"{self._settings.basiq_api_base_url}/users/{self._settings.basiq_user_id}/transactions"
        if next_id:
            url = f"{url}?next={next_id}"

        response = self._request_session.get(url, headers=headers)

        if response.status_code == 403:
            if self._is_token_expired(response):
                self.setup_repo()
            else:
                raise UnauthorizedException(message=response.json()['data'][0]['detail'])
            return self.get_transactions(next_id)
        elif response.status_code == 200:
            return self._select_transactions_from_response(response.json()['data']), \
                self._select_next_id(response.json()['links'])
        else:
            raise HTTPException(status_code=503, message=response.json()['data'][0]['detail'])

    @classmethod
    def _select_transactions_from_response(cls, response_data) -> List[BasiqTransaction]:
        return list(map(lambda x: BasiqTransaction.from_disc(x), response_data))

    @classmethod
    def _select_next_id(cls, response_links) -> str:
        next_url = response_links.get('next')
        if not next_url:
            return None

        next_id = str(next_url).split('?')[1]
        return next_id.split('=')[1]

    @classmethod
    def _is_token_expired(cls, response):
        response_data = response.json()
        return response_data['detail'] == 'Token has expired'
