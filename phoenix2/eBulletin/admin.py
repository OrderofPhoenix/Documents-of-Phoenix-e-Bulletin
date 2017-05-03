from django.contrib import admin
from eBulletin.models import Bulletin,Userprofile,Message,Comment
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Bulletin)
admin.site.register(Message)
admin.site.register(Comment)
