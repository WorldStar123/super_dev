# Generated by Django 3.1.5 on 2021-09-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_workerinvitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
    ]
