
from django.urls import path 

from . import views


urlpatterns = [

    path('',                          views.home_page ,            name="home_page"),
    path('profile_list/',             views.profile_list ,         name="profile_list"),
    path('profile/<int:pk>',          views.profile ,              name="profile"),
    path('profile/followers/<int:pk>',views.followers ,            name="followers"),
    path('profile/following/<int:pk>',views.following ,            name="following"),
    path('login/',                    views.login_user ,           name="login_user"),
    path('logout/',                   views.logout_user ,          name="logout_user"),
    path('register_user/',            views.register_user ,        name="register_user"),
    path('update_user/',              views.update_user ,          name="update_user"),
    path('update_password/',          views.update_password ,      name="update_password"),
    path('gweek_like/<int:pk>',       views.gweek_like ,           name="gweek_like"),
    path('show_gweek/<int:pk>',       views.show_gweek ,           name="show_gweek"),
    path('delete_gweek/<int:pk>',     views.delete_gweek ,         name="delete_gweek"),
    path('unfollow/<int:pk>',         views.unfollow ,             name="unfollow"),
    path('follow/<int:pk>',           views.follow ,               name="follow"),
    path('search/',                   views.search ,               name="search"),
    path('search_user/',              views.search_user ,          name="search_user"),


]

