from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('addTask/', views.addTask, name='addTask'),
    # Mark as done feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as undone feature
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit Feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete Task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),  # Uncomment when delete functionality is implemented
]