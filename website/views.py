from django.shortcuts import render

# Create your views here.

def index(request):
    args = {}

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.save()
        args('msg': 'usuario cadastrado')

    return render(request, 'index.html', args)

def sobre(request):
    pessoa = Pessoa.objects.all()
    args = {
        'pessoas':pessoa
    }
    return render(request, 'sobre.html', args)
