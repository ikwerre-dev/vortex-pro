from django.contrib import admin
from django.urls import path,include
from vortex.views import Index
from vortex.views import Loginpage
from vortex.views import Registerpage
from vortex.views import Courses
from vortex.views import Contact
from vortex.views import About

from blog.views import BlogListView, CategoryDetailView, BlogPostDetailView, tagged_view, UpdateCommentView, DeleteCommentView

app_name = 'blog'

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='bloglist'),
    path('article/<slug:slug>/', BlogPostDetailView.as_view(), name='BlogPost-details'),
    path('tag/<slug:slug>/', tagged_view, name="tagged"),
    path('category/<slug:slug>/', CategoryDetailView, name='category_detail'),
    path('article/<int:pk>/update_comment', UpdateCommentView.as_view(), name='Update_comment'),
    path('article/<int:pk>/delete_comment', DeleteCommentView.as_view(), name='Delete_comment'),

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', Index.as_view(),name="index"),
    path('login/', Loginpage.as_view(),name="login"),
    path('register/', Registerpage.as_view(),name="register"),
    path('contact/', Contact.as_view(),name="contact"),
    path('courses/', Courses.as_view(),name="courses"),
    path('about/', About.as_view(),name="about"),
    
]
