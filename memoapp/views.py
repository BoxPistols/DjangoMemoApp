from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import MemoModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

class MemoList(ListView):
    template_name = 'memoapp/list.html'
    model = MemoModel

class MemoDetail(DetailView):
    template_name = 'memoapp/detail.html'
    model = MemoModel

class MemoCreate(CreateView):
    template_name = 'memoapp/create.html'
    model = MemoModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('list')

class MemoDelete(DeleteView):
    template_name = 'memoapp/delete.html'
    model = MemoModel
    success_url = reverse_lazy('list')

class MemoUpdate(UpdateView):
    template_name = 'memoapp/update.html'
    model = MemoModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('list')

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
        try:
            user.save()
            return render(request, 'signup.html', {'context': '登録完了'})
        except:
            return render(request, 'signup.html', {'context': '登録できませんでした'})
    return render(request, 'signup.html', {'context': '新規登録'})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'login.html')