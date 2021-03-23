from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rest_framework import routers

import store.views
import store.api_views


# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
# router.register(r'accouts', AccountViewSet)
# urlpatterns += router.urls

urlpatterns = [
    path('api/v1/products/', store.api_views.ProductList.as_view()),  # Python3
    # path('', include(router.urls)),
    
    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('cart/', store.views.cart, name='shopping-cart'),
    path('', store.views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
