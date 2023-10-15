from django.db import models


class Logging(models.Model):
    requested_date = models.DateTimeField(auto_now_add=True)
    source_ip = models.GenericIPAddressField()
    request_data = models.JSONField()
    response_data = models.JSONField()
