# Generated by Django 4.0.2 on 2022-03-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_hrana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zherler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
