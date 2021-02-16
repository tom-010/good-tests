from django.urls import path
from desiderata import views

app_name = 'desiderata'

urlpatterns = [
    path('detail/<desiderata_slug>', views.DetailView.as_view(), name='detail'),
    path('all', views.DesiderataListView.as_view(), name='all'),
]