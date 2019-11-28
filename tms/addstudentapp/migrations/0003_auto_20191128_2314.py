# Generated by Django 2.2.7 on 2019-11-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addstudentapp', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('Jun', 'Jun'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='year',
            field=models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year')], max_length=10),
        ),
    ]
