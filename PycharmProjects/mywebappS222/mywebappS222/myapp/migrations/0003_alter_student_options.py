# Generated by Django 4.0.6 on 2022-07-31 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('canSeeMyAccount', 'Can see the my account page')]},
        ),
    ]
