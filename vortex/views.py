from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

class Loginpage(TemplateView):
    template_name = 'login.html'

class Registerpage(TemplateView):
    template_name = 'register.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Courses(TemplateView):
    template_name = 'courses.html'

class About(TemplateView):
    template_name = 'about.html'

