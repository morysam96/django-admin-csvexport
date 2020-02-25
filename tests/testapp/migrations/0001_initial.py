# Generated by Django 2.2.10 on 2020-02-24 21:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.CharField(default='ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ', max_length=255)),
                ('two', models.CharField(default='ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ModelC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.CharField(default='ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ', max_length=255)),
                ('two', models.CharField(default='ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean_field', models.BooleanField(default=True)),
                ('char_field', models.CharField(default='ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ', max_length=255)),
                ('date_field', models.DateField(auto_now=True)),
                ('duration_field', models.DurationField()),
                ('float_field', models.FloatField(default=1.234)),
                ('integer_field', models.IntegerField(default=1234)),
                ('text_field', models.TextField(default='ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ')),
                ('time_field', models.TimeField(auto_now=True)),
                ('binary_field', models.BinaryField(default=b'abcde', max_length=255)),
                ('uuid_field', models.UUIDField(default=uuid.uuid4)),
                ('generic_ip_address_field', models.GenericIPAddressField(default='1.2.3.4')),
                ('model_b', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testapp.ModelB')),
                ('model_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.ModelC')),
            ],
        ),
    ]