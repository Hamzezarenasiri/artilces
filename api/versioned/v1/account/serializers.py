from django.contrib.auth import get_user_model
from rest_framework import serializers

USER_MODEL = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ('username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'first_name': {
                'required': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = USER_MODEL(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, max_length=32, min_length=1)
    password = serializers.CharField(write_only=True, max_length=32, min_length=1)
