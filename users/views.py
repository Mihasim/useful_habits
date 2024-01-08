from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Сериалезатор для взаимодействия с пользователями
    """
    def list(self, request):
        # Метод для вывода списка пользователей с определением выборки из базы и указанием сериализатора
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Метод для вывода информации по пользователю с определением выборки из базы и указанием сериализатора
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UsersRegisterView(generics.CreateAPIView):
    """
    Сериализатор для регистрации нового пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)
