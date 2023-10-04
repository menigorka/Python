from django.urls import path
from .views import ProductListView, ProductDetailView, LessonListView, LessonDetailView, UserLessonAccessView, ProductStatisticsView, UserProductLessonListView, UserProductLessonDetailView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('user-lessons/', UserLessonAccessView.as_view(), name='user-lesson-access-list'),
    path('product-statistics/', ProductStatisticsView.as_view(), name='product-statistics'),
    path('user-product-lessons/', UserProductLessonListView.as_view(), name='user-product-lesson-list'),
    path('user-product-lessons/<int:product_id>/', UserProductLessonDetailView.as_view(), name='user-product-lesson-detail'),
]
