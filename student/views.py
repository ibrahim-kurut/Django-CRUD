from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer


from rest_framework.generics import GenericAPIView, mixins
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.viewsets import ModelViewSet



from rest_framework.views import APIView
# Create your views here.


#? _____________ Create New Student _____________
@api_view(['POST'])
def create_new_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": "Student created successfully"
        }
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#? _____________ Get All Student _____________
@api_view(['GET'])
def get_all_students(request):
    # get data from DB by Complex
    students = Student.objects.all()
    # convert complex to py dict
    serializer = StudentSerializer(students, many=True)
    # convert py dict to json format
    return Response(serializer.data)


#? _____________ Get single Student _____________
@api_view(['GET'])
def get_single_student(request, pk):
    single_student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(single_student)
    return Response(serializer.data)


#? _____________ Update Student _____________
@api_view(['PUT'])
def update_student(request, pk):
    update_single_student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=update_single_student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": "Student updated successfully"
            }
        return Response(message, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#? _____________ Delete Student _____________
@api_view(['DELETE'])
def delete_student(request, pk):
    delete_single_student = get_object_or_404(Student, id=pk)
    delete_single_student.delete()
    message = {
        "message": "Student deleted successfully"
    }
    return Response(message)

#! ________________ Paths ________________

#? _____________ Create New Path _____________
@api_view(['POST'])
def create_new_Path(request):
    serializer = PathSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": "Path created successfully"
        }
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#? _____________ Get All Path _____________
@api_view(['GET'])
def get_all_path(request):
    paths = Path.objects.all()
    serializer = PathSerializer(paths, many=True)
    return Response(serializer.data)


#? _____________ Get single Path _____________
@api_view(['GET'])
def get_single_path(request, pk):
    path = get_object_or_404(Path, id=pk)
    serializer = PathSerializer(path)
    return Response(serializer.data)


#? _____________ Update Path _____________
@api_view(['PUT'])
def update_path(request, pk):
    update_path = get_object_or_404(Path, id=pk)
    serializer = PathSerializer(instance=update_path, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": "Path updated successfully"
            }
        return Response(message, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#? _____________ Delete Path _____________
@api_view(['DELETE'])
def delete_path(request, pk):
    delete_path = get_object_or_404(Path, id=pk)
    delete_path.delete()
    message = {
        "message": "Path deleted successfully"
    }
    return Response(message)


#! _____________________________ class based views _____________________________

#? create a new path
class CreatePath(APIView):
    def post(self, request):
        serializer = PathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": "Path created successfully"
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#? get all paths
class PathList(APIView):
    def get(self, request):
        paths = Path.objects.all()
        serializer = PathSerializer(paths, many=True)
        return Response(serializer.data)

#? get single path
class PathDetail(APIView):
    def get(self, request, pk):
        path = get_object_or_404(Path, id=pk)
        serializer = PathSerializer(path)
        return Response(serializer.data)

#? update single path
class UpdatePath(APIView):
    def put(self, request, pk):
        update_path = get_object_or_404(Path, id=pk)
        serializer = PathSerializer(instance=update_path, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": "Path updated successfully"
                }
            return Response(message, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#? delete path
class DeletePath(APIView):
    def delete(self, request, pk):
        delete_path = get_object_or_404(Path, id=pk)
        delete_path.delete()
        message = {
            "message": "Path deleted successfully"
        }
        return Response(message)

#* _______________ Generic APIView _______________


#? create a new path
class Create_Path_GenericAPIView(mixins.CreateModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#? get all path
class Get_Paths_GenericAPIView(mixins.ListModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#? get single path
class Get_Path_GenericAPIView(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

#? update path
class Update_Path_GenericAPIView(mixins.UpdateModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#? delete path
class Delete_Path_GenericAPIView(mixins.DestroyModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#* _______________ Concrete View Classes _______________

class AllPath(ListAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class CreatePath(CreateAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class GetPath(RetrieveAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class UpdatePathCV(UpdateAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class RemovePath(DestroyAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer


#* _______________ Model View Set _______________
class PathModelViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
