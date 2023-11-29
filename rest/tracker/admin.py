from django.contrib import admin
from .models import User, App, Entry, Comment, Attachment

admin.site.register(User)
admin.site.register(App)
admin.site.register(Entry)
admin.site.register(Comment)
admin.site.register(Attachment)