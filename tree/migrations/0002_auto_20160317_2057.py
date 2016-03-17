# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='link',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='node',
            name='deleted',
        ),
        migrations.AddField(
            model_name='link',
            name='tags',
            field=models.ManyToManyField(related_name='links', to='tree.Tag'),
            preserve_default=True,
        ),
    ]
