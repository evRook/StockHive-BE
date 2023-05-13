# Generated by Django 4.2.1 on 2023-05-13 13:55

import django.contrib.auth.base_user
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=10, null=True)),
                ('Name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField()),
                ('shortName', models.CharField()),
                ('longName', models.CharField()),
                ('address1', models.CharField()),
                ('city', models.CharField()),
                ('state', models.CharField()),
                ('country', models.CharField()),
                ('phone', models.CharField()),
                ('website', models.CharField()),
                ('sector', models.CharField()),
                ('longBuisnessSummary', models.TextField()),
                ('overallRisk', models.IntegerField()),
                ('open', models.IntegerField()),
                ('dayLow', models.IntegerField()),
                ('dayHigh', models.IntegerField()),
                ('regularMarketPreviousClose', models.IntegerField()),
                ('regularMarketOpen', models.IntegerField()),
                ('regularMarketDayLow', models.IntegerField()),
                ('regularMarketDayHigh', models.IntegerField()),
                ('marketCap', models.IntegerField()),
                ('fiftyTwoWeekHigh', models.IntegerField()),
                ('fiftyTwoWeekLow', models.IntegerField()),
                ('currency', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAcctManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, django.contrib.auth.base_user.BaseUserManager),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Open', models.IntegerField(null=True)),
                ('Close', models.IntegerField(null=True)),
                ('High', models.IntegerField(null=True)),
                ('Low', models.IntegerField(null=True)),
                ('Company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history', to='stocks.company')),
            ],
        ),
        migrations.CreateModel(
            name='UserAcct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first', models.CharField()),
                ('last', models.CharField()),
                ('user_name', models.CharField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
