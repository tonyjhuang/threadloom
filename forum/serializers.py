from django.contrib.auth.models import User
from forum.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    created = serializers.ReadOnlyField(source='date_joined')

    class Meta:
        model = User
        fields = ('id', 'created', 'username', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TopicSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'created', 'title', 'owner',)

class ThreadSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Thread
        fields = ('id', 'created', 'title', 'topic', 'owner',)

class ReplySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ('id', 'created', 'text', 'thread', 'owner',)
