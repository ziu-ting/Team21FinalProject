from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
#import captcha

urlpatterns = [
    url(r'^$', views.index),
    url(r'^english/', views.english),
    url(r'^loading/', views.loading),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
