# Generated by Django 4.0.3 on 2022-05-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruiser', '0004_alter_lesson_material_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_material',
            name='lesson_theme',
            field=models.CharField(max_length=122, verbose_name='Тема урока'),
        ),
    ]
