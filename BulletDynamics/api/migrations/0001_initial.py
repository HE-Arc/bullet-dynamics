# Generated by Django 3.1.7 on 2021-04-16 20:04

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ammo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bullet_weight', models.DecimalField(decimal_places=3, max_digits=6)),
                ('cx', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cannon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('length', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('height', models.DecimalField(decimal_places=3, max_digits=6)),
                ('angle', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('length', models.DecimalField(decimal_places=3, max_digits=6)),
                ('standard_cannon_length', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InitSpeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_speed', models.DecimalField(decimal_places=3, max_digits=6)),
                ('ammo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ammo')),
                ('cannon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cannon')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('ammo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ammo')),
                ('cannon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cannon')),
                ('platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.platform')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='cannon',
            name='ammo',
            field=models.ManyToManyField(through='api.InitSpeed', to='api.Ammo'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('config', models.ManyToManyField(to='api.Config')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('param', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.param')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
