from django.contrib import admin
from django.db import models

class Org(models.Model):
    org_id = models.CharField(max_length=256)
    owner = models.CharField(max_length=256 )
    json_url = models.CharField(max_length=256, blank=True, null=True)
    json_text = models.TextField(blank=True, null=True)
    lif_balance = models.CharField(max_length=20, blank=True, null=True)
    trust_clues = models.TextField(blank=True, null=True)
    def str(self):
        return self.org_id
    class Admin(admin.ModelAdmin):
        list_display = ['org_id', 'json_url', 'lif_balance']
