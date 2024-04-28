from django.shortcuts import render
from blog.models import Post, Categoria


# Create your views here.
def categoria(request, categoria_id):
    categoriasa = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoriasa)
    return render(request, 'blog/categorias.html', {'categorias': categoriasa, 'posts': posts})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {"posts": posts})
