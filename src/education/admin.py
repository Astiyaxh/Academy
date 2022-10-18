from django.contrib import admin
from education import models

admin.site.register(models.City)
admin.site.register(models.District)
admin.site.register(models.Area)
admin.site.register(models.InstituteEnglish)
admin.site.register(models.InstitueNonProfit)
admin.site.register(models.InstitueActivityType)
admin.site.register(models.StudyPeriod)
admin.site.register(models.InstituteEnglishDefineTerm)
admin.site.register(models.InstituteEnglishRegister)
admin.site.register(models.InstituteEnglishForm)