# Generated by Django 4.1.3 on 2022-11-04 09:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todos",
            fields=[
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=500)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
