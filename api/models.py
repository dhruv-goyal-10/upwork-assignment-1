from django.db import models


class Worker(models.Model):

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"
        
    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class Unit(models.Model):

    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"
        
    def __str__(self):
        return f"({self.id}) {self.name}"


class Visit(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"
