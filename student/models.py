from django.db import models

# Create your models here.
class Path(models.Model):
    path_name = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.path_name}"
    
class Student(models.Model):
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"