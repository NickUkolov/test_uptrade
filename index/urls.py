from django.urls import path

from index.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', IndexView.as_view(), name='menu_item'),
]
