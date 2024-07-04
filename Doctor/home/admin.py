from django.contrib import admin
from home.models import Patient,PatientList



class PatientListInline(admin.TabularInline):
    model = PatientList
    fields = ('created', 'do', 'price', 'paid','remaining_money_display')
    readonly_fields = ('created','remaining_money_display')
    
    
    def remaining_money_display(self,obj):
        return obj.remaining_money()


class PatientAdmin(admin.ModelAdmin):
    list_display = ('doctor','full_name',)
    raw_id_fields = ('doctor', )
    inlines = (PatientListInline,)
    readonly_fields = ('total_price_display',)

    def total_price_display(self,obj):
        return obj.get_total_price()

admin.site.register(Patient,PatientAdmin)