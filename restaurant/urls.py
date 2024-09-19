from django.urls import path
from .views import MenuItemsView, SingleMenuItemView


app_name = "restaurant"
urlpatterns = [
    # path("", index, name="index"),
    path("menu/", MenuItemsView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
]
