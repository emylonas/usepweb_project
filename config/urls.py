# -*- coding: utf-8 -*-

# import usep_app
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView


admin.autodiscover()


urlpatterns = patterns('',

    url( r'^usep/admin/links/$',  'usep_app.views.admin_links', name='admn_links_url' ),
    url( r'^usep/admin/', include(admin.site.urls) ),

    url( r'^usep/info/$',  'usep_app.views.info', name='info_url' ),

    url( r'^usep/collections/$',  'usep_app.views.collections', name='collections_url' ),
    url( r'^usep/collections/(?P<collection>[^/]+)/$',  'usep_app.views.collection', name='collection_url' ),
    url( r'^usep/inscription/(?P<inscription_id>[^/]+)/$', 'usep_app.views.display_inscription', name='inscription_url' ),

    url( r'^usep/publications/$',  'usep_app.views.publications', name='publications_url' ),
    url( r'^usep/publication/(?P<publication>[^/]+)/$', 'usep_app.views.pub_children', name='publication_url' ),

    url( r'^usep/texts/$',  'usep_app.views.texts', name='texts_url' ),
    url( r'^usep/links/$',  'usep_app.views.links', name='links_url' ),
    url( r'^usep/about/$',  'usep_app.views.about', name='about_url' ),
    url( r'^usep/contact/$',  'usep_app.views.contact', name='contact_url' ),

    url( r'^usep/search/$', 'usep_app.search.search_form', name='search_url'),
    url( r'^usep/search/results/$', 'usep_app.search.results', name='search_results_url'),

    url( r'^usep/error_check/$', 'usep_app.views.error_check', name='error_check_url' ),  # only generates error if DEBUG == True

    url( r'^usep/$',  RedirectView.as_view(pattern_name='collections_url') ),

    )
