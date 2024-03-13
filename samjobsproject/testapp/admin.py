from django.contrib import admin
from testapp.models import hydjobs
from testapp.models import punejobs
from testapp.models import bangulorjobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['interviewdate','companyname','tittle','qualification','address','email','phno']
class punejobsAdmin(admin.ModelAdmin):
    list_display=['interviewdate','companyname','tittle','qualification','address','email','phno']
class bangulorjobsAdmin(admin.ModelAdmin):
    list_display=['interviewdate','companyname','tittle','qualification','address','email','phno']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
admin.site.register(bangulorjobs,bangulorjobsAdmin)
