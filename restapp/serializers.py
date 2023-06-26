from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import random

phone_number=os.getenv("PHONE_NUMBER")
account_sid=os.getenv("TWILIO_ACCOUNT_SSID")
auth_token=os.getenv("TWILIO_AUTH_TOKEN")
client=Client(account_sid,auth_token)



# class UserRegister(serializers.ModelSerializer):
#     confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ["username", "email", "password", "confirm"]
#
    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     confirm = attrs.get('confirm')
    #
    #     if password != confirm:
    #         raise serializers.ValidationError({'password': 'Passwords do not match.'})
    #
    #     return attrs
    #
    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     confirm = validated_data.pop('confirm')
    #
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #
    #     return user
#
# class locationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Location
#         fields='__all__'
#
# class itemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ItemName
#         fields='__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta():
        model = RegisterModel
        fields='__all__'

    def validate(self, attrs):
        password = attrs.get('password')
        confirm = attrs.get('confirm')

        if password != confirm:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        return attrs



# class otpserializer(serializers.Serializer):
#     otp=serializers.CharField(max_length=30)

class checkSerializer(serializers.Serializer):
    user=serializers.CharField(max_length=60)
    otp=serializers.IntegerField()


class otpserializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = '__all__'


class login(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=60)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if not RegisterModel.objects.get(email=email):
            raise serializers.ValidationError("incorrrect email")

        if not RegisterModel.objects.get(password=password):
            raise serializers.ValidationError("password doesn't match")

        return attrs
