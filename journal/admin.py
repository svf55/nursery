from django.contrib import admin
from journal.models import Journal


@admin.register(Journal)
class DayBookAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_is_studying', 'ts']
    list_filter = ('child__is_studying',)

    def get_name(self, obj):
        return obj.child.name

    def get_is_studying(self, obj):
        return obj.child.is_studying

    def child__is_studying(self, obj):
        stud = obj.child.is_studying.filter(is_studying=True)
        if stud:
            return stud.is_studying

    get_name.short_description = 'name'
    get_is_studying.short_description = 'is studying'

