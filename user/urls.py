from django.urls import path
from .views import create_user, login_user

app_name = "user"

urlpatterns = [
    path("", create_user, name="cadastrar_usuario"),
    path("login/", login_user, name="login_usuario")
]