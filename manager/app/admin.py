from django.contrib import admin

from .models import Rule, RuleType


class RuleAdmin(admin.ModelAdmin):
    fields = ['type', 'mark', 'uri', 'method', 'createtime', 'expired', 'action', 'response', 'duration', 'domain']
    list_display = ('type', 'mark', 'uri', 'method', 'createtime', 'expired', 'action', 'response', 'duration', 'domain')
    list_filter = ['type', 'action']
    search_fields = ['uri']

    def get_ordering(self, request):
        return ['-expired']

class RuleTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'priority', 'lamda', 'enable', 'optional', 'domain']
    list_display = ('name', 'priority', 'lamda', 'enable', 'optional', 'domain')
    list_filter = ['enable', 'optional']
    search_fields = ['name']

    def get_ordering(self, request):
        return ['priority']


admin.site.register(Rule, RuleAdmin)
admin.site.register(RuleType, RuleTypeAdmin)
