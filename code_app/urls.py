from django.urls import path
from . import views

app_name = 'code_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('contact-us', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('career', views.career, name='career'),
    path('quarry-crusher-erp', views.quarry_crusher, name='quarry_crusher'),
    path('ready-mix-concrete-erp', views.ready_mix_erp, name='ready_mix_erp'),
    path('brick-manufacturing-erp', views.brick_erp, name='brick_erp'),

    path('blog', views.blogs, name='blogs'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    path('customer-stories', views.customerStories, name='customerStories'),

    path('events', views.events, name='events'),

    path('site-visits', views.siteVisits, name='siteVisits'),

    path('resources', views.resources, name='resources'),

    path('quarry-landing', views.quarryLanding, name='quarryLanding'),

    path('capture-landing-lead/', views.landingLeadCapture, name='landing_lead_capture'),

    path('ready-mix-landing', views.readymixLanding, name='readymixLanding'),

    path('brick-manufacturing-landing', views.brickLanding, name='brickLanding'),

    path('privacy-policy', views.privacy, name='privacy'),

    path('terms-and-conditions', views.term, name='term'),
]