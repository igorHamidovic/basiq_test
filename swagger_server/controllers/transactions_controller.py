from swagger_server.services.transactions import Transactions
from http_exceptions import BadRequestException, UnauthorizedException, HTTPException


def transaction_analyses_get():  # noqa: E501
    try:
        transaction_services = Transactions()
        return transaction_services.calculate_average_spending()
    except UnauthorizedException as ex:
        pass
    except BadRequestException as ex:
        pass
    except HTTPException as ex:
        pass
    except Exception as ex:
        pass
