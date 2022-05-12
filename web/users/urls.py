from django.urls import path
from .views import UserListView, UserDetailView, ProfileView


app_name = 'users'


urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/', ProfileView.as_view(), name='profile')
]
