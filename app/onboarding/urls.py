from django.urls import include, path
from rest_framework import routers
from .views import OnboardingViewSet, StepViewSet

router = routers.DefaultRouter()
router.register(r'steps', StepViewSet, basename='steps')
router.register(r'onboardings', OnboardingViewSet, basename='onboardings')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
