from django.db import models
from autoslug import AutoSlugField

class Desiderata(models.Model):

    slug = AutoSlugField(populate_from='name')
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    ordering = models.IntegerField(default=0)

    @staticmethod
    def example():
        return Desiderata(
            name='Desiderata-Name',
            description='Desiderata-Description')