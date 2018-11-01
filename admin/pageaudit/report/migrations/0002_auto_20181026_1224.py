# Generated by Django 2.0 on 2018-10-26 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTimingMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('start_time', models.PositiveIntegerField(default=0)),
                ('lighthouse_run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_timing_measure_lighthouse_run', to='report.LighthouseRun')),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.CreateModel(
            name='UserTimingMeasureAverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('start_time', models.PositiveIntegerField(default=0)),
                ('number_samples', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserTimingMeasureName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='urlkpiaverage',
            name='redirect_hops',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usertimingmeasureaverage',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_timing_measure_avg_name', to='report.UserTimingMeasureName'),
        ),
        migrations.AddField(
            model_name='usertimingmeasureaverage',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_timing_measure_avg_url', to='report.Url'),
        ),
        migrations.AddField(
            model_name='usertimingmeasure',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_timing_measure_name', to='report.UserTimingMeasureName'),
        ),
        migrations.AddField(
            model_name='usertimingmeasure',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_timing_measure_url', to='report.Url'),
        ),
    ]
