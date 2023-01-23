from .models import *
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(
        source="owner.username", read_only=True)
    
    class Meta:
        model= Post  
        fields=('title','body','owner','created')
        read_only_fields = ('created',)
        
        
    def create(self, validated_data):
        
        
        post=Post.objects.create(
            title=validated_data['title'],
            body=validated_data['body'],
            owner=self.context['request'].user
        )   
        if post:      
            post.save()
            return post
        
        
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(
    source="owner.username", read_only=True)
    post = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='post_detail',)
    
    class Meta:
        model= Comment  
        fields=('post','body','owner','created','updated')
        read_only_fields = ('created','updated','post','owner')
    
    
    def create(self, validated_data):
        comment=Comment.objects.create(
            body=validated_data['body'],
            post_id=self.context['view'].kwargs.get('post_id'),
            owner=self.context['request'].user
        )
        comment.save()
        return comment




class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(
    source="owner.username", read_only=True)
    comment_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment_detail'
        
    )
    class Meta:
        
        model= Post  
        fields=('title','body','owner','comment_set','created','updated')
        read_only_fields = ('created','updated','owner','comment_set')
        
        
        
