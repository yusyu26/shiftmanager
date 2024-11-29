from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from .forms import PostForm
from django.http import Http404
from django.utils import timezone
    
class Index(ListView):
    model = Post
    template_name = 'shifts/post_list.html'
    # クエリセットを取得し、日付順に並べ替え
    def get_queryset(self):
        #今日の日付取得
        today = timezone.now().date()
        #過去のシフトを取り除く（今日は含む）
        future_shifts = Post.objects.filter(date__gte=today)
        no_substitute_shifts = future_shifts.filter(substitute='').order_by('date')
        filled_substitute_shifts = future_shifts.exclude(substitute='').order_by('date')
        
        return no_substitute_shifts, filled_substitute_shifts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # `get_queryset` で取得したデータを `context` に追加
        no_substitute_shifts, filled_substitute_shifts = self.get_queryset()
        context['no_substitute_shifts'] = no_substitute_shifts
        context['filled_substitute_shifts'] = filled_substitute_shifts
        return context

class Detail (DetailView):
    model = Post

from django.views.generic.edit import CreateView, UpdateView
class Create(CreateView):
    model = Post
    form_class = PostForm
    success_url = "/"

class Confirmsubstitute(UpdateView):
    model = Post
    fields = ['substitute']
    success_url = "/"
    template_name = 'shifts/confirm.html'
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        # substituteが空でない場合、アクセス制限
        if post.substitute:
            raise Http404("このシフトはすでに埋まっています。")
        return post

    def form_valid(self, form):
        # フォームが有効な場合の処理
        return super().form_valid(form)