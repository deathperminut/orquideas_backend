# Generated by Django 5.0.7 on 2024-08-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0011_activitymodule_co_create_aproximate_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmodule',
            name='color',
            field=models.CharField(max_length=100),
        ),
    ]
