from rest_framework import serializers
from .models import Student, Path



class StudentSerializer(serializers.ModelSerializer):
    born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField() # read_onyl
    path_id = serializers.IntegerField()
    
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "email", "phone_number","age", "address", "born_year","path","path_id")

    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    
class PathSerializer(serializers.ModelSerializer):
    
    #  students = StudentSerializer(many=True)
     class Meta:
        model = Path
        # fields = "all"
        fields = ["id", "path_name"]
        # fields = ["id", "path_name", "students"]