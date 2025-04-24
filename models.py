from django.db import models

# Create your models here.
class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    moisture = models.IntegerField()
    temperature = models.IntegerField()
    humidity = models.IntegerField(null=True, blank=True)  # Optional enhancement

# class IrrigationControl(models.Model):
#     status = models.BooleanField(default=False)
#     last_updated = models.DateTimeField(auto_now=True)
# from django.db import models

class IrrigationControl(models.Model):
    status = models.BooleanField(default=False)  # ON/OFF status of the irrigation
    mode = models.CharField(max_length=10, choices=[('manual', 'Manual'), ('auto', 'Automatic')], default='auto')  # Control mode (manual or automatic)
    pump_status = models.BooleanField(default=False)  # Pump status (running or stopped)
    flow_rate = models.FloatField(null=True, blank=True)  # Water flow rate in L/min
    schedule_time = models.DateTimeField(null=True, blank=True)  # Time the irrigation is scheduled to run
    last_updated = models.DateTimeField(auto_now=True)  # Last update timestamp

    def __str__(self):
        return f"Irrigation Control - {'ON' if self.status else 'OFF'}"
