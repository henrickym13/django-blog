from django.urls import path
from . import views


urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('notice/<int:id>/', views.show_notice, name='notice'),
    path('notice/<int:category_id>/category/', views.show_notice_for_category, name='notice_category'),
    path('notice/tags/<slug:tag_slug>/', views.tagged_notices, name='tagged_notices'),
    path('search/', views.search_notices, name='search_notices'),
]
