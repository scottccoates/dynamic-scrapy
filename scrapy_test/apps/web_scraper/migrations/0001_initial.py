# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):
  def forwards(self, orm):
    from django.core.management import call_command

    call_command("loaddata", "0001_initial.json")

  def backwards(self, orm):
    "Write your backwards methods here."

  models = {

  }

  complete_apps = ['web_scraper']
  symmetrical = True
