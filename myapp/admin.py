from django.contrib import admin

# Register your models here.
from myapp.models import Snippet, Tag

admin.site.register(Snippet)
admin.site.register(Tag)
