# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'NewsSource'
        db.create_table('sources_newssource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('name_verbose', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('sel_stories', self.gf('django.db.models.fields.CharField')(default='item', max_length=255)),
            ('sel_title', self.gf('django.db.models.fields.CharField')(default='title', max_length=255)),
            ('sel_teaser', self.gf('django.db.models.fields.CharField')(default='description', max_length=255)),
            ('sel_link', self.gf('django.db.models.fields.CharField')(default='link', max_length=255)),
            ('sel_content', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sel_continuations', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('max_items', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('sources', ['NewsSource'])


    def backwards(self, orm):
        
        # Deleting model 'NewsSource'
        db.delete_table('sources_newssource')


    models = {
        'sources.newssource': {
            'Meta': {'object_name': 'NewsSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_items': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'name_verbose': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sel_content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sel_continuations': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sel_link': ('django.db.models.fields.CharField', [], {'default': "'link'", 'max_length': '255'}),
            'sel_stories': ('django.db.models.fields.CharField', [], {'default': "'item'", 'max_length': '255'}),
            'sel_teaser': ('django.db.models.fields.CharField', [], {'default': "'description'", 'max_length': '255'}),
            'sel_title': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['sources']
