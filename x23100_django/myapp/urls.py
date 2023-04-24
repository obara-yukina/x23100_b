from django.urls import path
from .import views

urlpatterns = [
    # users/の場合、views.py：showUsersメソッド呼び出し
    path('', views.showUsers, name = 'showUsers'),
]