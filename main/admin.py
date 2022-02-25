from django.contrib import admin

# Register your models here.
from main.models import Note



class NoteAdmin(admin.ModelAdmin):
    list_display =  ('title', 'content', 'created_at' ,'updated_at' )

admin.site.register(Note, NoteAdmin)