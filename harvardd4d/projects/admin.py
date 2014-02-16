from django.contrib import admin
import projects.models

# Register your models here.
admin.site.register(projects.models.Tag)
admin.site.register(projects.models.Partner)
admin.site.register(projects.models.Project)
admin.site.register(projects.models.JobOpportunity)
