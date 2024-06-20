from django.urls import path
from .views import get_all_students ,create_new_student, get_single_student, update_student, delete_student , get_all_path, get_single_path, create_new_Path, update_path, delete_path


urlpatterns = [
    path('students/', get_all_students),
    path('create_student/', create_new_student),
    # Details url
    path('single_student/<int:pk>', get_single_student),
    path('update_student/<int:pk>', update_student),
    path('delete_student/<int:pk>', delete_student),

    
# ______________ paths url ______________

    path('create_path/', create_new_Path),
    path('paths/', get_all_path),
    
    path('path/<int:pk>', get_single_path),
    path('update_path/<int:pk>', update_path),
    path('delete_path/<int:pk>', delete_path),
]