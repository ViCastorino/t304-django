from django.shortcuts import render, redirect
from website.models import Pessoa, Ideias

# Create your views here.

def index(request):
    args = {}

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        args = {'msg': 'Yep, agora é só colocar o email bro'}
        return  render(request, 'login.html', args)

    return render(request, 'index.html', args)

def sobre(request):
    ideias = Ideias.objects.all()
    args = {
        'pessoas':ideias
    }
    return render(request, 'sobre.html', args)

def login(request):
    #conferir se cadastrado, retornar para sobre, senaao retornar para cadastro
    if req.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_form).first()

        print('Eae mano(a)', pessoa)

        if pessoa is None:
            #retornar para a page de cadastro
            args = {'msg': 'Cadastre-se para criar uma ideia'}
            return render(request, 'index.html', args)
        else:
            #retornar para a page de ideias
            args = {'pessoa': pessoa}
            return render(request, 'ideias.html', args)
    
    return render(request, 'login.html', {})        

def cadastrar_ideia(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pessoa).first()
        
        if pessoa is not None:
            ideia = Ideias()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria = request.POST.get('categoria')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('yeaah')

            return redirect('/sobre')

    return render(request, 'ideias.html', {})









      