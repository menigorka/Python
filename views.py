from rest_framework import generics
from rest_framework.response import Response
from .models import Product, Lesson, LessonAccess
from .serializers import ProductSerializer, LessonSerializer, LessonAccessSerializer
from django.contrib.auth.models import User
from django.db.models import Sum

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class UserLessonAccessView(generics.ListAPIView):
    serializer_class = LessonAccessSerializer

    def get_queryset(self):
        user = self.request.user
        return LessonAccess.objects.filter(user=user)

class ProductStatisticsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        for product in products:
            product.lesson_count = product.lessons.count()
            product.watched_lesson_count = LessonAccess.objects.filter(
                user=self.request.user,
                lesson__in=product.lessons.all(),
                watched=True
            ).count()
            product.total_watch_time_seconds = LessonAccess.objects.filter(
                user=self.request.user,
                lesson__in=product.lessons.all(),
                watched=True
            ).aggregate(total_watch_time=Sum('watched_time_seconds'))['total_watch_time']
            product.student_count = User.objects.filter(
                lessonaccess__lesson__in=product.lessons.all()
            ).distinct().count()
            product.purchase_percentage = product.productaccess_set.count() / User.objects.count()
        return products

class UserProductLessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(products__productaccess__user=user)

class UserProductLessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(products__productaccess__user=user, products__id=product_id)
