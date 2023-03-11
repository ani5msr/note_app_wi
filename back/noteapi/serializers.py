from rest_framework import serializers
from notes.models import Note
class NoteSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    #fields are the json objects which we allow to be serialized
    class Meta:
        model = Note
        fields = ['id','title','description','created']