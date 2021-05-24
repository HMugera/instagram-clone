from django.contrib import admin

from .models import Profile,Post,Comments,Follow


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Follow)
