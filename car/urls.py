from django.urls import path

from . import views

urlpatterns = [
    path('add_posts/', views.AddCarPost.as_view(), name='add_posts'),
   
    path('edit/<int:id>/', views.EditPostView.as_view(), name='edit_posts'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete_post'),
    path('detail/<int:id>/', views.detailView.as_view(), name='post_detail'),

]