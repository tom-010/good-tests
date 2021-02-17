from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

class Desiderata(models.Model):

    slug = AutoSlugField(populate_from='name')
    name = models.CharField(max_length=256)
    video = models.CharField(max_length=1024, null=True)
    description = HTMLField(null=True, blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'name']

    @staticmethod
    def example():
        return Desiderata(
            name='Desiderata-Name',
            description='Desiderata-Description')

    def with_ordering(self, ordering):
        self.ordering = ordering
        return self

    def with_name(self, name):
        self.name = name
        return self

    def __str__(self):
        return self.name