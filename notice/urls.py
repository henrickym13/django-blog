from django.urls import path
from . import views


urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('notice/<int:id>/', views.show_notice, name='notice'),
    path('notice/<int:category_id>/category/', views.show_notice_for_category, name='notice_category'),
]
