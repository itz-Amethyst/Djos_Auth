from django.contrib import admin
from django.urls import path , include , re_path
from drf_spectacular.views import SpectacularAPIView , SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    #? Djoser
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('auth/', include('core.api.router.urls')),

    # ! Docs
    path('api/schema/' , SpectacularAPIView.as_view() , name = 'schema') ,
    path('api/docs/' , SpectacularSwaggerView.as_view(url_name = 'schema') , name = 'swagger-ui') ,
]
