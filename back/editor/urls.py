from rest_framework import routers
from .views import MenuViewSet, InfoCardViewSet

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'infocard', InfoCardViewSet)

urlpatterns = router.urls