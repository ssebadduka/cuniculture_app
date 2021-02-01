# Generated by Django 2.2.1 on 2021-01-01 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuniculture_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribution',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='livestock',
        ),
        migrations.RemoveField(
            model_name='farmstock',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='farmstock',
            name='livestock',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='livestock',
        ),
        migrations.RemoveField(
            model_name='livestock',
            name='gender',
        ),
        migrations.AddField(
            model_name='livestock',
            name='farm',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cuniculture_app.Farm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livestock',
            name='female',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livestock',
            name='male',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livestock',
            name='maturity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livestock',
            name='maturity_period',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livestock',
            name='status',
            field=models.CharField(choices=[('Birth', 'Birth'), ('Stock', 'Stock')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Births',
        ),
        migrations.DeleteModel(
            name='Distribution',
        ),
        migrations.DeleteModel(
            name='FarmStock',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
