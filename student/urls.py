from django.urls import path
from .views import get_all_students ,create_new_student, get_single_student, update_student, delete_student


urlpatterns = [
    path('students/', get_all_students),
    path('create_student/', create_new_student),
    # Details url
    path('single_student/<int:pk>', get_single_student),
    path('update_student/<int:pk>', update_student),
    path('delete_student/<int:pk>', delete_student),
]