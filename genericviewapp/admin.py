from django.contrib import admin
from genericviewapp import models
# Register your models here.
admin.site.register([
    models.Student,
    models.College,
])