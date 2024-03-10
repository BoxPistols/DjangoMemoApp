from django.shortcuts import render, redirect
from .models import MemoModel
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.models import User  # これは、
from django.db import InternalError
from django.contrib.auth import authenticate, login, logout

from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .serializers import MemoSerializer


# class MemoDetail(DetailView):


class MemoDetail(generics.RetrieveUpdateDestroyAPIView, DetailView):
    template_name = "memoapp/detail.html"
    model = MemoModel
    queryset = MemoModel.objects.all()
    serializer_class = MemoSerializer

    @swagger_auto_schema(
        operation_description="Get a memo by ID",
        responses={
            200: MemoSerializer,
            404: "Memo not found",
        },
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MemoList(ListView):
    template_name = "memoapp/list.html"
    model = MemoModel


class MemoCreate(CreateView):
    template_name = "memoapp/create.html"
    model = MemoModel
    fields = ("title", "memo")
    success_url = reverse_lazy("list")


class MemoDelete(DeleteView):
    template_name = "memoapp/delete.html"
    model = MemoModel
    success_url = reverse_lazy("list")


class MemoUpdate(UpdateView):
    template_name = "memoapp/update.html"
    model = MemoModel
    fields = ("title", "memo")
    success_url = reverse_lazy("list")


def signupfunc(request):  # 新規登録
    if request.method == "POST":  # ユーザー名とパスワードを受け取り、ユーザーを作成
        username = request.POST["username"]  # ユーザー名
        password = request.POST["password"]  # パスワード
        user = User.objects.create_user(username, "", password)
        try:
            user = User.objects.create_user(username, "", password)
            return redirect("login")
        except InternalError:
            return render(request, "signup.html", {"context": "登録できませんでした"})
    return render(request, "signup.html", {"context": "新規登録"})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return render(
                request, "login.html", {"error": "Username or password is incorrect"}
            )
    else:
        return render(request, "login.html")


def logoutfunc(request):
    logout(request)
    return redirect("login")
