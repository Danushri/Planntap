from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from Mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), #as_view method returns a function because urls don't map to classes
    path('login/', LoginView.as_view(template_name = 'Mainapp2/login.html') , name = 'login'),
    path('logout/', LogoutView.as_view() , name = 'logout'),
    path('register/',views.register, name='register'),
    path('addDiary/',AddDiaryView.as_view(), name='add diary'),
    path('maps/', views.maps, name='maps'),
    path('RandomButton/', views.RandomButton, name='RandomButton'),
    path('getDiary/', views.get_diaryEntry, name='getDiary'),
    path('deleteDiary/', views.deleteDiary, name='DeleteDiary'),
    path('updateDiary/', views.updateDiary, name='UpdateDiary'),
    path('twitter/', views.twitter, name='twitter'),
    path('EntrySuccess/', views.EntrySuccess, name='EntrySuccess'),
    path('facebook/', views.facebookEvent, name='facebook'),
    path('Random/', views.Random, name='Random'),


    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
    name='password_reset'),

    path('password-reset/done',
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete '),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
