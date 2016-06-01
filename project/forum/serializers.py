from django.contrib.auth.models import User
from forum.models import *
from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Topic
        fields = ('id', 'created', 'title', 'owner',)

class ThreadSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Thread
        fields = ('id', 'created', 'title', 'topic', 'owner',)

class ReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reply
        fields = ('id', 'created', 'text', 'thread', 'owner',)

class UserSerializer(serializers.ModelSerializer):
    topics = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Topic.objects.all(), required=False)
    threads = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Thread.objects.all(), required=False)
    replies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reply.objects.all(), required=False)

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'topics', 'threads', 'replies',)
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
