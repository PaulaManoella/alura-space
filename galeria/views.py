from django.shortcuts import render

#função responsável pela pagina principal da aplicação
def index(request):
    #renderizando o arquivo index.html
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')