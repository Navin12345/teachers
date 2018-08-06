from classcast.teachers.models import teacher_info
from rest_framework import serializers

class teacherserializer(serializers.ModelSerializer):

    class Meta:
        model = teacher_info
        