# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'MemberMetadata.profile_quote'
        db.add_column('memberinfo_membermetadata', 'profile_quote', self.gf('django.db.models.fields.CharField')(default="Gotta catch 'em all", max_length=50, blank=True), keep_default=False)

        # Changing field 'MemberJoin.user'
        db.alter_column('memberinfo_memberjoin', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # Adding unique constraint on 'MemberJoin', fields ['user']
        db.create_unique('memberinfo_memberjoin', ['user_id'])


    def backwards(self, orm):
        
        # Deleting field 'MemberMetadata.profile_quote'
        db.delete_column('memberinfo_membermetadata', 'profile_quote')

        # Changing field 'MemberJoin.user'
        db.alter_column('memberinfo_memberjoin', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Removing unique constraint on 'MemberJoin', fields ['user']
        db.delete_unique('memberinfo_memberjoin', ['user_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'memberinfo.databaseaccount': {
            'Meta': {'object_name': 'DatabaseAccount'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'memberinfo.execplacement': {
            'Meta': {'object_name': 'ExecPlacement'},
            'end': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberinfo.ExecPosition']"}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'memberinfo.execposition': {
            'Meta': {'object_name': 'ExecPosition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'memberinfo.gamingids': {
            'Meta': {'object_name': 'GamingIDs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'psnID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'raptrID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'steamID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'xboxID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'xfireID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'memberinfo.mailinglist': {
            'Meta': {'object_name': 'MailingList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']"})
        },
        'memberinfo.member': {
            'Meta': {'object_name': 'Member'},
            'guest': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'showDetails': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'memberinfo.memberjoin': {
            'Meta': {'object_name': 'MemberJoin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'memberinfo.membermetadata': {
            'Meta': {'object_name': 'MemberMetadata'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_quote': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'memberinfo.nicknamedetails': {
            'Meta': {'object_name': 'NicknameDetails'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'memberinfo.quota': {
            'Meta': {'object_name': 'Quota'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'memberinfo.shellaccount': {
            'Meta': {'object_name': 'ShellAccount'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'memberinfo.term': {
            'Meta': {'object_name': 'Term'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_number': ('django.db.models.fields.IntegerField', [], {}),
            'which': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'memberinfo.websitedetails': {
            'Meta': {'object_name': 'WebsiteDetails'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'websiteTitle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'websiteUrl': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['memberinfo']
