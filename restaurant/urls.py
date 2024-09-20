from django.urls import path, include
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


app_name = "restaurant"
router: DefaultRouter = DefaultRouter()
router.register(r"tables", BookingViewSet)

urlpatterns = [
    path("menu/", MenuItemsView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
    path("booking/", include(router.urls)),
    path("api-token-auth/", obtain_auth_token),
]
