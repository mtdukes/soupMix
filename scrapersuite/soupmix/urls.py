from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^export_csv', views.export_csv, name='export_csv'),
    url(r'^ajax',views.ajax_view,name='ajax_view'),
    url(r'^get_frag',views.update_fragment,name='update_fragment'),
    #capture and pass in a slug for a scraper
    url(r'^(\w+)',views.index,name='index'),
]