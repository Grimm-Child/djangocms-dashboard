from django.conf.urls import url
from djangocms_dashboard.views import home, plugins_list, apphooks_list, plugin_detail, apphook_detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^plugins/$', plugins_list, name='plugins_list'),
    url(r'^apphooks/$', apphooks_list, name='apphooks_list'),
    url(r'^plugin_detail/(?P<plugin_type>\w+)$', plugin_detail, name='plugin_detail'),
    url(r'^apphook_detail/(?P<apphook_class>\w+)$', apphook_detail, name='apphook_detail'),
    # url(r'^plugins/export/csv/$', 'djangocms_dashboard.views.export', name='export_csv'),
]
