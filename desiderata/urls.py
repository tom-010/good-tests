from django.urls import path
from desiderata import views

app_name = 'desiderata'

urlpatterns = [
    path('<desiderata_slug>', views.DetailView.as_view(), name='detail'),
]