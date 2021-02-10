from rest_framework import viewsets
from .serializers import OnboardingSerializer, StepSerializer
from .models import Onboarding, Step


class OnboardingViewSet(viewsets.ModelViewSet):
    queryset = Onboarding.objects.all()
    serializer_class = OnboardingSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
