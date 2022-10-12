from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(), name = 'home'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('accounts/profile/<int:pk>/', views.UserProfile.as_view(), name="user_profile"),
    path('accounts/profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
    path('auto/new/', views.AutoPost.as_view(), name = 'newAutoPost'),
    path('auto/<int:pk>/update/', views.UpdateAutoPost.as_view(), name = 'auto_post_update'),
    path('auto/',views.AutoList.as_view(), name = 'auto_posts'),
    path('auto/<int:pk>/detail/',views.AutoPostDetail.as_view(), name = 'auto_post_detail'),
    path('auto/<int:pk>/delete/', views.AutoPostDelete.as_view(), name="auto_post_delete"),
]