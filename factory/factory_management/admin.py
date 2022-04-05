from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


admin.site.register(WorkerRelation)


class PositionFilter(admin.SimpleListFilter):
    title = _('position')

    parameter_name = 'by_position'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no',  _('No')),
        )

    def queryset(self, request, queryset):
        return queryset.order_by('position')


@admin.register(Worker)
class AdminView(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'salary', 'paid_salary', 'get_head')
    list_display_links = ['get_head']
    list_filter = [PositionFilter]

