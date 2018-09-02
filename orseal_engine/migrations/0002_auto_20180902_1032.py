# Generated by Django 2.1.1 on 2018-09-02 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orseal_engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolidaySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_id', models.CharField(max_length=200)),
                ('closed', models.BooleanField(blank=True, null=True)),
                ('opens_at', models.TextField(blank=True, null=True)),
                ('closes_at', models.TextField(blank=True, null=True)),
                ('start_date', models.TextField(blank=True, null=True)),
                ('end_date', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegularSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_id', models.CharField(max_length=200)),
                ('weekday', models.PositiveIntegerField(blank=True, null=True)),
                ('opens_at', models.TextField(blank=True, null=True)),
                ('closes_at', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='holidayscheduleaddress',
            name='project',
        ),
        migrations.RemoveField(
            model_name='regularscheduleaddress',
            name='project',
        ),
        migrations.RemoveField(
            model_name='program',
            name='description',
        ),
        migrations.AddField(
            model_name='accessibilityfordisabilities',
            name='accessibility',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accessibilityfordisabilities',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accessibilityfordisabilities',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='contact',
            name='department',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Organisation'),
        ),
        migrations.AddField(
            model_name='contact',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='contact',
            name='service_at_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.ServiceAtLocation'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eligibility',
            name='eligibility',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eligibility',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='funding',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Organisation'),
        ),
        migrations.AddField(
            model_name='funding',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='funding',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='language',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='language',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='location',
            name='alternate_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Organisation'),
        ),
        migrations.AddField(
            model_name='location',
            name='transportation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='alternate_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='legal_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='tax_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='tax_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='year_incorporated',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentaccepted',
            name='payment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentaccepted',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Contact'),
        ),
        migrations.AddField(
            model_name='phone',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='extension',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='language',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='phone',
            name='number',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Organisation'),
        ),
        migrations.AddField(
            model_name='phone',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='phone',
            name='service_at_location_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.ServiceAtLocation'),
        ),
        migrations.AddField(
            model_name='phone',
            name='type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='address_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='attention',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='postal_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='region',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicaladdress',
            name='state_province',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='address_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='attention',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='postal_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='region',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='state_province',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='alternate_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Organisation'),
        ),
        migrations.AddField(
            model_name='requireddocument',
            name='document',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requireddocument',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='service',
            name='accreditations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='alternate_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='application_process',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='fees',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='interpretation_services',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='licenses',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Program'),
        ),
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='wait_time',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='service_area',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serviceatlocation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serviceatlocation',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='serviceatlocation',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='servicetaxonomy',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='servicetaxonomy',
            name='taxonomy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Taxonomy'),
        ),
        migrations.AddField(
            model_name='servicetaxonomy',
            name='taxonomy_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Taxonomy'),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='vocabulary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='HolidayScheduleAddress',
        ),
        migrations.DeleteModel(
            name='RegularScheduleAddress',
        ),
        migrations.AddField(
            model_name='regularschedule',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='regularschedule',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Project'),
        ),
        migrations.AddField(
            model_name='regularschedule',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='regularschedule',
            name='service_at_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.ServiceAtLocation'),
        ),
        migrations.AddField(
            model_name='holidayschedule',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Location'),
        ),
        migrations.AddField(
            model_name='holidayschedule',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Project'),
        ),
        migrations.AddField(
            model_name='holidayschedule',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.Service'),
        ),
        migrations.AddField(
            model_name='holidayschedule',
            name='service_at_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orseal_engine.ServiceAtLocation'),
        ),
    ]
