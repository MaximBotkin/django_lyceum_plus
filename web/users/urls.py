from django.urls import path
from .views import UserListView, UserDetailView


app_name = 'users'


urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
]
