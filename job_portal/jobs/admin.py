from django.contrib import admin
from .models import Job # import the model that you have created here

# For Autopopulation of creator in Job creation
class JobAdmin(admin.ModelAdmin):
    exclude = ('creator',)

    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creator=request.user)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

    def get_list_display(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return ('position_name','creator',)
        else:
            return ('position_name', )



# Register your models here.
admin.site.register(Job, JobAdmin)