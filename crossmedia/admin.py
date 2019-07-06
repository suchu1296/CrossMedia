from django.contrib import admin
from crossmedia.models import FriendList, Group, GroupMember, Event

# Register your models here.

admin.site.register(FriendList)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Event)
