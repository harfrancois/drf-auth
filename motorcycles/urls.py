from django.urls import path
from .views import MotorcycleList, MotorcycleDetail

urlpatterns = [
    path('', MotorcycleList.as_view(), name='motorcycle_list'),
    path('<int:pk>/', MotorcycleDetail.as_view(), name='motorcycle_detail')
]