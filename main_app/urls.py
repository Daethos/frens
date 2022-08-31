from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profiles/', views.profiles_index, name='index.profile'),
    path('profiles/<int:profile_id>/', views.profiles_detail, name='detail.profile'),
    path('frens/', views.frens_index, name='index.fren'),
    path('frens/<int:fren_id>/', views.frens_detail, name='detail.fren'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profiles/<int:pk>/update', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete', views.ProfileDelete.as_view(), name='profiles_delete'),
    path('profiles/<int:profile_id>/add_theme/', views.add_theme, name='add_theme'),
    path('frens/create/', views.FrenCreate.as_view(), name='frens_create'),
    path('frens/<int:pk>/update', views.FrenUpdate.as_view(), name='frens_update'),
    path('frens/<int:pk>/delete', views.FrenDelete.as_view(), name='frens_delete'),
    path('profiles/<int:profile_id>/request_fren/<int:fren_id>', views.request_fren, name='request_fren')
]