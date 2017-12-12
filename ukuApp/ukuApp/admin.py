from django.contrib import admin
from .models import Agreement
from .models import Activity

admin.site.register(Agreement)
admin.site.register(Activity)