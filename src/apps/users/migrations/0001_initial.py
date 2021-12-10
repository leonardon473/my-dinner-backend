# Generated by Django 3.2 on 2021-12-10 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("client_id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=120, unique=True)),
                ("full_name", models.CharField(max_length=120)),
                ("mobile_number", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
            },
        ),
        migrations.CreateModel(
            name="ClientAddress",
            fields=[
                (
                    "client_address_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("street", models.CharField(max_length=50)),
                ("num_ext", models.CharField(max_length=50)),
                ("num_int", models.CharField(blank=True, max_length=50)),
                ("neighborhood", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=5)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.client"
                    ),
                ),
            ],
            options={
                "verbose_name": "Client Address",
                "verbose_name_plural": "Client Addresses",
            },
        ),
    ]
