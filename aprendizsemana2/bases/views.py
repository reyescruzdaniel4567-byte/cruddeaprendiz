from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import Aprendiz_Form
from .models import aprendiz  # Importación del modelo en minúscula como lo definiste

def listar(request):
    """Vista principal para mostrar la tabla con todos los registros."""
    # Trae todos los aprendices desde la base de datos
    registros_aprendices = aprendiz.objects.all()
    
    # Pasa los registros a la plantilla index.html
    return render(request, 'bases/index.html', {'aprendices': registros_aprendices})


def crear_aprendiz(request):
    """Vista para agregar un nuevo aprendiz."""
    if request.method == 'POST':
        form = Aprendiz_Form(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, '¡Aprendiz creado con éxito!')  
            return redirect('crear_aprendiz')  
    else:
        form = Aprendiz_Form()  
        
    return render(request, 'bases/aprendiz.html', {'form': form})


def editar_aprendiz(request, documento):
    aprendiz_objeto = get_object_or_404(aprendiz, documento=documento)
    form = Aprendiz_Form(request.POST or None, instance=aprendiz_objeto)
    if 'documento' in form.fields:
        form.fields['documento'].disabled = True
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, '¡Aprendiz actualizado con éxito!')
        return redirect('bases')  
        
    return render(request, 'bases/aprendiz.html', {'form': form})

from . import models 

# ... Aquí quedan tus otras vistas (listar, crear_aprendiz, etc.) ...
# NOTA: Asegúrate de borrar cualquier línea "from .models import ..." que tengas suelta abajo.

def eliminar_aprendiz(request, documento):
    # Usamos models.aprendiz para que Django busque dinámicamente la clase
    aprendiz_objeto = get_object_or_404(models.aprendiz, documento=documento)
    aprendiz_objeto.delete()
    messages.success(request, '¡Aprendiz eliminado con éxito!')
    return redirect('bases')