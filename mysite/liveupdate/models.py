from django.db import models
from django.utils import timezone
from django.contrib import admin


class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        localtime = timezone.localtime(self.timestamp)
        return "[%s] %.8s" % (
            localtime.strftime("%Y-%m-%d %H:%M:%S"),
            self.text[0:8]
        )

admin.site.register(Update)
