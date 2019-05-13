# Generated by Django 2.2.1 on 2019-05-13 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('flexible_plans', '0006_feature_polymorphic_ctype'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionFeature',
            fields=[
                ('feature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.FLEXIBLE_PLANS_FEATURE_MODEL)),
                ('group', models.ManyToManyField(blank=True, null=True, to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
            bases=('flexible_plans.feature',),
        ),
    ]
