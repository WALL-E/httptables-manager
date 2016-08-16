from django.contrib import admin

from .models import Role, RoleType


class RoleAdmin(admin.ModelAdmin):
    fields = ['type', 'mark', 'uri', 'method', 'createtime', 'expired', 'action', 'response', 'duration']
    list_display = ('type', 'mark', 'uri', 'method', 'createtime', 'expired', 'action', 'response', 'duration')
    list_filter = ['type', 'action']
    search_fields = ['uri']

    def get_ordering(self, request):
        return ['-expired']

class RoleTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'priority', 'lamda', 'enable']
    list_display = ('name', 'priority', 'lamda', 'enable')
    list_filter = ['enable']
    search_fields = ['name']

    def get_ordering(self, request):
        return ['priority']


admin.site.register(Role, RoleAdmin)
admin.site.register(RoleType, RoleTypeAdmin)
