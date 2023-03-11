from rest_framework import serializers
from notes.models import Note
class NoteSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    class Meta:
        model = Note
        fields = ['id','title','description','created']