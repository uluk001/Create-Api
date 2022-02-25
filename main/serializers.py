from rest_framework import serializers
from main.views import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note 
        fields = ('title', 'content', 'created_at' ,'updated_at' )