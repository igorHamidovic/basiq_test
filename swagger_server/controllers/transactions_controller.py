import logging
from swagger_server.services.transactions import Transactions
from http_exceptions import BadRequestException, UnauthorizedException, HTTPException
from swagger_server.models.error_response import ErrorResponse

logger = logging.getLogger('connexion.app')


def transaction_analyses_get(category=None):  # noqa: E501
    try:
        if category:
            category = str(category).split(',')
        transaction_services = Transactions()
        return transaction_services.calculate_average_spending(category)
    except UnauthorizedException as ex:
        return ErrorResponse(details=ex.message), 403
    except BadRequestException as ex:
        return ErrorResponse(details=ex.message), 400
    except HTTPException as ex:
        return ErrorResponse(details=ex.message), 503
    except Exception as ex:
        logger.exception(f"{ex}")
        return ErrorResponse(details=str(ex)), 500
