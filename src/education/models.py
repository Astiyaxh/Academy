from django.db import models
from user.models import User
from APA_module import apa_datetime
import datetime

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
        verbose_name        = 'A- شهر'
        verbose_name_plural = 'A- شهر'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.id)

class District(models.Model):
    """
    منطقه
    """
    class Meta:
        verbose_name        = 'B- منطقه'
        verbose_name_plural = 'B- منطقه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.id)

class Area(models.Model):
    """
    ناحیه
    """
    class Meta:
        verbose_name        = 'C- ناحیه'
        verbose_name_plural = 'C- ناحیه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)

class InstitueActivityType(models.Model):
    """
    نوع فعالیت موسسه
    """
    class Meta:
        verbose_name        = 'D- نوع فعالیت موسسه'
        verbose_name_plural = 'D- نوع فعالیت موسسه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class StudyPeriod(models.Model):
    """
    دوره تحصیلی
    """
    class Meta:
        verbose_name        = 'E- دوره تحصیلی'
        verbose_name_plural = 'E- دوره تحصیلی'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class InstituteEnglish(models.Model):
    """
    مرکز آموزش زبان خارجه
    """
    class Meta:
        verbose_name        = 'F- مرکز آموزش زبان خارجه'
        verbose_name_plural = 'F- مرکز آموزش زبان خارجه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class InstituteEnglishDefineTerm(models.Model):
    """
    تعریف سطح دوره مرکز آموزش زبان خارجی
    """
    class Meta:
        verbose_name        = 'G- تعریف سطح دوره مرکز آموزش زبان خارجی'
        verbose_name_plural = 'G- تعریف سطح دوره مرکز آموزش زبان خارجی'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.id)


class InstituteEnglishRegister(models.Model):
    """
    ثبت نام مرکز آموزش زبان خارجه
    """
    class Meta:
        verbose_name        = 'H- ثبت نام مرکز آموزش زبان خارجه'
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
    nsession_price                      = models.IntegerField('نرخ یک دوره آموزشی بر اساس N جلسه',)

    def __str__(self):
        return str(self.id)


class NoneProfitForm(models.Model):
    """
    فرم ثبت مرکز آموزشی علمی آزاد
    """
    class Meta:
        verbose_name        = 'فرم ثبت مرکز آموزشی علمی آزاد'
        verbose_name_plural = 'فرم ثبت مرکز آموزشی علمی آزاد'


    user                    = models.ForeignKey(User, on_delete=models.PROTECT)
    non_proft_institute     = models.ForeignKey("NonProfitInstitue", on_delete=models.PROTECT)
    city                    = models.ForeignKey("City", on_delete=models.PROTECT)
    district                = models.ForeignKey("District", on_delete=models.PROTECT)
    area                    = models.ForeignKey("Area", on_delete=models.PROTECT)
    status                  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    send_status             = models.IntegerField('وضعیت ارسال', default=1, choices=SendStatus)
    type                    = models.IntegerField('نوع', default=2, choices=TypeChoieces)
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



class NoneProfitFormTable(models.Model):
    """
    جدول ثبت مرکز علمی آزاد
    """
    class Meta:
        verbose_name        = 'جدول ثبت مرکز علمی آزاد'
        verbose_name_plural = 'جدول ثبت مرکز علمی آزاد'

    non_profit_institute_define_term        = models.ForeignKey("NonProfitInstituteDefineTerm", on_delete=models.PROTECT)
    none_profit_form                        = models.ForeignKey("NoneProfitForm", on_delete=models.CASCADE)
    education_content                       = models.CharField('محتوا آموزشی', max_length=255)
    session_number                          = models.IntegerField('تعداد جلسات',)
    max_student                             = models.IntegerField('حداکثر تعداد دانش آموز',)
    max_hour                                = models.IntegerField('میزان کل ساعت دوره',)
    tuition                                 = models.IntegerField('شهریه مصوب دوره',)

    def __str__(self):
        return str(self.id)


class rejected_english_institute_form_list(models.Model):
    """
    رد کردن فرم زبان خارجه
    """
    class Meta:
        verbose_name        = 'رد کردن فرم زبان خارجه'
        verbose_name_plural = 'رد کردن فرم زبان خارجه'

    english_institute_id         = models.ForeignKey(EnglishInstituteRegister, on_delete=models.CASCADE)
    user_id                      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title                        = models.CharField(max_length=500)
    reason                       = models.TextField(max_length=4000)
    time                         = models.TimeField(auto_now_add=True)
    status                       = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    create_date                  = models.IntegerField('تاریخ ثبت', default=apa_datetime.get_persian_date_normalized())

class rejected_nonprofit_institue_form_list(models.Model):
    """
    رد کردن فرم علمی آزاد
    """
    class Meta:
        verbose_name        = 'رد کردن فرم علمی آزاد'
        verbose_name_plural = 'رد کردن فرم علمی آزاد'

    nonprofit_institue_id        = models.ForeignKey(NoneProfitForm, on_delete=models.CASCADE)
    user_id                      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title                        = models.CharField(max_length=500)
    reason                       = models.TextField(max_length=4000)
    time                         = models.TimeField(auto_now_add=True)
    status                       = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    create_date                  = models.IntegerField('تاریخ ثبت', default=apa_datetime.get_persian_date_normalized())
