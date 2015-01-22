# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_num', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('zip_code', models.CharField(max_length=15, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('requirements', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('description', models.TextField(null=True)),
                ('donation_type', models.CharField(max_length=200, choices=[(b'Currency', b'Currency'), (b'Equipment', b'Equipment'), (b'Food', b'Food'), (b'Toys', b'Toys'), (b'Ink Cartridges', b'Ink Cartridges')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(null=True)),
                ('location', models.ForeignKey(to='main_site.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event_Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(to='main_site.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ssn', models.TextField(max_length=9, null=True)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.CharField(max_length=15)),
                ('drivers_lic', models.ImageField(null=True, upload_to=b'')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('individual_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main_site.Individual')),
                ('education', models.TextField(null=True)),
                ('job_exp', models.TextField(null=True, verbose_name=b'Job Experience')),
            ],
            options={
                'abstract': False,
            },
            bases=('main_site.individual',),
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('individual_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main_site.Individual')),
                ('interests', models.TextField(null=True)),
                ('education', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_site.individual',),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('individual_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main_site.Individual')),
                ('education', models.TextField(null=True)),
                ('job_exp', models.TextField(null=True, verbose_name=b'Job Experience')),
            ],
            options={
                'abstract': False,
            },
            bases=('main_site.individual',),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('Sponsor_type', models.CharField(max_length=200, choices=[(b'Personal', b'Personal'), (b'Company', b'Company')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('individual_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main_site.Individual')),
                ('job_exp', models.TextField(null=True, verbose_name=b'Job Experience')),
            ],
            options={
                'abstract': False,
            },
            bases=('main_site.individual',),
        ),
        migrations.AddField(
            model_name='individual',
            name='address',
            field=models.ForeignKey(to='main_site.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='individual',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_main_site.individual_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event_worker',
            name='individual',
            field=models.ForeignKey(to='main_site.Individual'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donation',
            name='sponsor',
            field=models.ForeignKey(to='main_site.Event'),
            preserve_default=True,
        ),
    ]
