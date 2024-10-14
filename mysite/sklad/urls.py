from django.urls import path
from .views import *


urlpatterns = [
    path('', ExelViewSet.as_view({'get':'list', 'post': 'create'}), name='exel_list'),
    path('<int:pk>', ExelViewSet.as_view({'get':'retrieve', 'put': 'update', 'delete': 'destroy'}), name='exel_detail')

]