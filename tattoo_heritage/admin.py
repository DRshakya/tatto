from django.contrib import admin
from tattoo_heritage.models import Artist, gallery1,artist_work

# Register your models here.
admin.site.register(Artist)
admin.site.register(gallery1)
admin.site.register(artist_work)

class ModelAdmin(admin.ModelAdmin):


    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.save(request=request)
        return instance