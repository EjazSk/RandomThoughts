from django.contrib import admin
from .models import RT
from registration.models import RegistrationProfile  
# Register your models here.

#admin.site.register(RegistrationProfile)

class AdminRegistrationProfile(admin.ModelAdmin):
	list_display=['username','email']
	class Meta:
		model = RegistrationProfile

admin.site.register(RT)
#admin.site.register(RegistrationProfile,AdminRegistrationProfile)		