
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from django.contrib.auth import logout as django_logout

def listaGeral(request):
    return render(request, 'produtos/base.html')

def estoque(request):
    produtos = Produtos.objects.filter(quantidade__gt=0)
    produtos = Produtos.objects.all()
    return render(request, 'produtos/estoque.html', {'produtos': produtos})

def produtos_add(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        Produtos.objects.create(descricao=descricao, categoria=categoria, quantidade=quantidade)
        return redirect('/estoque')
    return render(request, 'produtos/produtos_add.html')

def saida(request):
    produtos = Produtos.objects.all()

    if request.method == 'POST':
        produto_id       = request.POST.get('produto')
        qt_saida         = int(request.POST.get('quantidade_saida', 0))

        produto = get_object_or_404(Produtos, id=produto_id)
        produto.quantidade = max(produto.quantidade - qt_saida, 0)
        produto.save()

        return redirect('/estoque')

    return render(request, 'produtos/saida.html', {
        'produtos': produtos
    })