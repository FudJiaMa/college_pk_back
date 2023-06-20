from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateDocumentAPIView.as_view(), name='get_post_Documents'),
    path('<int:pk>/', views.RetrieveUpdateDestroyDocumentAPIView.as_view(), name='get_delete_update_Document'),
]