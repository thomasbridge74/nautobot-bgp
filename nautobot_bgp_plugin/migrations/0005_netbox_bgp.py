# Generated by Django 3.1.3 on 2021-04-07 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_bgp_plugin', '0004_netbox_bgp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asn',
            options={'verbose_name_plural': 'AS Numbers'},
        ),
    ]
