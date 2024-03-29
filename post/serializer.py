from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body') #fields = '__all__'
        #read_only_fields = ('title',)
        #write_only_fields = ('body',)
        