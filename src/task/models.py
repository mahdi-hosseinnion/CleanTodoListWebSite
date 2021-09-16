from django.db import models

# Create your models here.


class Task(models.Model):
    uuid                  = models.CharField(max_length = 60, unique = True, null = False, blank = False)
    title               = models.CharField(max_length = 60, null = False, blank = False)
    body                = models.TextField(null = True, blank = True)
    done                = models.BooleanField(default = False, null = False, blank = False)
    updated_at          = models.BigIntegerField(null = False, blank = False)
    created_at          = models.BigIntegerField(null = False, blank = False)
