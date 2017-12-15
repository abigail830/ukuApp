from django.contrib import admin
from .models import Agreement
from .models import Activity
from .models import Product
from .models import SignupInfo


class MyAdminSite(admin.AdminSite):
    site_header = 'ukuApp站点管理 '
    site_header = 'ukuApp管理网站'

admin_site = MyAdminSite()

admin_site.register(Agreement)
admin_site.register(Activity)
admin_site.register(Product)
admin_site.register(SignupInfo)
