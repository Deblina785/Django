# Generated by Django 4.0.5 on 2022-06-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
            ],
        ),
    ]