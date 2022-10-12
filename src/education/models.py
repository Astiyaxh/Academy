from email.policy import default
from random import choices
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

Registered = 1
Posted     = 2
Rejected   = 3
Accepted   = 4
SendStatus = (
    (Registered, "ثبت شده"),
    (Posted, "ارسال شده"),
    (Rejected, "رد شده"),
    (Accepted, "تایید شده"),
)

Institute                         = 1
ForeignLanguageTrainingCenter     = 2
NonProfitScientificTrainingCenter = 3
TypeChoieces = (
    (Institute, "آموزشگاه"),
    (ForeignLanguageTrainingCenter, "مرکز آموزشی آزاد علمی"),
    (NonProfitScientificTrainingCenter, "مرکز آموزشی زبان خارجی"),
)

class City(models.Model):
    """
    شهر
    """
    class Meta:
        verbose_name        = 'شهر'
        verbose_name_plural = 'شهر'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.id)

class District(models.Model):
    """
    منطقه
    """
    class Meta:
        verbose_name        = 'منطقه'
        verbose_name_plural = 'منطقه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.id)

class Area(models.Model):
    """
    ناحیه
    """
    class Meta:
        verbose_name        = 'ناحیه'
        verbose_name_plural = 'ناحیه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class EnglishInstitute(models.Model):
    """
    مرکز آموزش زبان خارجه
    """
    class Meta:
        verbose_name        = 'مرکز آموزش زبان خارجه'
        verbose_name_plural = 'مرکز آموزش زبان خارجه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class NonProfitInstitue(models.Model):
    """
    مرکز آموزشی علمی آزاد
    """
    class Meta:
        verbose_name        = 'مرکز آموزشی علمی آزاد'
        verbose_name_plural = 'مرکز آموزشی علمی آزاد'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)

class InstitueActivityType(models.Model):
    """
    نوع فعالیت موسسه
    """
    class Meta:
        verbose_name        = 'نوع فعالیت موسسه'
        verbose_name_plural = 'نوع فعالیت موسسه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)

class StudyPeriod(models.Model):
    """
    دوره تحصیلی
    """
    class Meta:
        verbose_name        = 'دوره تحصیلی'
        verbose_name_plural = 'دوره تحصیلی'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)

class EnglishInstituteDefineTerm(models.Model):
    """
    تعریف سطح دوره مرکز آموزش زبان خارجی
    """
    class Meta:
        verbose_name        = 'تعریف سطح دوره مرکز آموزش زبان خارجی'
        verbose_name_plural = 'تعریف سطح دوره مرکز آموزش زبان خارجی'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)

class EnglishInstituteRegister(models.Model):
    """
    ثبت نام مرکز آموزش زبان خارجه
    """
    class Meta:
        verbose_name        = 'ثبت نام مرکز آموزش زبان خارجه'
        verbose_name_plural = 'ثبت نام مرکز آموزش زبان خارجه'

    user                    = models.ForeignKey(User, on_delete=models.PROTECT)
    institue_english        = models.ForeignKey("EnglishInstitute", on_delete=models.PROTECT)
    city                    = models.ForeignKey("City", on_delete=models.PROTECT)
    district                = models.ForeignKey("District", on_delete=models.PROTECT)
    area                    = models.ForeignKey("Area", on_delete=models.PROTECT)
    status                  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    send_status             = models.IntegerField('وضعیت ارسال', default=1, choices=SendStatus)
    type                    = models.IntegerField('نوع', default=1, choices=TypeChoieces)
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

class EnglishInstituteForm(models.Model):
    """
    فرم آموزش زبان خارجه
    """
    class Meta:
        verbose_name        = 'فرم آموزش زبان خارجه'
        verbose_name_plural = 'فرم آموزش زبان خارجه'

    english_institute_define_term       = models.ForeignKey("EnglishInstituteDefineTerm", on_delete=models.PROTECT)
    english_institute_register          = models.ForeignKey("EnglishInstituteRegister", on_delete=models.CASCADE)
    education_content                   = models.CharField('محتوا آموزشی', max_length=255)
    session_number                      = models.IntegerField('تعداد جلسات',)
    max_student                         = models.IntegerField('حداکثر تعداد دانش آموز',)
    session_price                       = models.IntegerField('نرخ یک جلسه آموزشی',)
    nsession_price                      = models.IntegerField('نرخ یک دوره آموزشی بر اساس ان جلسه',)

    def __str__(self):
        return str(self.id)
