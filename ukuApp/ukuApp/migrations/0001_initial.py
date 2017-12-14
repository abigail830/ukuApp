# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 13:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100, verbose_name='Activity Title')),
                ('desc_text', models.TextField(default='This is the default description', max_length=1024, verbose_name='Description')),
                ('start_date', models.DateField(default=datetime.date.today, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='Start Date')),
                ('end_date', models.DateField(default=datetime.date.today, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='End Date')),
                ('status', models.BooleanField(default=True, verbose_name='Active?')),
                ('fields_to_display', models.CharField(choices=[('Rental', (('name', 'Name'), ('phoneNum', 'Phone Number'), ('address', 'Address'), ('school', 'School'), ('idNum', 'Student ID'), ('product', 'Ukulele you plan to rent'))), ('Membership', (('name', 'Name'), ('phoneNum', 'Phone Number'), ('remark', 'Remark'))), ('unknown', 'Unknown')], default='Membership', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySignupMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='ukuApp.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100)),
                ('desc_text', models.TextField(default='This is the default description', max_length=1024, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100)),
                ('desc_text', models.TextField(default='This is the default description', max_length=1024, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ProductActivityMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ukuApp.Activity')),
                ('products', models.ManyToManyField(related_name='_productactivitymapping_products_+', to='ukuApp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SignupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phoneNum', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='Phone Number')),
                ('address', models.TextField(default='This is the default address', max_length=1024, verbose_name='Address')),
                ('school', models.TextField(default='This is the default school', max_length=1024, verbose_name='School Name')),
                ('idNum', models.DecimalField(decimal_places=0, max_digits=30, verbose_name='ID Number')),
                ('remark', models.TextField(blank=True, max_length=1024, verbose_name='Remarks')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ukuApp.Product')),
            ],
        ),
        migrations.AddField(
            model_name='activitysignupmapping',
            name='signup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='signup', to='ukuApp.SignupInfo'),
        ),
        migrations.AddField(
            model_name='activity',
            name='agreement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ukuApp.Agreement'),
        ),
    ]
