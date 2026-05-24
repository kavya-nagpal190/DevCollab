from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import SkillViewset,UserViewset,RegisterViewset
router = DefaultRouter()
router.register('users',UserViewset)
router.register('skills',SkillViewset)

urlpatterns = [
   path('',include(router.urls)),
   path('register/',RegisterViewset.as_view(),name='register'),
]
