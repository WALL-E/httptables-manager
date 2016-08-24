from django.db import models
from project import settings
import requests
import logging
import http

logger = logging.getLogger("django")

# Create your models here.

class Role(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=64, null=False)
    mark = models.CharField(max_length=1024, null=False)
    uri = models.CharField(max_length=1024, null=False)
    method = models.CharField(max_length=64, null=False)
    createtime = models.IntegerField(blank=True, null=False)
    expired = models.IntegerField(blank=True, null=False)
    action = models.CharField(max_length=64, null=False)
    response = models.CharField(max_length=1024, null=False)
    duration = models.IntegerField(blank=True, null=False)
    domain = models.CharField(max_length=64, null=False)

    def __unicode__(self):
        return "%s_%s" %(self.type, self.mark)
 
    def __str__(self):
        return "%s_%s" %(self.type, self.mark)
   
    def save(self, *args, **kw):
        for url in settings.HTTPTABLES_NOTIFY_URL:
            try:
                response = requests.get(url)
                if response.status_code == http.client.OK:
                    logger.info("[httptables notify] %s: ok" % (url))
                else:
                    logger.error("[httptables notify] %s: failed" % (url))
            except Exception as e:
                logger.error("[httptables notify] %s: %s" % (url, e))
        super(Role, self).save(*args, **kw)

    class Meta:
        db_table = 'role'


class RoleType(models.Model):
    ENABLE_CHOICES = (
        (0, "停用"),
        (1, "启用"),
    )
    OPTIONAL_CHOICES = (
        (0, "不可选"),
        (1, "可选"),
    )
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    priority = models.IntegerField(blank=True, null=False)
    lamda = models.CharField(max_length=1024, null=False)
    enable = models.IntegerField(choices=ENABLE_CHOICES, default=1, null=False)
    optional = models.IntegerField(choices=OPTIONAL_CHOICES, default=0, null=False)
    domain = models.CharField(max_length=64, null=False)

    def __unicode__(self):
        return self.name
 
    def __str__(self):
        return self.name

    def save(self, *args, **kw):
        for url in settings.HTTPTABLES_NOTIFY_URL:
            try:
                response = requests.get(url)
                if response.status_code == http.client.OK:
                    logger.info("[httptables notify] %s: ok" % (url))
                else:
                    logger.error("[httptables notify] %s: failed" % (url))
            except Exception as e:
                logger.error("[httptables notify] %s: %s" % (url, e))
        super(RoleType, self).save(*args, **kw)

    class Meta:
        db_table = 'role_type'
        unique_together = (("name", "domain"),)
