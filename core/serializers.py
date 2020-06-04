from rest_framework import serializers
from django.contrib.auth import models as dj_models
from core import models as core_models


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()

    def validate_username(self, value):
        """ validation to make sure username is unique """

        count = dj_models.User.objects.filter(username=value).count()

        if count:
            raise serializers.ValidationError("username already exists")
        return value

    def validate_email(self, value):
        ''' Validation to make sure email is unique '''

        count = dj_models.User.objects.filter(email=value).count()

        if count:
            raise serializers.ValidationError("email already exists")

        return value

    def save(self):
        """ Overridden method for creating new user """

        validated_data = self.validated_data
        dj_models.User.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get('password'),
            first_name=validated_data.get("firstname"),
            last_name=validated_data.get("lastname")
        )


class SignInSerializer(serializers.Serializer):
    """ Viewset for signin user """
    username = serializers.CharField(max_length=20)
    password = serializers.CharField()


class PaginationSerializer(serializers.Serializer):
    """ viewset for get requests where page number is required"""
    page = serializers.IntegerField()
