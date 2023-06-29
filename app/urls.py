from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"posts", views.PostViewSet)
router.register(r"likes", views.LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
