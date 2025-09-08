from django.contrib import admin
from .models import Book

# Custom admin configuration
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') 
    list_filter = ('publication_year', 'author')             
    search_fields = ('title', 'author')                       

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)
