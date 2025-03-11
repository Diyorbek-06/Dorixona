from django.urls import path
from .views import  DoriList, DoriDetail, DoriCreate, DoriUpdate, DoriDelete
urlpatterns = [
    path('', DoriList.as_view(), name='dori-list'),
    path('dori/<int:pk>', DoriDetail.as_view(), name='dori-detail'),
    path('dori-create', DoriCreate.as_view(), name='dori-create'),
    path('dori-update/<int:pk>/', DoriUpdate.as_view(), name='dori-update'),
    path('dori-delete/<int:pk>/', DoriDelete.as_view(), name='dori-delete'),
    ]






    # path('dori-list', dori_list, name='dori-list'),
    # path('dori/<int:id>', dori_detail, name='dori-detail')
