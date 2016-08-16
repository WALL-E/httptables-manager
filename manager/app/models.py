from django.db import models

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

    class Meta:
        managed = False
        db_table = 'role'


class RoleType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    priority = models.IntegerField(blank=True, null=True)
    lamda = models.CharField(max_length=1024)
    enable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_type'

    def __unicode__(self):
        return self.name
 
    def __str__(self):
        return self.name
