from django.contrib.auth.models import User
from rest_framework import serializers

from myapp.models import Tag, Snippet


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=["id","title"]
        read_only_field=["id"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SnippetListSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    created_user = UserSerializer()
    class Meta:
        model = Snippet
        fields = ["id","snippet", "timestamp", "created_user", "tag"]

class SnippetCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        exclude = ["timestamp"]


    def create(self, validated_data):
        title = validated_data.get("snippet")
        if Tag.objects.filter(title=title).exists():
            validated_data["tag"] = Tag.objects.get(title=title)
        else:
            validated_data["tag"] = Tag.objects.create(title=title)
        snippet = super(SnippetCreateUpdateSerializer, self).create(validated_data)
        return snippet
            # tag_instance = Tag.objects.create(title=title)
            # validated_data["tag"] = tag_instance
        # snippet = super(SnippetCreateUpdateSerializer, self).create(validated_data)
        # snippet=SnippetCreateUpdateSerializer.object.create(**validated_data)
        # return snippet