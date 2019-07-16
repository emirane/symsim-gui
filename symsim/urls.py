from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from symsim.views import base_view, example_nica_view,\
    example_cas_view, login_view, registration_view, account_view, \
    project_view, usage_view, technology_view, get_simulation_report, ajax_graph, ajax_graph2,\
    create_model_name, get_user_model,\
    create_model, create_comp_node, create_data_generator, create_disk_server, create_switch

urlpatterns = [
    url(r'^$', base_view, name='base'),
    url(r'^example_nica/$', example_nica_view, name='example_nica'),
    url(r'^example_cas/$', example_cas_view, name='example_cas'),
    url(r'^login/$', login_view, name='login'),
    url(r'^registration/$', registration_view, name='register'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('base')), name='logout'),
    url(r'^account/$', get_user_model, name='get_user_model'),
    url(r'^create_model_name/$', create_model_name, name='create_model_name'),
    url(r'^account/$', account_view, name='account'),
    url(r'^create_model/(?P<id>\d+)/$', create_model, name='create_model'),
    url(r'^project/$', project_view, name='project'),
    url(r'^usage/$', usage_view, name='usage'),
    url(r'^technology/$', technology_view, name='technology'),
    url(r'^create_comp_node/$', create_comp_node, name='create_comp_node'),
    url(r'^create_data_gen/$', create_data_generator, name='create_data_generator'),
    url(r'^create_disk_server/$', create_disk_server, name='create_disk_server'),
    url(r'^create_switch/$', create_switch, name='create_switch'),
    url(r'^graphics-data/$', ajax_graph, name='ajax_graph'),
    url(r'^graphics-data2/$', ajax_graph2, name='ajax_graph2'),
    url(r'^graphics/$', get_simulation_report, name='get_simulation_report'),



]