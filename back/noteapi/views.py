from rest_framework import generics,permissions
from .serializers import NoteSerializer
from notes.models import Note
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
class NoteListCreate(generics.ListCreateAPIView):
# ListAPIView requires two mandatory attributes, serializer_class and
# queryset.
# We specify Serializer which we have earlier implemented 
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user).order_by('-created')
    def perform_create(self, serializer):
#serializer holds a django model
        serializer.save(user=self.request.user)
class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
# user can only update, delete own posts
        return Note.objects.filter(user=user)
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request) # data is a dictionary
            user = User.objects.create_user(
            username=data['username'],
            password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token),'status': 'created'},status=201)
        except IntegrityError:
            return JsonResponse(
            {'error':'username taken. choose another username'},
            status=400)
#csrf is used for enalbing the front end to use the backend api 
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
        request,
        username=data['username'],
        password=data['password'])
    if user is None:
        return JsonResponse(
        {'error':'unable to login. check username and password'},
        status=400)
    else: # return user token
        try:
            token = Token.objects.get(user=user)
        except: # if token not in db, create a new one
            token = Token.objects.create(user=user)
        return JsonResponse({'token':str(token), 'status': 'login successful'}, status=201)
