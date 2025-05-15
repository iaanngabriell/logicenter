from django.shortcuts import render

# Create your views here.

def listaGeral(request):
    return render(request, 'produtos/lista.html')
    