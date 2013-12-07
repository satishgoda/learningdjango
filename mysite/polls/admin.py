from django.contrib import admin
from polls.models import Poll, Choice

# Customize admin UI for models

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = []
    fieldsets.append((None, {'fields': ['question']}));
    fieldsets.append(('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}));

    inlines = [ChoiceInline]
    
    list_display = ['question', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    
    search_fields = ['question']

# Register your models here.

admin.site.register(Poll, PollAdmin)