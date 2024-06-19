from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
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