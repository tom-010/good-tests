from django.shortcuts import render, get_object_or_404
from django.views import View
from desiderata.models import Desiderata

class DetailView(View):

    def get(self, request, desiderata_slug, *args, **kwargs):
        desiderata = get_object_or_404(Desiderata, slug=desiderata_slug)
        context = {
            'desiderata': desiderata
        }
        return render(request, 'desiderata/detail.html', context)