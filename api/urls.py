from django.urls import path, include
from rest_framework import routers
from .views import user_views

router = routers.DefaultRouter()

router.register(
    r"users",
    user_views.UserViewSet,
    basename="user",
)

urlpatterns = [
    path(
        "users/login/",
        user_views.MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("", include(router.urls)),
]
