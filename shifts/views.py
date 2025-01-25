from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post
from .forms import PostForm
from django.http import Http404
from django.utils import timezone
from .utils.line_notify import send_line_notification
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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


class Create(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = "/"
    
    def form_valid(self, form):
        # フォームデータを保存
        response = super().form_valid(form)
        
        # LINE通知のロジック
        send_line_notification(form.instance)
        
        return response

class Confirmsubstitute(LoginRequiredMixin, UpdateView):
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
    
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'shifts/signup.html',{'error':'このユーザーは既に登録されています。'})
    return render(request, 'shifts/signup.html',{'some':100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'shifts/login.html',{'context':'登録情報が正しくありません'})
    return render(request, 'shifts/login.html',{}) 
    
def logoutfunc(request):
    logout(request)
    return redirect('/')
    