# Generated by Django 4.1.7 on 2023-02-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Наша история')),
            ],
            options={
                'verbose_name': ('О нас',),
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': ('Настройки',), 'verbose_name_plural': 'Настройки'},
        ),
    ]
