from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('',              views.TarefaList.as_view(),   name='list'),
    path('nova/',         views.TarefaCreate.as_view(), name='create'),
    path('<int:pk>/',     views.TarefaDetail.as_view(), name='detail'),
    path('<int:pk>/edit/',views.TarefaUpdate.as_view(), name='update'),
    path('<int:pk>/del/', views.TarefaDelete.as_view(), name='delete'),
]
