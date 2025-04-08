from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .forms import ConsultaForms

def listar_medicos(request):
    listar = Medico.objects.all()
    return render (request, 'listar_medicos.html', {'listar': listar})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = ConsultaForms()
    return render(request, 'from_consulta.html', {'form': form})

def detalhes_consulta (request, pk):
    consulta = get_object_or_404(Consulta, pk = pk)
    consulta = Consulta.objects.all().order_by(pk)

def filtro_especialidade(request):
    especialidade = request.GET.get('especialidade', '')

    if especialidade:
        especialidade = Medico.objects.filter(especialidade__icontains = especialidade)
    else:
        especialidade = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'listar': especialidade})