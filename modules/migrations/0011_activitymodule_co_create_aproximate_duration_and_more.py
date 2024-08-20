# Generated by Django 5.0.7 on 2024-08-11 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modules", "0010_useractivitymodule_co_create_aproximate_duration_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="activitymodule",
            name="co_create_aproximate_duration",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="activitymodule",
            name="engage_aproximate_duration",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="activitymodule",
            name="foundations_aproximate_duration",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="activitymodule",
            name="reflection_aproximate_duration",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="surveymodule",
            name="survey_aproximate_duration",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="usersurveymodule",
            name="survey_aproximate_duration",
            field=models.IntegerField(default=0),
        ),
    ]