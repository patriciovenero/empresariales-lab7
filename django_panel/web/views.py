from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404



# importamos la clase View
from django.shortcuts import redirect
from django.views import View
from .models import *
from .forms import *


# Create your views here.

class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')
        

def eliminar_alumno(request, pk):
    alumno = get_object_or_404(TblAlumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('/')
    return render(request, 'index.html', {'alumno': alumno})

class ProfesorView(View):
    
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'profesor.html',context)

    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('/profesor')

def eliminar_profesor(request, pk):
    profesor = get_object_or_404(TblProfesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('/')
    return render(request, 'profesor.html', {'profesor': profesor})