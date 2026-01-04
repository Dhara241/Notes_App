from django.urls import path
from . import views

app_name = 'notes'   # ⭐ IMPORTANT (namespace)

urlpatterns = [
    path('', views.NotesListView.as_view(), name='list'),
    path('<int:pk>/', views.NotesDetailView.as_view(), name='detail'),
    path('new/', views.NotesCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', views.NotesUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.NotesDeleteView.as_view(), name='delete'),
    
]
