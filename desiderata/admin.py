from django.contrib import admin
from desiderata.models import Desiderata
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class DesiderataResource(resources.ModelResource):
    class Meta:
        model = Desiderata
class DesiderataAdmin(ImportExportModelAdmin):
    resource_class = DesiderataResource

admin.site.register(Desiderata,DesiderataAdmin)