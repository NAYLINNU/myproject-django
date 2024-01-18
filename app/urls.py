from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='app/main.html')),
    path('open', views.OpenView.as_view(), name='open'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('manual', views.ManualProtect.as_view(), name='manual'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('python', views.DumpPython.as_view(), name='python'),
]
