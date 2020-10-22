from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import (
    permissions,
    status,
    viewsets,
)
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.versioned.v1.account import serializers
from api.versioned.v1.account.serializers import (
    LoginSerializer,
)

USER_MODEL = get_user_model()


class AuthViewSet(viewsets.GenericViewSet, ):
    permission_classes = [permissions.AllowAny]
    queryset = USER_MODEL.objects.all()
    serializer_classes = {
        "register": serializers.RegisterSerializer,
    }
    default_serializer_class = serializers.RegisterSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @swagger_auto_schema(
        operation_description="register",
        responses={
            201: serializers.RegisterSerializer,
            400: f"{_('username exist')}",
        },
    )
    @action(
        detail=False,
        methods=["POST"],
        permission_classes=[AllowAny],
        serializer_class=serializers.RegisterSerializer,
        url_path="register",
        url_name="register",
    )
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Login",
        responses={
            200: "'token : {token}'",
            406: f"{_('Entered values is NOT valid')}",
        },
    )
    @action(
        detail=False,
        methods=["POST"],
        permission_classes=[AllowAny],
        serializer_class=LoginSerializer,
        url_path="login",
        url_name="login",
    )
    def login(self, request):
        """
        Login by username and  Password

        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get("password")
        username = serializer.validated_data.get("username")

        try:
            user = USER_MODEL.objects.get(username=username)
        except USER_MODEL.DoesNotExist:
            return Response(
                data={
                    "message": f"{_('Entered values is NOT valid')}"
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": _("user & pass is valid."),
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            )

        return Response(
            data={
                "message": f"{_('Entered values is NOT valid')}"
            },
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
