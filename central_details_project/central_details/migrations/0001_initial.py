# Generated by Django 4.1.7 on 2023-03-20 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('dept_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(default='Aruba', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('emp_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_salary', models.IntegerField()),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_id', to='central_details.department')),
            ],
        ),
    ]
