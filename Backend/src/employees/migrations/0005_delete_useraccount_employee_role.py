# Generated by Django 5.1.6 on 2025-02-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_remove_employee_user_account_remove_useraccount_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccount',
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee')], default='', max_length=10),
            preserve_default=False,
        ),
    ]
