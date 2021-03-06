# Generated by Django 3.0.4 on 2020-03-18 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Bills', 'Bills'), ('Food_Drinks', 'Food_Drinks'), ('Gas', 'Gas'), ('Personal_Expense', 'Personal_Expense')], default='Personal_Expense', max_length=50)),
                ('date_pushed', models.DateTimeField(default=django.utils.timezone.now)),
                ('maxAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxSpendAmount', models.IntegerField()),
                ('bills', models.IntegerField()),
                ('food_drink', models.IntegerField()),
                ('gas', models.IntegerField()),
                ('personal_expense', models.IntegerField()),
            ],
        ),
    ]
