# Generated by Django 3.0.3 on 2020-03-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_auto_20200326_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complete',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]