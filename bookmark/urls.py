from django.urls import path

# from .views import BookMarkListView, BookMarkCreateView
from .views import *

urlpatterns = [
    path("", BookMarkListView.as_view(), name='list'),
    path("add/", BookMarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookMarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookMarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookMarkDeleteView.as_view(), name='delete'),

]