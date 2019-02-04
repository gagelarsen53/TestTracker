# Generated by Django 2.1.5 on 2019-02-04 21:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_tracker', '0006_teststatus_text_hex_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('version', models.CharField(max_length=16)),
                ('notes', models.TextField(blank=True, max_length=256, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('source', models.CharField(max_length=64)),
                ('summary', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('needs_review', models.BooleanField(default=True)),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_tracker.TestCategory')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_tracker.Product')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_tracker.TestSubcategory')),
            ],
            options={
                'verbose_name': 'Test Case',
                'verbose_name_plural': 'Test Cases',
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('note', models.TextField(max_length=256)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_tracker.TestStatus')),
                ('testcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_tracker.TestCase')),
            ],
            options={
                'verbose_name': 'Test Result',
                'verbose_name_plural': 'Test Results',
            },
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'version')},
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together={('product', 'name')},
        ),
    ]