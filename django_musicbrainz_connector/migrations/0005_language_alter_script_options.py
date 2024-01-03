# Generated by Django 5.0 on 2024-01-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_musicbrainz_connector", "0004_script"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                ("id", models.IntegerField(db_column="id", primary_key=True, serialize=False, verbose_name="ID")),
                ("iso_code_2t", models.CharField(db_column="iso_code_2t", max_length=3, verbose_name="ISO Code 2T")),
                ("iso_code_2b", models.CharField(db_column="iso_code_2b", max_length=3, verbose_name="ISO Code 2B")),
                ("iso_code_1", models.CharField(db_column="iso_code_1", max_length=2, verbose_name="ISO Code 1")),
                ("name", models.CharField(db_column="name", max_length=100, verbose_name="Name")),
                ("frequency", models.SmallIntegerField(db_column="frequency", default=0, verbose_name="Frequency")),
                ("iso_code_3", models.CharField(db_column="iso_code_3", max_length=3, verbose_name="ISO Code 3")),
            ],
            options={
                "verbose_name_plural": "Languages",
                "db_table": "language",
                "ordering": ["name"],
                "managed": False,
            },
        ),
        migrations.AlterModelOptions(
            name="script",
            options={"managed": False, "ordering": ["name"], "verbose_name_plural": "Scripts"},
        ),
    ]