# Generated by Django 5.1 on 2024-08-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=15)),
                ('mot_de_passe', models.CharField(max_length=30)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
