from django.urls import path
from . import views
urlpatterns = [
path('notes/', views.NoteListCreate.as_view()),
path('notes/<int:pk>', views.NoteRetrieveUpdateDestroy.as_view()),
path('signup/', views.signup),
path('login/', views.login),
]
