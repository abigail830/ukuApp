from django.contrib import admin
from .models import Agreement
from .models import Activity
from .models import Product
from .models import SignupInfo
from .models import ActivitySignupMapping
from .models import ProductActivityMapping

admin.site.register(Agreement)
admin.site.register(Activity)
admin.site.register(Product)
admin.site.register(SignupInfo)
admin.site.register(ActivitySignupMapping)
admin.site.register(ProductActivityMapping)
