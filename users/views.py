from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


# Create your views here.

class UserDetail(APIView):
    """
    View to create a User object.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
