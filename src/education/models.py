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
        verbose_name        = 'شهر'
        verbose_name_plural = 'A- شهر'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.name)

class District(models.Model):
    """
    منطقه
    """
    class Meta:
        verbose_name        = 'منطقه'
        verbose_name_plural = 'B- منطقه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    def __str__(self):
        return str(self.name)

class Area(models.Model):
    """
    ناحیه
    """
    class Meta:
        verbose_name        = 'ناحیه'
        verbose_name_plural = 'C- ناحیه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.name)


class StudyPeriod(models.Model):
    """
    دوره تحصیلی
    """
    class Meta:
        verbose_name        = 'دوره تحصیلی'
        verbose_name_plural = 'D- دوره تحصیلی'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.name)


class InstitueActivityType(models.Model):
    """
    نوع فعالیت موسسه
    """
    class Meta:
        verbose_name        = 'نوع فعالیت موسسه'
        verbose_name_plural = 'E- نوع فعالیت موسسه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.name)


class EnglishInstitute(models.Model):
    """
    مرکز آموزش زبان خارجه
    """
    class Meta:
        verbose_name        = 'مرکز آموزش زبان خارجه'
        verbose_name_plural = 'F- مرکز آموزش زبان خارجه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.name)


class EnglishInstituteDefineTerm(models.Model):
    """
    تعریف سطح دوره زبان خارجه
    """
    class Meta:
        verbose_name        = 'تعریف سطح دوره زبان خارجه'
        verbose_name_plural = 'G- تعریف سطح دوره زبان خارجه'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.name)


class EnglishInstituteRegister(models.Model):
    """
    فرم ثبت زبان خارجه
    """
    class Meta:
        verbose_name        = 'فرم ثبت زبان خارجه'
        verbose_name_plural = 'H- فرم ثبت زبان خارجه'

    user                    = models.ForeignKey(User, on_delete=models.PROTECT)
    english_institute       = models.ForeignKey("EnglishInstitute", on_delete=models.PROTECT)
    city                    = models.ForeignKey("City", on_delete=models.PROTECT)
    district                = models.ForeignKey("District", on_delete=models.PROTECT)
    area                    = models.ForeignKey("Area", on_delete=models.PROTECT)
    status                  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    send_status             = models.IntegerField('وضعیت ارسال', default=1, choices=SendStatus)
    type                    = models.IntegerField('نوع', default=3, choices=TypeChoieces)
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
        verbose_name_plural = 'I- فرم آموزش زبان خارجه'

    english_institute_define_term       = models.ForeignKey("EnglishInstituteDefineTerm", on_delete=models.PROTECT)
    english_institute_register          = models.ForeignKey("EnglishInstituteRegister", on_delete=models.CASCADE)
    education_content                   = models.CharField('محتوا آموزشی', max_length=255)
    session_number                      = models.IntegerField('تعداد جلسات',)
    max_student                         = models.IntegerField('حداکثر تعداد دانش آموز',)
    session_price                       = models.IntegerField('نرخ یک جلسه آموزشی',)
    nsession_price                      = models.IntegerField('نرخ یک دوره آموزشی بر اساس N جلسه',)

    def __str__(self):
        return str(self.id)


class NonprofitInstitue(models.Model):
    """
    مرکز آموزشی علمی آزاد
    """
    class Meta:
        verbose_name        = 'مرکز آموزشی علمی آزاد'
        verbose_name_plural = 'J- مرکز آموزشی علمی آزاد'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.name)


class NonprofitInstituteDefineTerm(models.Model):
    """
    تعریف سطح دوره علمی آزاد
    """
    class Meta:
        verbose_name        = 'تعریف سطح دوره علمی آزاد'
        verbose_name_plural = 'K- تعریف سطح دوره علمی آزاد'

    name    = models.CharField('نام', max_length=255, unique=True, )
    status  = models.IntegerField('وضعیت', default=1, choices=StatusChoices)

    def __str__(self):
        return str(self.name)


class NonprofitInstituteRegister(models.Model):
    """
    فرم ثبت مرکز علمی آزاد
    """
    class Meta:
        verbose_name        = 'فرم ثبت علمی آزاد'
        verbose_name_plural = 'L- فرم ثبت علمی آزاد'


    user                    = models.ForeignKey(User, on_delete=models.PROTECT)
    nonproft_institute      = models.ForeignKey("NonprofitInstitue", on_delete=models.PROTECT)
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



class NonprofitInstituteForm(models.Model):
    """
    فرم آموزش مرکز علمی آزاد
    """
    class Meta:
        verbose_name        = 'فرم آموزش علمی آزاد'
        verbose_name_plural = 'M- فرم آموزش علمی آزاد'

    nonprofit_institute_define_term         = models.ForeignKey("NonprofitInstituteDefineTerm", on_delete=models.PROTECT)
    nonprofit_institute_register            = models.ForeignKey("NonprofitInstituteRegister", on_delete=models.CASCADE)
    education_content                       = models.CharField('محتوا آموزشی', max_length=255)
    session_number                          = models.IntegerField('تعداد جلسات',)
    max_student                             = models.IntegerField('حداکثر تعداد دانش آموز',)
    max_hour                                = models.IntegerField('میزان کل ساعت دوره',)
    tuition                                 = models.IntegerField('شهریه مصوب دوره',)

    def __str__(self):
        return str(self.id)


class RejectedEnglishInstituteFormList(models.Model):
    """
    رد کردن فرم زبان خارجه
    """
    class Meta:
        verbose_name        = 'رد کردن فرم زبان خارجه'
        verbose_name_plural = 'N- رد کردن فرم زبان خارجه'

    english_institute_id         = models.ForeignKey(EnglishInstituteRegister, on_delete=models.CASCADE)
    user_id                      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title                        = models.CharField(max_length=500)
    reason                       = models.TextField(max_length=4000)
    time                         = models.TimeField(auto_now_add=True)
    status                       = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    create_date                  = models.IntegerField('تاریخ ثبت', default=apa_datetime.get_persian_date_normalized())

class RejectedNonprofitInstitueFormList(models.Model):
    """
    رد کردن فرم علمی آزاد
    """
    class Meta:
        verbose_name        = 'رد کردن فرم علمی آزاد'
        verbose_name_plural = 'O- رد کردن فرم علمی آزاد'

    nonprofit_institue_id        = models.ForeignKey(NonprofitInstituteRegister, on_delete=models.CASCADE)
    user_id                      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title                        = models.CharField(max_length=500)
    reason                       = models.TextField(max_length=4000)
    time                         = models.TimeField(auto_now_add=True)
    status                       = models.IntegerField('وضعیت', default=1, choices=StatusChoices)
    create_date                  = models.IntegerField('تاریخ ثبت', default=apa_datetime.get_persian_date_normalized())