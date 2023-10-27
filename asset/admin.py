from django.contrib import admin
from asset.models import cred,it_asset,voip

admin.site.register(cred),
admin.site.register(voip),
admin.site.register(it_asset),
