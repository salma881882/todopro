from django.urls import path
from . import views
from .views import TaskListView

urlpatterns = [
    path('',views.index,name='index'),
   # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('clsbsdhom/',views.TaskListView.as_view(),name='clsbsdhom'),
    path('dbv/<int:pk>/',views.TaskDetailView.as_view(),name='dbv'),
    path('cbvupdate/<int:pk>/',views.TaskUpdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDelete.as_view(),name='cbvdelete'),
]
