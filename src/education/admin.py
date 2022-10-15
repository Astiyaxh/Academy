from django.contrib import admin
from education import models

admin.site.register(models.City)
admin.site.register(models.District)
admin.site.register(models.Area)
admin.site.register(models.EnglishInstitute)
admin.site.register(models.NonProfitInstitue)
admin.site.register(models.InstitueActivityType)
admin.site.register(models.StudyPeriod)
admin.site.register(models.EnglishInstituteDefineTerm)
admin.site.register(models.EnglishInstituteRegister)
admin.site.register(models.EnglishInstituteForm)
admin.site.register(models.NoneProfitForm)
admin.site.register(models.NoneProfitFormTable)
admin.site.register(models.NonProfitInstituteDefineTerm)