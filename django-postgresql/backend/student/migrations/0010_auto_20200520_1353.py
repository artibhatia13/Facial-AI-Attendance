# Generated by Django 3.0.5 on 2020-05-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_student_total_class_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subj1',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='subj2',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='subj3',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
