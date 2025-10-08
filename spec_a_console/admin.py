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
        'created_by',
        'slug',
        'manufacturer',
        'release_year',
        'approval',
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


@admin.register(SystemReview)
class SystemReviewAdmin(admin.ModelAdmin):
    """
    Admin model for SystemReview.
    """

    def system_creator(self, obj):
        return obj.system.created_by
    system_creator.short_description = 'System Creator'

    list_display = (
        'system',
        'system_creator',
        'reviewer',
        'rating',
        'comment',
        'created_on',
        'approved',
    )
    list_filter = ('approved', 'created_on')
    search_fields = ('system__name', 'reviewer__username', 'comment')
