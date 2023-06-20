from rest_framework import serializers
from .models import Document
from django.contrib.auth.models import User


class DocumentSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Document
        fields = ('id', 'title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    Documents = serializers.PrimaryKeyRelatedField(many=True, queryset=Document.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'Documents')
