from email.policy import default
from enum import unique
from random import choices
from tabnanny import verbose
from unicodedata import name
from django.db import models
from user.models import User

Active   = 1
Deactive = -1
StatusChoices = (
    (Active, "فعال"),
    (Deactive, "غیر فعال"),
)

Private_Person = 1
legal_Person   = 2
PermissionChoieces = (
    (Private_Person, "شخص حقیقی"),
    (legal_Person, "شخص حقوقی"),
)

Male    = 1
Female  = 2
SexChoieces = (
    (Male, "مرد"),
    (Female, "زن"),
)

class City(models.Model):
    """
    شهر
    """
    class Meta:
        verbose_name = 'A- شهر'
        verbose_name_plural = 'A- شهر'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.id)

class District(models.Model):
    """
    منطقه
    """
    class Meta:
        verbose_name = 'B- منطقه'
        verbose_name_plural = 'B- منطقه'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.id)

class Area(models.Model):
    """
    ناحیه
    """
    class Meta:
        verbose_name = 'C- ناحیه'
        verbose_name_plural = 'C- ناحیه'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)

class InstitueActivityType(models.Model):
    """
    نوع فعالیت موسسه
    """
    class Meta:
        verbose_name = 'D- نوع فعالیت موسسه'
        verbose_name_plural = 'D- نوع فعالیت موسسه'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class StudyPeriod(models.Model):
    """
    دوره تحصیلی
    """
    class Meta:
        verbose_name = 'E- دوره تحصیلی'
        verbose_name_plural = 'E- دوره تحصیلی'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class InstituteEnglish(models.Model):
    """
    مرکز آموزش زبان خارجه
    """
    class Meta:
        verbose_name = 'F- مرکز آموزش زبان خارجه'
        verbose_name_plural = 'F- مرکز آموزش زبان خارجه'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class InstituteEnglishDefineTerm(models.Model):
    """
    تعریف سطح دوره مرکز آموزش زبان خارجی
    """
    class Meta:
        verbose_name = 'G- تعریف سطح دوره مرکز آموزش زبان خارجی'
        verbose_name_plural = 'G- تعریف سطح دوره مرکز آموزش زبان خارجی'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class InstituteEnglishRegister(models.Model):
    """
    ثبت نام مرکز آموزش زبان خارجه
    """
    class Meta:
        verbose_name = 'H- ثبت نام مرکز آموزش زبان خارجه'
        verbose_name_plural = 'H- ثبت نام مرکز آموزش زبان خارجه'

    user                    = models.ForeignKey(User, on_delete=models.PROTECT)
    institue_english        = models.ForeignKey("InstituteEnglish", on_delete=models.PROTECT)
    city                    = models.ForeignKey("City", on_delete=models.PROTECT)
    district                = models.ForeignKey("District", on_delete=models.PROTECT)
    area                    = models.ForeignKey("Area", on_delete=models.PROTECT)
    permission_type         = models.IntegerField('نوع مجوز', default=1, choices=PermissionChoieces)
    sex                     = models.IntegerField('جنسیت', default=1, choices=SexChoieces)
    score                   = models.IntegerField('امتیاز کیفیت بخشی مرکز', blank = True)
    name_founder            = models.CharField('نام و نام خانوادگی موسس', max_length=255)
    name_manager            = models.CharField('نام و نام خانوادگی مدیر', max_length=255)
    bin_number              = models.CharField('شماره حساب مرکز', max_length=255)
    bank                    = models.CharField('نزد بانک', max_length=255)
    branch                  = models.CharField('شعبه', max_length=255)

    def __str__(self):
        return str(self.id)

class InstituteEnglishForm(models.Model):
    """
    فرم آموزش زبان خارجه
    """
    class Meta:
        verbose_name = 'I- فرم آموزش زبان خارجه'
        verbose_name_plural = 'I- فرم آموزش زبان خارجه'

    institute_english_define_term       = models.ForeignKey("InstituteEnglishDefineTerm", on_delete=models.PROTECT)
    institute_english_register          = models.ForeignKey("InstituteEnglishRegister", on_delete=models.CASCADE)
    education_content                   = models.CharField('محتوا آموزشی', max_length=255)
    session_number                      = models.IntegerField('تعداد جلسات',)
    max_student                         = models.IntegerField('حداکثر تعداد دانش آموز',)
    session_price                       = models.IntegerField('نرخ یک جلسه آموزشی',)
    nsession_price                      = models.IntegerField('نرخ یک دوره آموزشی بر اساس ان جلسه',)

    def __str__(self):
        return str(self.id)


class InstitueNonProfit(models.Model):
    """
    مرکز آموزشی علمی آزاد
    """
    class Meta:
        verbose_name = 'J- مرکز آموزشی علمی آزاد'
        verbose_name_plural = 'J- مرکز آموزشی علمی آزاد'

    name = models.CharField('نام', max_length=255, unique=True, )
    status = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)