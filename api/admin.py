from django.contrib import admin
from api.models import Worker, Unit, Visit


class WorkerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone_number", "created_at", "updated_at"]
    search_fields = ["name", "phone_number"]
    list_filter = ["created_at", "updated_at"]
    
    
class UnitAdmin(admin.ModelAdmin):
    
    list_display = ["id", "name", "worker", "created_at", "updated_at"]
    search_fields = ["name", "worker__name"]
    list_filter = ["created_at", "updated_at"]


class VisitAdmin(admin.ModelAdmin):
    
    list_display = ["id", "unit", "timestamp"]
    search_fields = ["unit__name", "unit__worker__name"]
    list_filter = ["timestamp"]

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Visit, VisitAdmin)