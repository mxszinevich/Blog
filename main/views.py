from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import ArticleForm
from .models import  Article
from bs4 import BeautifulSoup as BS

def home(request):
    return render(request,'base.html',{})

def create_article_view(request,slug, pk):
    user=request.user

    if f'{user.slug}-{user.pk}' == f'{slug}-{pk}':  # Если обновляет данные действительный пользователь
        articles=Article.objects.filter(user=user).order_by('-date_time')

        if request.method=='POST' or request.method=='FILES':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                data=form.cleaned_data
                User=get_user_model()
                name=data.get('name')
                description=data.get('description')
                body=data.get('body')
                image=data.get('image')
                article=Article(name=name,body=body,user=user,description=description,image=image)
                article.save()
                return redirect('articles')
        else:
            form = ArticleForm()
    else:
        return redirect('create_article',slug=user.slug,pk=user.pk)
    return render(request,'main/create_article.html',{'form':form,'articles':articles})

def articles_view(request):
    article_list=Article.objects.all().order_by('-date_time')
    paginator = Paginator(article_list, 5)
    page_number = request.GET.get('page')
    article=paginator.get_page(page_number)
    article_first=article_list.first()
    return render(request,'main/articles.html',{'object_list':article,'article_first':article_first})

def article_view(request,slug):
    article=Article.objects.get(slug=slug)

    print(article.name)
    print(article.slug)
    return render(request,'main/article.html',context={'article':article })

def user_articles_view(request,slug):
    #Исправить user.slug на user
    articles=Article.objects.filter(user__slug=slug).order_by('-date_time')
    return render(request,'main/user_articles_list.html',context={'articles':articles})

def update_article_view(request,slug):
    request_list_post= ['POST','FILES']

    if request.method in request_list_post:

        form=ArticleForm(request.POST,request.FILES)
        article = Article.objects.get(slug=slug)

        if form.is_valid():
            user=request.user
            if user==article.user:
                data=form.cleaned_data
                #Изменение полей объекта
                if data.get('name'):
                    article.name=data.get('name')
                if data.get('description'):
                    article.description=data.get('description')
                if data.get('body'):
                    article.body=data.get('body')
                if data.get('image'):
                    article.image=data.get('image')
                print(data.get('publication_status'),'status')
                article.publication_status=data.get('publication_status')
                article.save()
                messages.success(request, 'Данные обновлены')

        return redirect('update_article',slug=article.slug)

    else:
        article = Article.objects.get(slug=slug)
        initial_values={
            'name': article.name,
            'description': article.description,
            'body': article.body,
            'image': article.image,
            'publication_status':article.publication_status
        }
        request.FILES['image']=article.image
        form = ArticleForm(initial=initial_values)
    return render(request,'main/update_article.html',context={'form':form})



def delete_article_view(request,slug):
    print(request.method)
    user = request.user

    article = Article.objects.get(slug=slug)
    assert article, 'Статья не найдена'
    if user == article.user and article:
        if request.method=='POST':
            messages.success(request, f'Статья {BS(article.name[:30],"html.parser").text} удалена')
            article.delete()#удаление статьи
            return redirect('user_articles',user.slug)
        return render(request,'main/delete_article.html',context={'article':article})
    else:
        return redirect('home')

















