from django.db import models


# Create your models here.


class Att(models.Model):
    timingID = models.IntegerField()
    timeFor = models.CharField(max_length=20, null=False, blank=False)
    classesID = models.IntegerField()
    sectionID = models.IntegerField()
    entryTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.timeFor
