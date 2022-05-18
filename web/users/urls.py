from django.urls import path
from .views import UserListView, UserDetailView, ProfileView


app_name = 'users'


urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<username>/', UserDetailView.as_view(), name='user_detail'),
]
