from django.urls import path, include
from rest_framework import permissions

from .views import ActorViewSet, MovieActorAPIView, MovieViewSet  # CommentAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi






from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, AddCommentAPI


router = DefaultRouter()
router.register('actors', ActorViewSet)


urlpatterns = [
    path('comments/', AddCommentAPI.as_view()),  # Base URL prefix
    path('api/', include(router.urls)),
    path('movie/', MovieViewSet.as_view({'get': 'list'})),

]