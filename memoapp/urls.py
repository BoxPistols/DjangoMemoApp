from django.urls import path
from .views import MemoList, MemoDetail, MemoCreate, MemoDelete, MemoUpdate

urlpatterns = [
    path("", MemoList.as_view(), name="list"),
    path("detail/<int:pk>/", MemoDetail.as_view(), name="detail"),
    path("create/", MemoCreate.as_view(), name="create"),
    path("delete/<int:pk>/", MemoDelete.as_view(), name="delete"),
    path("update/<int:pk>/", MemoUpdate.as_view(), name="update"),
]
