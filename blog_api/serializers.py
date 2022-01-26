from rest_framework import serializers
from blog_api.models import Author, Entry


class EntrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entry
        fields = ['title', 'released' , 'description', 'director']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ['name', 'access_level', 'entries']
