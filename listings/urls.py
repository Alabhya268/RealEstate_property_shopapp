from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.search, name='listing'),
    path('search', views.search, name='search')
]
