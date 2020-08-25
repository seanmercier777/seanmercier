from django.conf.urls import url

from . import views

urlpatterns = [

    url('cv/', views.cv, name='cv'),
    url('projects/', views.projects, name='projects'),
    url('contact/', views.contact, name='contact'),
    url('', views.index, name='index'),
    # url(r'^admin/', admin.site.urls),
]
