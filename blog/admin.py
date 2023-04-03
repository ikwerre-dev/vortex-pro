from django.contrib import admin
from blog.models import Tag,Category,WriterProfile,BlogPost,BlogComment,About,Roles

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(WriterProfile)
admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(About)
admin.site.register(Roles)
