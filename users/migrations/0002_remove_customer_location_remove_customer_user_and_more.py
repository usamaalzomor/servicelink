# Generated by Django 4.2.1 on 2023-06-25 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employeeassistant',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='employeeassistant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='technician',
            name='user',
        ),
        migrations.AddField(
            model_name='technician',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='user_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='employeeassistant',
            name='user_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='technician',
            name='user_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
    ]