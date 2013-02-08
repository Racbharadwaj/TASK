from portfolio.models import *
from django.contrib import admin

class EducationInline(admin.StackedInline):
    model = Education
    
##    extra = 3
### class portfolioAdmin(admin.ModelAdmin):
##
##
    
class GeneralAdmin(admin.ModelAdmin):
##    fieldsets = [
##        (None, {'fields':['name'],'classes': ['education10']}),
##    ]
    inlines = [EducationInline]
    
admin.site.register(General, GeneralAdmin)
