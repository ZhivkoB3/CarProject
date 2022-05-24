from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from .serializers import CustomUser, RegisterSerializer, CustomUserSerializer

from rest_framework.authtoken.models import Token


# Create your views here.


class BaseQueryClass(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UsersList(generics.ListAPIView, BaseQueryClass):
    pass


class UsersDetail(BaseQueryClass):
    pass


class UsersSoftDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Deactivates the user`s account
        """
        current = self.get_object()
        current.is_active = False
        current.save()
        return Response(
            {"message": "Account deleted successfully!"}, status=status.HTTP_200_OK
        )


class UsersRestore(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    pass

    def patch(self, request, *args, **kwargs):
        """
        Activates the user accounts after it has been deactivated
        """
        current = self.get_object()
        current.is_active = True
        current.save()
        return Response(
            {"message": "Account restored successfully!"}, status=status.HTTP_200_OK
        )



@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data["response"] = "Account created!"
        data["email"] = account.email
        data["username"] = account.username
        token = Token.objects.get(user=account).key
        data["token"] = token
    else:
        data = serializer.errors
    return Response(data)
