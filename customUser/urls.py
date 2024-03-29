from django.urls import path
from .views import SignUpView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/', views.edit_profile, name = 'edit_profile'),
    path('showDonor/', views.show_nearby_donors, name = 'showNearbyDonors'),
    path('showRecievers/', views.show_nearby_recievers, name = 'showNearbyRecievers'),
    path('messages/', views.seeNotifications, name = 'notification'),
    path('password_reset/',
     auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"),
      name = 'password_reset'),
    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"),
         name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"), 
        name = 'password_reset_confirm'),
    path('reset/done/',
     auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), 
     name = 'password_reset_complete'),
    path('showmap/', views.createMap, name = "maps"),
    path('delete/<pk>/', views.deleteNotification, name = "deleteNotification"),
    path('read/<pk>/', views.readMessage, name = 'readMessage'),
    path('getResource/<emailid>/', views.updateResources, name = 'update_requirements'),
    path('donation/<email>/', views.donation_done, name = 'donation_done'),
    path('contactUs/', views.ContactUs, name = 'contact'),
]