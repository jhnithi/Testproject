from django.urls import path
from . import views
from file_upload_app.views import upload_file, delete_file, delete_all_files

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('file_content/<int:file_id>/', views.view_file_content, name='file_content'),
    path('view_uploaded_files/', upload_file, name='view_uploaded_files'),
     path('delete_file/<int:file_id>/', delete_file, name='delete_file'),
    path('delete_all_files/', delete_all_files, name='delete_all_files'),
]
