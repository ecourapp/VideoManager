# Generated by Django 4.1.2 on 2023-03-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="video",
            options={"ordering": ["-date"]},
        ),
        migrations.AddField(
            model_name="video",
            name="date",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
