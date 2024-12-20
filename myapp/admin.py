from django.contrib import admin
from .models import Form, Field, UserFormSubmission

class FieldInline(admin.TabularInline):
    model = Field

class FormAdmin(admin.ModelAdmin):
    inlines = [FieldInline]

admin.site.register(Form, FormAdmin)
admin.site.register(UserFormSubmission)
