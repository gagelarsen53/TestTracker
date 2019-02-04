# Generated by Django 2.1.5 on 2019-02-04 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0002_testcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=32)),
                ('description', models.CharField(default='No description provided...', max_length=64)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_tracker.TestCategory')),
            ],
            options={
                'verbose_name': 'Test Subcategory',
            },
        ),
        migrations.AlterUniqueTogether(
            name='testsubcategory',
            unique_together={('category', 'subcategory')},
        ),
    ]
