from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy


@login_required(login_url="/accounts/login/")
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    paginator = Paginator(Article.objects.all().order_by('-date'), 6)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    page_range = paginator.page_range[0:max_index]

    return render(request, 'articles/article_list.html', {'articles': articles, 'items': items, 'page_range': page_range})


@login_required(login_url="/accounts/login/")
def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


class ArticleEditView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Article
    form_class = forms.CreateArticle
    success_url = reverse_lazy('articles:list')

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)


@login_required(login_url="/accounts/login/")
def article_delete(request, slug):
    article = Article.objects.get(slug=slug)
    article.delete()
    return redirect('articles:list')
