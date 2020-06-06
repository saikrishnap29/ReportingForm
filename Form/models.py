from django.db import models

# Create your models here.
class Reporting(models.Model):
    LOCATION_AS_CHOICES = (
    ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
    ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
    ("Puducherry", "Puducherry"))

    # state = models.CharField(choices=LOCATION_AS_CHOICES, max_length=255, null=True, blank=True)
    location=models.CharField(max_length=100, choices=LOCATION_AS_CHOICES,)
    incident_description=models.TextField(max_length=200)
    date=models.DateField()
    time=models.TimeField()
    incident_location=models.TextField(max_length=200)
    SEVERITY_AS_CHOICES = (
        ("Critical", "Critical"),
        ("Major", "Major"),
        ("Moderate", "Moderate"),
        ("Minor", "Minor"),
        ("Cosmetic", "Cosmetic"),
    )
    incident_severity = models.CharField(max_length=100, choices=SEVERITY_AS_CHOICES,)
    suspected_cause=models.TextField()
    immediate_action_taken=models.TextField()
    environmental_incident=models.BooleanField("Environmental Incident")
    injury_illness=models.BooleanField("Injury illness")
    property_damage=models.BooleanField("Property Damage")
    vehicle_damage=models.BooleanField("Vehicle Damage")
    reported_by=models.CharField(max_length=100)