from django.contrib import admin

from .models import CV, Education, WorkExperience

admin.site.register(CV)
admin.site.register(Education)
admin.site.register(WorkExperience)