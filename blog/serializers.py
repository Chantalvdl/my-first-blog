from rest_framework import serializers
from .models import Post, Todo

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('item', 'comments', 'deadline',)
