from django.db import models
import datetime


def show_limited_char(data):
    return data[:20] + (data[20:] and '..')


class Agreement(models.Model):
    title_text = models.CharField(u'标题',max_length=100)
    desc_text = models.TextField(u'描述',max_length=1024,default='This is the default description')

    def __str__(self):
        return '协议: ' + self.title_text + ' / ' + show_limited_char(self.desc_text)

    class Meta:
        verbose_name = '协议'
        verbose_name_plural = '协议'


class Product(models.Model):
    title_text = models.CharField(u'标题',max_length=100)
    desc_text = models.TextField(u'描述', max_length=1024,default='This is the default description')

    def __str__(self):
        return '产品: ' + self.title_text + ' / '+ show_limited_char(self.desc_text)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'


class Activity(models.Model):
    title_text = models.CharField(u'活动名称',max_length=100)
    desc_text = models.TextField(u'活动详情',max_length=1024,
                                 default='This is the default description')
    start_date = models.DateField(u'开始日期', default=datetime.date.today,
                                  auto_now=False,
                                  auto_now_add=False,
                                  help_text="Please use the following format: <em>YYYY-MM-DD</em>."
                                  )
    end_date = models.DateField(u'结束日期', default=datetime.date.today,
                                auto_now=False,
                                auto_now_add=False,
                                help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    status = models.BooleanField(u'是否有效', default=True)
    fields_CHOICES = (
            (u'租用', '姓名|性别|电话|地址|学校|学号|产品|备注'),
            (u'会员', '姓名|性别|电话|学校|学号|备注')
    )
    fields_to_display = models.CharField(u'显示字段',max_length=12,
                                         choices=fields_CHOICES,
                                         default="租用")
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE,
                                  related_name='agreement',
                                  default=1,
                                  verbose_name='使用协议')
    products = models.ManyToManyField(Product, verbose_name='参与的产品')

    def __str__(self):
        return '活动: ' + self.title_text + ' / ' + show_limited_char(self.desc_text)

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = '活动'


class SignupInfo(models.Model):
    name = models.CharField(u'姓名', max_length=100)
    phoneNum = models.DecimalField(u'电话', max_digits=11, decimal_places=0)
    address = models.TextField(u'地址', max_length=1024,default='This is the default address')
    school = models.TextField(u'学校', max_length=1024,default='This is the default school')
    idNum = models.DecimalField(u'学号', max_digits=30, decimal_places=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product',
                                default=1, verbose_name='租琴型号')
    remark = models.TextField(u'备注', max_length=1024,blank=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    sex_CHOICES = (
        ('M', '男孩子'),
        ('F', '女孩子')
    )
    sex = models.CharField(u'性别', max_length=3,
                           choices=sex_CHOICES,
                           default="M")

    def __str__(self):
        return '报名: ' + self.activity.title_text + ' / ' + self.name + ' / '+ str(self.phoneNum)

    class Meta:
        verbose_name = '报名名单'
        verbose_name_plural = '报名名单'


