from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from .models import Tarefas

class TarefaList(ListView):
    model = Tarefas
    paginate_by = 10           
    ordering = ['-created_at']  

class TarefaDetail(DetailView):
    model = Tarefas

class TarefaCreate(CreateView):
    model = Tarefas
    fields = ['title', 'descricao']
    success_url = reverse_lazy('tarefas:list')

class TarefaUpdate(UpdateView):
    model = Tarefas
    fields = ['title', 'descricao']
    success_url = reverse_lazy('tarefas:list')

class TarefaDelete(DeleteView):
    model = Tarefas
    success_url = reverse_lazy('tarefas:list')
