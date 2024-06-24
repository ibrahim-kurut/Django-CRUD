from django.urls import path
from .views import (
    get_all_students ,
    create_new_student,
    get_single_student, 
    update_student, 
    delete_student ,
    get_all_path, 
    get_single_path, 
    create_new_Path, 
    update_path, 
    delete_path,


#? class based views
    PathList,
    PathDetail,
    CreatePath,
    UpdatePath,
    DeletePath,

    #* ______ GenericAPIView ______
    Get_Paths_GenericAPIView,
    Create_Path_GenericAPIView,
    Get_Path_GenericAPIView,
    Update_Path_GenericAPIView,
    Delete_Path_GenericAPIView,

    #* ______ Concrete View Classes ______
    AllPath,
    CreatePath,
    GetPath,
    UpdatePathCV,
    RemovePath






    )


urlpatterns = [
    # path('students/', get_all_students),
    # path('create_student/', create_new_student),
    # # Details url
    # path('single_student/<int:pk>', get_single_student),
    # path('update_student/<int:pk>', update_student),
    # path('delete_student/<int:pk>', delete_student),

    
# ______________ paths url ______________

    # path('create_path/', create_new_Path),
    # path('paths/', get_all_path),
    
    # path('path/<int:pk>', get_single_path),
    # path('update_path/<int:pk>', update_path),
    # path('delete_path/<int:pk>', delete_path),

# ______________ class based views url ______________

    # path('paths/', PathList.as_view()),
    # path('new_path/', CreatePath.as_view()),
    # path('path/<int:pk>/', PathDetail.as_view()),
    # path('update_path/<int:pk>/', UpdatePath.as_view()),
    # path('delete_path/<int:pk>/', DeletePath.as_view()),




    # path('all_path/', Get_Paths_GenericAPIView.as_view()),
    # path('create_path/', Create_Path_GenericAPIView.as_view()),
    # path('get_path/<int:pk>/', Get_Path_GenericAPIView.as_view()),
    # path('update_path/<int:pk>/', Update_Path_GenericAPIView.as_view()),
    # path('delete_path/<int:pk>/', Delete_Path_GenericAPIView.as_view()),


#?_______________ Concrete View Classes Url _______________


    path('all_path/', AllPath.as_view()),
    path('new_path/', CreatePath.as_view()),
    path('get_path/<int:pk>/', GetPath.as_view()),
    path('update_path/<int:pk>/', UpdatePathCV.as_view()),
    path('delete_path/<int:pk>/', RemovePath.as_view()),



]