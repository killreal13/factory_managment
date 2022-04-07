from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


class PositionFilter(admin.SimpleListFilter):
    title = _('position')

    parameter_name = 'by_position'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        return queryset.order_by('position')


class LevelFilter(admin.SimpleListFilter):
    title = _('level')

    parameter_name = 'by_level'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        return queryset.order_by('level')


@admin.register(Worker)
class AdminView(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'salary', 'paid_salary', 'get_head')
    list_display_links = ['get_head']
    list_filter = [PositionFilter, LevelFilter]

    @admin.action(description='Clear payments information')
    def clear_payments_information(self, request, queryset):
        queryset.update(paid_salary=0)
        self.message_user(request, f'Selected workers payments information is cleared')

    admin.site.add_action(clear_payments_information)


admin.site.register(WorkerRelation)