# Generated by Django 3.1.1 on 2020-09-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200917_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=255)),
            ],
        ),
    ]
