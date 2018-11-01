# Generated by Django 2.0 on 2018-10-26 16:22

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('banner_text', models.CharField(max_length=255)),
                ('banner_type', models.CharField(choices=[('info', 'info'), ('warn', 'warn'), ('alert', 'alert')], default='info', max_length=20)),
            ],
            options={
                'ordering': ['active', 'name'],
            },
        ),
        migrations.CreateModel(
            name='LighthouseDataRaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('report_data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'verbose_name_plural': 'Lighthouse data raw',
            },
        ),
        migrations.CreateModel(
            name='LighthouseDataUsertiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('report_data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='LighthouseRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('invalid_run', models.BooleanField(default=False)),
                ('http_error_code', models.PositiveIntegerField(blank=True, null=True)),
                ('lighthouse_error_code', models.CharField(blank=True, max_length=255, null=True)),
                ('lighthouse_error_msg', models.TextField(blank=True, null=True)),
                ('accessibility_score', models.PositiveIntegerField(default=0)),
                ('dom_content_loaded', models.PositiveIntegerField(default=0)),
                ('first_contentful_paint', models.PositiveIntegerField(default=0)),
                ('first_meaningful_paint', models.PositiveIntegerField(default=0)),
                ('interactive', models.PositiveIntegerField(default=0)),
                ('dom_loaded', models.PositiveIntegerField(default=0)),
                ('masthead_onscreen', models.PositiveIntegerField(default=0)),
                ('number_network_requests', models.PositiveIntegerField(default=0)),
                ('performance_score', models.PositiveIntegerField(default=0)),
                ('redirect_hops', models.PositiveIntegerField(default=0)),
                ('redirect_wasted_ms', models.PositiveIntegerField(default=0)),
                ('seo_score', models.PositiveIntegerField(default=0)),
                ('thumbnail_image', models.TextField(blank=True, null=True)),
                ('time_to_first_byte', models.PositiveIntegerField(default=0)),
                ('total_byte_weight', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=2000, unique=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-view_count'],
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(unique=True)),
                ('inactive', models.BooleanField(default=False)),
                ('sequence', models.PositiveIntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='url_created_by', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='url_edited_by', to=settings.AUTH_USER_MODEL)),
                ('lighthouse_run', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='url_lighthouse_run', to='report.LighthouseRun')),
            ],
            options={
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='UrlKpiAverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('number_samples', models.PositiveIntegerField(default=0)),
                ('invalid_average', models.BooleanField(default=False)),
                ('accessibility_score', models.PositiveIntegerField(default=0)),
                ('dom_content_loaded', models.PositiveIntegerField(default=0)),
                ('first_contentful_paint', models.PositiveIntegerField(default=0)),
                ('first_meaningful_paint', models.PositiveIntegerField(default=0)),
                ('interactive', models.PositiveIntegerField(default=0)),
                ('dom_loaded', models.PositiveIntegerField(default=0)),
                ('masthead_onscreen', models.PositiveIntegerField(default=0)),
                ('number_network_requests', models.PositiveIntegerField(default=0)),
                ('performance_score', models.PositiveIntegerField(default=0)),
                ('redirect_wasted_ms', models.PositiveIntegerField(default=0)),
                ('seo_score', models.PositiveIntegerField(default=0)),
                ('time_to_first_byte', models.PositiveIntegerField(default=0)),
                ('total_byte_weight', models.PositiveIntegerField(default=0)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url_kpi_average_url', to='report.Url')),
            ],
        ),
        migrations.AddField(
            model_name='url',
            name='url_kpi_average',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='url_url_kpi_average', to='report.UrlKpiAverage'),
        ),
        migrations.AddField(
            model_name='lighthouserun',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lighthouse_run_url', to='report.Url'),
        ),
        migrations.AddField(
            model_name='lighthousedatausertiming',
            name='lighthouse_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lighthouse_data_usertiming_lighthouse_run', to='report.LighthouseRun'),
        ),
        migrations.AddField(
            model_name='lighthousedataraw',
            name='lighthouse_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lighthouse_data_raw_lighthouse_run', to='report.LighthouseRun'),
        ),
    ]
