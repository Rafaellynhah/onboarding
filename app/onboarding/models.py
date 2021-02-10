from django.db import models


class Step(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, blank=False)
    start_data = models.DateTimeField(null=False)
    end_data = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return self.name


class Onboarding(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, blank=False)
    steps = models.ManyToManyField(Step)

    def __str__(self) -> str:
        return self.name
