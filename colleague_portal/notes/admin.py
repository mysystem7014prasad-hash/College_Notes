from django.contrib import admin
from .models import Note, Subject, PreviousPaper

# Register Subject
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'semester']
    search_fields = ['name', 'code']

# Register Note
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'category', 'uploaded_by', 'downloads', 'uploaded_at']
    list_filter = ['subject', 'category', 'uploaded_by']
    search_fields = ['title', 'description']
    readonly_fields = ['uploaded_at', 'downloads']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subject', 'category', 'description')
        }),
        ('File & Metadata', {
            'fields': ('file', 'uploaded_by')
        }),
        ('Tracking', {
            'fields': ('downloads', 'uploaded_at')
        }),
    )

# Register PreviousPaper
@admin.register(PreviousPaper)
class PreviousPaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'semester', 'year', 'category', 'uploaded_by', 'downloads', 'uploaded_at']
    list_filter = ['subject', 'semester', 'year', 'category']
    search_fields = ['title', 'subject__name', ]
    raw_id_fields = ['uploaded_by']
    readonly_fields = ['uploaded_at', 'downloads']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subject', 'semester', 'year')
        }),
        ('File & Metadata', {
            'fields': ('file', 'category', )
        }),
        ('Tracking', {
            'fields': ('uploaded_by', 'downloads', 'uploaded_at')
        }),
    )