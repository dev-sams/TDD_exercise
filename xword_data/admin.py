from django.contrib import admin

from xword_data.models import Puzzle, Entry, Clue
# Register your models here.

admin.site.register(Puzzle)
admin.site.register(Entry)
admin.site.register(Clue)
