from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefa/', include('tarefas.urls', namespace='tarefas')),
]