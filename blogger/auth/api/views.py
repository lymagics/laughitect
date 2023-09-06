from rest_framework.decorators import api_view
from rest_framework.response import Response

from auth import services
from auth.api.schemas import CredentialsIn
from auth.errors import InvalidCredentials
from core.decorators import input


@api_view(['POST'])
@input(CredentialsIn)
def login(request):
    data = request.data
    try:
        jwt_token = services.login(
            request, data['username'], data['password'],
        )
    except InvalidCredentials as e:
        detail = {'detail': str(e)}
        return Response(detail, status=403)

    response = Response(status=200)
    response.set_cookie('access', jwt_token)
    return response
