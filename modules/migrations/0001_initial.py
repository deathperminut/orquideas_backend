# Generated by Django 5.0.7 on 2024-08-11 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ActivityName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="ChoiceQuestionary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("choice_text", models.CharField(max_length=500)),
                ("is_correct", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Evidence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                (
                    "upload",
                    models.FileField(blank=True, null=True, upload_to="evidence/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FormatText",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ForumParticipation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("response", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Lecture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField(blank=True)),
                ("link", models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OpenQuestionary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("response", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="OpenQuestionaryOptional",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("response", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Redaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("text", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SatisfactionQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("survey", models.TextField(blank=True, null=True)),
                (
                    "level_of_satisfaction",
                    models.IntegerField(
                        choices=[
                            (1, "Very Dissatisfied"),
                            (2, "Dissatisfied"),
                            (3, "Neutral"),
                            (4, "Satisfied"),
                            (5, "Very Satisfied"),
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SkillAndLearning",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SpecificObjective",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="UserSurveyModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("video_link", models.URLField(blank=True, max_length=300, null=True)),
                (
                    "video_file",
                    models.FileField(blank=True, null=True, upload_to="videos/"),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="SelectionMultipleQuestionary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question_text", models.CharField(max_length=500)),
                ("choices", models.ManyToManyField(to="modules.choicequestionary")),
            ],
        ),
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "activity_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.activityname",
                    ),
                ),
                (
                    "evidence",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.evidence",
                    ),
                ),
                (
                    "format_text",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.formattext",
                    ),
                ),
                (
                    "forum_participation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.forumparticipation",
                    ),
                ),
                (
                    "lecture",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.lecture",
                    ),
                ),
                (
                    "open_questionary",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.openquestionary",
                    ),
                ),
                (
                    "open_questionary_optional",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.openquestionaryoptional",
                    ),
                ),
                (
                    "redaction",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.redaction",
                    ),
                ),
                (
                    "satisfaction_question",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.satisfactionquestion",
                    ),
                ),
                (
                    "selection_multiple_questionary",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.selectionmultiplequestionary",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SurveyModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "survey",
                    models.ManyToManyField(
                        blank=True,
                        related_name="master_survey_modules",
                        to="modules.activity",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TrainingModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("module_name", models.CharField(max_length=200)),
                ("tag_line", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("color", models.CharField(max_length=30)),
                ("color_name", models.CharField(max_length=32)),
                (
                    "document",
                    models.FileField(blank=True, null=True, upload_to="modules/"),
                ),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("general_objective", models.TextField(blank=True)),
                (
                    "skills_and_learnings",
                    models.ManyToManyField(blank=True, to="modules.skillandlearning"),
                ),
                (
                    "specific_objectives",
                    models.ManyToManyField(blank=True, to="modules.specificobjective"),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="ActivityModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "co_create",
                    models.ManyToManyField(
                        blank=True,
                        related_name="master_co_create_modules",
                        to="modules.activity",
                    ),
                ),
                (
                    "engage",
                    models.ManyToManyField(
                        blank=True,
                        related_name="master_engage_modules",
                        to="modules.activity",
                    ),
                ),
                (
                    "foundations",
                    models.ManyToManyField(
                        blank=True,
                        related_name="master_foundation_modules",
                        to="modules.activity",
                    ),
                ),
                (
                    "reflection",
                    models.ManyToManyField(
                        blank=True,
                        related_name="master_reflection_modules",
                        to="modules.activity",
                    ),
                ),
                (
                    "training_module",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modules.trainingmodule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserActivityModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "co_create",
                    models.ManyToManyField(
                        blank=True,
                        related_name="co_create_modules",
                        to="modules.activity",
                    ),
                ),
                (
                    "engage",
                    models.ManyToManyField(
                        blank=True, related_name="engage_modules", to="modules.activity"
                    ),
                ),
                (
                    "foundations",
                    models.ManyToManyField(
                        blank=True,
                        related_name="foundation_modules",
                        to="modules.activity",
                    ),
                ),
                (
                    "reflection",
                    models.ManyToManyField(
                        blank=True,
                        related_name="reflection_modules",
                        to="modules.activity",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "activity_module_editable",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_modules",
                        to="modules.useractivitymodule",
                    ),
                ),
                (
                    "activity_module_master",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_modules_master",
                        to="modules.activitymodule",
                    ),
                ),
            ],
        ),
    ]
