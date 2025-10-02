from django.contrib import admin
from .models import ConsoleSystem, SystemReview
from django_summernote.admin import SummernoteModelAdmin  # type: ignore


@admin.register(ConsoleSystem)
class ConsoleSystemAdmin(SummernoteModelAdmin):
    """
    Admin model for ConsoleSystem, using Summernote for
    detailed_description.
    """

    list_display = (
        'name',
        'slug',
        'manufacturer',
        'release_year',
        'approval',
        'created_by',
        'created_on',
        'updated_on',
    )
    search_fields = (
        'name', 'manufacturer', 'release_year', 'detailed_description'
    )
    list_filter = (
        'approval', 'manufacturer', 'release_year', 'created_on', 'updated_on'
    )
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('detailed_description',)


# Register your models here.

admin.site.register(SystemReview)
