from django.urls import path
from App_Blog import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
    path('upload/',views.UploadVideo.as_view(), name='upload_video'),
    path('uploadlist/',views.UploadList.as_view(),name='upload_list'),
]
