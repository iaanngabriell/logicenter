
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from django.contrib.auth import logout as django_logout

def listaGeral(request):
    return render(request, 'produtos/base.html')

def estoque(request):
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
    # 1) Trazer todos os produtos para preencher o SELECT
    produtos = Produtos.objects.all()

    if request.method == 'POST':
        # 2) Ler dados do formulário
        produto_id       = request.POST.get('produto')
        qt_saida         = int(request.POST.get('quantidade_saida', 0))

        # 3) Buscar o objeto no banco, ou 404 se não existir
        produto = get_object_or_404(Produtos, id=produto_id)

        # 4) Atualizar a quantidade no estoque
        produto.quantidade = max(produto.quantidade - qt_saida, 0)
        produto.save()

        # 5) Redirecionar de volta para a lista de estoque
        return redirect('/estoque')

    # GET: apenas renderiza o formulário
    return render(request, 'produtos/saida.html', {
        'produtos': produtos
    })