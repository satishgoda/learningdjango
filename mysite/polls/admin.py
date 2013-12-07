from django.contrib import admin
from polls.models import Poll, Choice

# Customize admin UI for models

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = []
    fieldsets.append((None, {'fields': ['question']}));
    fieldsets.append(('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}));

    inlines = [ChoiceInline]

# Register your models here.

admin.site.register(Poll, PollAdmin)