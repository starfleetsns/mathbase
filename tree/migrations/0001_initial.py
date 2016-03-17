# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=500)),
                ('added', models.DateField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('text', models.TextField()),
                ('deleted', models.BooleanField(default=False, editable=False)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='tree.Node', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='link',
            name='nodes',
            field=models.ManyToManyField(related_name='links', to='tree.Node'),
            preserve_default=True,
        ),
    ]
