from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade', 'subject', 'uploaded_at', 'downloads')
    search_fields = ('title',)
    list_filter = ('grade', 'subject', 'uploaded_at')
