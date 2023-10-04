from rest_framework import serializers
from .models import Product, Lesson, LessonAccess

class LessonAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAccess
        fields = ('watched', 'watched_time_seconds', 'last_watched_date')

class LessonSerializer(serializers.ModelSerializer):
    accesses = LessonAccessSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('name', 'video_link', 'duration_seconds', 'accesses')

class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'owner', 'lessons')
