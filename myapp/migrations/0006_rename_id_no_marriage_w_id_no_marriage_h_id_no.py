# Generated by Django 5.0.4 on 2024-06-26 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_idcard_blood_type_delete_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marriage',
            old_name='ID_No',
            new_name='W_ID_No',
        ),
        migrations.AddField(
            model_name='marriage',
            name='H_ID_No',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Husband_info', to='myapp.idcard'),
        ),
    ]
