# Generated by Django 3.0.3 on 2020-03-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20200326_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complete',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='complete',
            name='date',
            field=models.TextField(blank=True, null=True),
        ),
    ]
