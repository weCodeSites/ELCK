# Generated by Django 4.2.3 on 2023-07-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_events_decription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='decription',
            field=models.CharField(max_length=60),
        ),
    ]
