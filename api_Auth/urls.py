from django.urls import path, include
from . import api
from rest_framework.authtoken import views


urlpatterns = [
    path('', api.index, name="index"),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', api.RegisterUser.as_view()),
]