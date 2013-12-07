from django.contrib import admin
from polls.models import Poll

# Customize admin UI for models

class PollAdmin(admin.ModelAdmin):
    fieldsets = []
    fieldsets.append((None, {'fields': ['question']}));
    fieldsets.append(('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}));

# Register your models here.

admin.site.register(Poll, PollAdmin)

