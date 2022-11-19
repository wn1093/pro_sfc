from django.urls import path, include
from recognition import views


urlpatterns = [
    path('', views.index, name='index'),
    path('facecam_feed/', views.facecam_feed, name='facecam_feed'),
    path('', include('student_management_app.urls')),
    path('',include('detectme.urls')),
    path('',include('recognition.urls')),
    ]