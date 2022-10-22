from django.contrib import admin
from education import models

admin.site.register(models.City)
admin.site.register(models.District)
admin.site.register(models.Area)
admin.site.register(models.EnglishInstitute)
admin.site.register(models.NonprofitInstitue)
admin.site.register(models.InstitueActivityType)
admin.site.register(models.StudyPeriod)
admin.site.register(models.EnglishInstituteDefineTerm)
admin.site.register(models.EnglishInstituteRegister)
admin.site.register(models.EnglishInstituteForm)
admin.site.register(models.NonprofitInstituteRegister)
admin.site.register(models.NonprofitInstituteForm)
admin.site.register(models.NonprofitInstituteDefineTerm)
admin.site.register(models.RejectedEnglishInstituteFormList)
admin.site.register(models.RejectedNonprofitInstitueFormList)
admin.site.register(models.Institute)
