from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView   # ← import para la redirección

urlpatterns = [
    # Panel de administración
    path("admin/", admin.site.urls),

    # Backend de inventario
    path("inventario/", include("inventario.urls")),

    # Login / logout / password-reset
    path("accounts/", include("django.contrib.auth.urls")),

    # Redirigir la raíz "/" al listado de productos
    path("", RedirectView.as_view(url="/inventario/productos/", permanent=False)),
]
