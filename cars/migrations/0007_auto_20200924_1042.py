# Generated by Django 3.1.1 on 2020-09-24 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20200924_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='cartypes',
            new_name='types',
        ),
    ]
