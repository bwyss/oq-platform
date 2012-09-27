# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'FaultSection.slip_type'
        db.alter_column('observations_faultsection', 'slip_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSection.contrib'
        db.alter_column('observations_faultsection', 'contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSection.compiler'
        db.alter_column('observations_faultsection', 'compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSource.slip_type'
        db.alter_column('observations_faultsource', 'slip_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSource.contrib'
        db.alter_column('observations_faultsource', 'contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'FaultSource.compiler'
        db.alter_column('observations_faultsource', 'compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Fault.slip_type'
        db.alter_column('observations_fault', 'slip_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Fault.contrib'
        db.alter_column('observations_fault', 'contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Fault.compiler'
        db.alter_column('observations_fault', 'compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))


    def backwards(self, orm):
        
        # Changing field 'FaultSection.slip_type'
        db.alter_column('observations_faultsection', 'slip_type', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'FaultSection.contrib'
        db.alter_column('observations_faultsection', 'contrib', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'FaultSection.compiler'
        db.alter_column('observations_faultsection', 'compiler', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'FaultSource.slip_type'
        db.alter_column('observations_faultsource', 'slip_type', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'FaultSource.contrib'
        db.alter_column('observations_faultsource', 'contrib', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'FaultSource.compiler'
        db.alter_column('observations_faultsource', 'compiler', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Fault.slip_type'
        db.alter_column('observations_fault', 'slip_type', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Fault.contrib'
        db.alter_column('observations_fault', 'contrib', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Fault.compiler'
        db.alter_column('observations_fault', 'compiler', self.gf('django.db.models.fields.CharField')(max_length=30))


    models = {
        'observations.displacement': {
            'Meta': {'object_name': 'Displacement'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'dis_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fault_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['observations.FaultSection']", 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'horizontal_displacement': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_displacement': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {}),
            'vertical_displacement': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.event': {
            'Meta': {'object_name': 'Event'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['observations.FaultSection']", 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'historical_earthquake': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'pre_historical_earthquake': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'observations.fault': {
            'Meta': {'object_name': 'Fault'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodic_behaviour': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'simple_geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultgeometry': {
            'Meta': {'object_name': 'FaultGeometry'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fault_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['observations.FaultSection']", 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'surface_dip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultsection': {
            'Meta': {'object_name': 'FaultSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodic_behaviour': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fault': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fault']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultsource': {
            'Meta': {'object_name': 'FaultSource'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fault': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['observations.Fault']"}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {'dim': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'source_nm': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.sliprate': {
            'Meta': {'object_name': 'SlipRate'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'dip_slip_rate_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dip_slip_rate_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dip_slip_rate_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fault_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['observations.FaultSection']", 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'hv_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_slip_rate_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'net_slip_rate_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'net_slip_rate_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'rake': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {}),
            'slip_rate_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slip_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'strike_slip_rate_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'strike_slip_rate_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'strike_slip_rate_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vertical_slip_rate_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vertical_slip_rate_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vertical_slip_rate_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.trace': {
            'Meta': {'object_name': 'Trace'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_meth': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['observations']
