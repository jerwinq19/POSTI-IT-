from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home, name="home"),
    path('profile/', views.ProfileView, name="profile_view"),
    path('add/', views.AddPost, name="add_post"),
    path('delete/<int:id>/', views.DeletePost, name="delete_post"),
    path('update/<int:id>/', views.UpdatePost, name="update_post"),
    path('register/', views.RegisterUser, name="register"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.Logout, name="logout")

]
