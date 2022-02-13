from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from sensor_web_api import views

urlpatterns = [
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('sensor/', views.SensorList.as_view(), name='sensor-list'),
    path('sensor/<int:pk>/', views.SensorDetail.as_view(), name='sensor-detail'),
    path('data/', views.data),
]

urlpatterns = format_suffix_patterns(urlpatterns)