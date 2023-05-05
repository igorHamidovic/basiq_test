import os


class Settings(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
        return cls.instance

    @property
    def basiq_api_base_url(self):
        return os.getenv('BASIQ_API')

    @property
    def basiq_api_key(self):
        return os.getenv('BASIQ_API_KEY')

    @property
    def basiq_api_version(self):
        return "2.1"

    @property
    def basiq_user_id(self):
        return os.getenv('BASIQ_USER_ID')
