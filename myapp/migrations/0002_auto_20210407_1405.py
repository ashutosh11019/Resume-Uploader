# Generated by Django 3.1.5 on 2021-04-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
