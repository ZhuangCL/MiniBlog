from django.shortcuts import render

# Create your views here.

# front page
from .models import Article,Blogger, ArticleInstance, Genre
def index(request):
    num_articles = Article.objects.all().count()
    num_comments = ArticleInstance.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    num_genre = Genre.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_articles' : num_articles,
        'num_comments' : num_comments,
        'num_bloggers' : num_bloggers,
        'num_genre' : num_genre,
        'num_visits' : num_visits
    }

    return render(request, 'index.html', context=context)

# List
from django.views import generic
class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 10

class ArticleDetailView(generic.DetailView):
    model = Article
    paginate_by = 10

    def article_detail_view(request, primary_key):
        try:
            article = Article.objects.get(pk = primary_key)
        except:
            raise Http404('Article does not exist')

        return render(request, 'blog/article_detail.html', context={'article':article})

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10
class BloggerDetailView(generic.DetailView):
    model = Blogger

    def blogger_detail_view(request, primary_key):
        try:
            blogger = Blogger.objects.get(pk = primary_key)
        except:
            raise Http404('Blogger does not exist')
        return render(request, 'blog/blogger_detail.html', context={'blogger':blogger})

# user list
from django.contrib.auth.mixins import LoginRequiredMixin
class MyArticleUserListView(LoginRequiredMixin,generic.ListView):
    model = Article
    template_name = 'blog/article_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(blogger__user = self.request.user)
class MyArticleAllUserListView(LoginRequiredMixin,generic.ListView):
    model = Article
    template_name = 'blog/article_list_all_user.html'
    paginate_by = 10

# usercreate
from django.shortcuts import render,redirect
from .forms import RegisterForm
def sign_up(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    context = {
        'form':form
    }
    return render(request, 'blog/register.html', context)

# article creat.update.delete
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Blogger,ArticleInstance
from django.contrib.auth.mixins import PermissionRequiredMixin

class ArticleUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'blog.can_edit_all_SET'
    model = Article
    fields = '__all__'

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('index')

# comment delete
class ArticleInstanceDelete(DeleteView):
    model = ArticleInstance
    def get_success_url(self):
        return reverse("article-detail", kwargs={'pk': self.object.id})

# create comment and article
from django.shortcuts import get_object_or_404
class ArticleInstanceCreate(CreateView):
    model = ArticleInstance
    fields = ['comment']

    def get_context_data(self, **kwargs):
        context = super(ArticleInstanceCreate, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk = self.kwargs['pk'])
        return context
    def form_valid(self, form):
        form.instance.commenter = self.request.user
        form.instance.article=get_object_or_404(Article, pk = self.kwargs['pk'])
        return super(ArticleInstanceCreate, self).form_valid(form)
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("article-detail", kwargs={"pk": pk})

class ArticleCreate(CreateView):
    model = Article
    fields = ['title','genre','content']
    # initial = {'genre':''}

    def get_context_data(self, **kwargs):
        context = super(ArticleCreate, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(Blogger, pk = self.kwargs['pk'])
        return context
    def form_valid(self, form):
        form.instance.article = self.request.user
        form.instance.blogger=get_object_or_404(Blogger, pk = self.kwargs['pk'])
        return super(ArticleCreate, self).form_valid(form)
    def get_success_url(self):
        return reverse("article-detail", kwargs={'pk': self.object.id})

