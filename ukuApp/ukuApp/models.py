from django.db import models
import datetime


class Agreement(models.Model):
    title_text = models.CharField(u'标题',max_length=100)
    desc_text = models.TextField(u'描述',max_length=1024,default='This is the default description')

    def __str__(self):
        return '协议: ' + self.title_text + ' / '+self.desc_text

    class Meta:
        verbose_name = '协议'
        verbose_name_plural = '协议'


class Product(models.Model):
    title_text = models.CharField(u'标题',max_length=100)
    desc_text = models.TextField(u'描述', max_length=1024,default='This is the default description')

    def __str__(self):
        return '产品: ' + self.title_text + ' / '+self.desc_text

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'


class SignupInfo(models.Model):
    name = models.CharField('Name', max_length=100)
    phoneNum = models.DecimalField('Phone Number', max_digits=11, decimal_places=0)
    address = models.TextField('Address', max_length=1024,default='This is the default address')
    school = models.TextField('School Name', max_length=1024,default='This is the default school')
    idNum = models.DecimalField('ID Number', max_digits=30, decimal_places=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='+',
                                default=1)
    remark = models.TextField('Remarks', max_length=1024,blank=True)
    fields_CHOICES = (
            ('rental', 'name|phoneNum|address|school|idNum|product'),
            ('member', 'name|phoneNum|remark')
    )
    class Meta:
        verbose_name = '报名'
        verbose_name_plural = '报名'


class Activity(models.Model):
    title_text = models.CharField('Activity Title',max_length=100)
    desc_text = models.TextField('Description',max_length=1024,
                                 default='This is the default description')
    start_date = models.DateField('Start Date', default=datetime.date.today,
                                  auto_now=False,
                                  auto_now_add=False,
                                  help_text="Please use the following format: <em>YYYY-MM-DD</em>."
                                  )
    end_date = models.DateField('End Date', default=datetime.date.today,
                                auto_now=False,
                                auto_now_add=False,
                                help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    status = models.BooleanField('Active?', default=True)
    agreement = models.ForeignKey(Agreement,on_delete=models.CASCADE,
                                  related_name='+',
                                  default=1)
    fields_to_display = models.CharField(max_length=12,
                                         choices=SignupInfo.fields_CHOICES,
                                         default="Membership")

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = '活动'


class ActivitySignupMapping(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,
                                 related_name='activity',
                                 default=1)
    signup = models.ForeignKey(SignupInfo, on_delete=models.CASCADE,
                               related_name='signup',
                               default=1)

class ProductActivityMapping(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,
                                 related_name='+',
                                 default=1)
    products = models.ManyToManyField(Product,
                                      related_name='+',)


