from django.urls import path
from .views import UserView,StoresView, password_update


urlpatterns = [
    path('users/me',UserView.as_view()),
    path('users/stores/',StoresView.as_view()),
    path('users/me/changePassword', password_update)
]