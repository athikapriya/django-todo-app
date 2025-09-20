from django.urls import path
from . views import TaskList, TaskDetail, TaskCreate, UpdateTask, DeleteTask, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'), # for user login
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'), # for user logout
    path('register/', RegisterPage.as_view(), name = 'register'), # for user registration

    path('', TaskList.as_view(), name = 'tasks'),   # home page showing list of tasks
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'), # detail view for a specific task identified by its primary key (pk)
    path('create-task/', TaskCreate.as_view(), name = 'create-task'), # page to create a new task
    path('edit-task/<int:pk>/', UpdateTask.as_view(), name = 'edit-task'), # page to edit an existing task identified by its primary key (pk)
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name = 'delete-task'), # page to delete a task identified by its primary key (pk)
    
]
