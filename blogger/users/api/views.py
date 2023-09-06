from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.decorators import input, output
from users import services, selectors
from users.api.schemas import UserIn, UserOut


@api_view(['POST'])
@input(UserIn)
def user_create(request):
    data = request.data
    services.user_create(
        data['email'], data['username'], data['password'],
    )
    return Response(status=200)


@api_view(['GET'])
@output(UserOut)
def user_get(request, user_id: int):
    user = selectors.user_get(id=user_id)
    return user
