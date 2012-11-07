/*
 Copyright (c) 2010-2012, GEM Foundation.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/agpl.html>. */

/**
 *
 * @require faulted_earth/models.js
 *
 */


Ext.namespace('faulted_earth.utils');

/**
 * Overrides the startEditing method of FeatureEditPopup to provide
 * client side validation
 */

origStartEditing = gxp.FeatureEditPopup.prototype.startEditing;
Ext.override(gxp.FeatureEditPopup, {
    startEditing: function() {
	origStartEditing.apply(this, arguments);
	this.addValidator();
    },
    
    addValidator: function() {
	if (this.hasValidator) {
	    return;
	} else {
	    this.hasValidator = true;
	}
	var grid = this.items.first();

	/* for each field in the grid we hijack the
	 * standard validation mechanism */
	Ext.iterate(grid.customEditors, function(fieldName) {
	    var gridEditor = this[fieldName];
	    var field = gridEditor.field;
	      
	    /* for compulsory field management. Do not
	     * allow an user to leave a compulsory field
	     * blank */
	    if (faulted_earth.isCompulsory(fieldName)) {
		field.allowBlank = false;
	    }
	    
	    // hack field.getErrors
	    var old_getErrors = field.getErrors;
	    field.getErrors = function(value) {
		var errors = old_getErrors.apply(field, [value]) || [];
		
		// CUSTOM VALIDATION
		// FIXME validator code should go into models
		switch(fieldName) {
		case 'fault_section_id':
		    if (! value) {
			break;
		    }
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkPositive(fieldName, value));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkInteger(fieldName, value));
		    
		    value = parseInt(value);

		    /* this store can be null if the fault section
		     * grid has not been yet activated. Please fix me
		     * once you know how to create a featuresttore
		     * bypassing the featuremanager complexity */
		    var store = app.tools.faultsection_manager.featureStore;
		    if (store) {
			var search = store.findBy(function(item) { 
			    return item.get('fid') == 'fault_section.' + value});
			if (search == -1) {
			    errors.push("Invalid fault section id");
			}
		    } else {
			alert("before editing the fault_section_id please activate the fault section tab to load the data");
		    }
		    break;

		case 'rake_min':
		case 'rake_max':
		case 'rake_pref':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkInterval(grid, fieldName, value));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkBetween(fieldName, value, -180, 180));
		    break;
		case 'marker_age':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkPositive(fieldName, value));
		    break;
		case 'low_d_min':
		case 'low_d_max':
		case 'low_d_pref':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkWidthRule(fieldName, grid));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkInterval(grid, fieldName, value));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkPositive(fieldName, value));
		    var upper_seismogenic_min_value = grid.getCurrentValue('u_sm_d_min', parseFloat);
		    value = parseFloat(value);
		    if (upper_seismogenic_min_value && value < upper_seismogenic_min_value) {
			errors.push("Lower Seismogenic minimum value has to be greater than the upper seismogenic minimum value");
		    }
		    break;

		case 'episodic_behaviour':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkValueIn(fieldName, value, ["Yes Active", "Yes Inactive", "No"]));
		    break;

		case 'u_sm_d_min':
		case 'u_sm_d_max':
		case 'u_sm_d_pref':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkWidthRule(fieldName, grid));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkInterval(grid, fieldName, value));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkPositive(fieldName, value));
		    var lower_seismogenic_min_value = grid.getCurrentValue('low_d_min', parseFloat);
		    value = parseFloat(value);
		    if (lower_seismogenic_min_value && value > lower_seismogenic_min_value) {
			errors.push("Lower Seismogenic minimum value has to be greater than the upper seismogenic minimum value");
		    }
		    break;
		case 'rake_com':
		case 'aseis_com':
		case 'net_slip_rate_com':
		case 'slip_com':
		case 'dip_com':
		case 're_int_com':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkCompleteness(fieldName, value));
		    break;
		case 'length':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkPositive(fieldName, value));
		    break;
		case 'mag_min':
		case 'mag_max':
		case 'mag_pref':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkInterval(grid, fieldName, value));
		    break;
		    
		case 'dip_min':
		case 'dip_max':
		case 'dip_pref':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkWidthRule(fieldName, grid));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkInterval(grid, fieldName, value));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkQuadrant(fieldName, value));
		    break;
		case 'dip_dir':
		    var strike_value = grid.getCurrentValue('strike', parseFloat);
		    value = parseFloat(value);
		    if (strike_value && value != ((strike_value + 90) % 360) ) {
			errors.push("Dip direction has to be equal to the strike plus 90 degrees");
		    }
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkAngle(fieldName, value));
		    break;
		case 'strike':
		    var dip_dir = grid.getCurrentValue('dip_dir', parseFloat);
		    value = parseFloat(value);
		    if (dip_dir && dip_dir != ((value + 90) % 360) ) {
			errors.push("Strike has to be equal to the dip direction minus 90 degrees");
		    }
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkAngle(fieldName, value));
		    break;
		case 'down_thro':
		    var choices = ['N', 'S', 'W', 'E', 'NW', 'NE', 'SW', 'SE'];
		    if (choices.indexOf(value) == -1) {
			errors.push("Downthrown side invalid. Valid choices: " + choices.join(','));
		    }
		    break;
		case 'length_min':
		case 'length_max':
		case 'length_pref':
		case 'mov_min':
		case 'mov_max':
		case 'mov_pref':
		case 'mom_min':
		case 'mom_max':
		case 'mom_pref':
		case 'width_min':
		case 'width_max':
		case 'width_pref':
		case 'area_min':
		case 'area_max':
		case 'area_pref':
		case 'dip_slip_rate_min':
		case 'dip_slip_rate_max':
		case 'dip_slip_rate_pref':
		case 'strike_slip_rate_min':
		case 'strike_slip_rate_max':
		case 'strike_slip_rate_pref':
		case 'vertical_slip_rate_min':
		case 'vertical_slip_rate_max':
		case 'vertical_slip_rate_pref':
		case 'net_slip_rate_min':
		case 'net_slip_rate_max':
		case 'net_slip_rate_pref':
		case 'dis_min':
		case 'dis_max':
		case 'dis_pref':
		case 're_int_min':
		case 're_int_max':
		case 're_int_pref':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkInterval(grid, fieldName, value));
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkPositive(fieldName, value));
		    break;
		case 'aseis_slip':
		    faulted_earth.utils.pushError(errors,
			      faulted_earth.utils.checkBetween(fieldName, value, 0, 1));
		    break;
		}
		return errors;
	    }
	});
    }
});


/* Overrides GeoExt.form.recordToField to allow custom form input
 * widgets */

var origRecordToField = GeoExt.form.recordToField;
GeoExt.form.recordToField = function(record) {
    var name = record.get("name");
    var field = origRecordToField(record);

    if (faulted_earth.isCalculated(name)) {
	field.xtype = "displayfield";
    }

    var choices = null;

    /* FIXME: choices should be in models.js */

    if (faulted_earth.utils.fieldSuffix(name) == 'com') {
	choices = [1, 2, 3, 4];
    }

    if (name == 'down_thro') {
	choices = ['N', 'S', 'W', 'E', 'NE', 'NW', 'SE', 'SW'];
    }

    if (name == 'slip_type') {
	choices = ['Reverse', 'Thrust (dip <45 deg)',
		   'Normal', 'Dextral', 'Sinistral', 'Normal Dextral',
		   'Dextral Normal', 'Sinistral Normal', 'Normal Sinistral',
		   'Dextral Reverse', 'Sinistral Reverse'];
    }

    if (name == 'slip_rate_category') {
	choices = ['0.001 - <0.01', '0.01 - <0.1', '0.1 - <1',
		   '0.1 - <1', '1 - <5', '5 - <10', '10 - <50',
		   '50 - <100', '100 - <200' ];
    }

    if (name == 're_int_category') {
	choices = ['10 - <100', '100 - <1,000',
		   '1,000 - <2,000', '2,000 - <5,000',
		   '5,000 - <10,000', '10,000 - <100,000',
		   '100,000 - <500,000', '500,000 - <1,000,000',
		   '1,000,000 - <10,000,000' ];
    }

    if (name == "mov_category") {
	choices = ['0 - <1,000', '1,000 - <11,700 (Holocene)',
		   '11,700 - <50,000', '100,000 - <1,000,000',
		   '1,000,000 - <10,000,000' ];
    }

    if (name == "geomorphic_expression") {
	choices = [
	    'Surface trace', 'Eroded scarp', 'Sharp feature',
	    'Topographic feature', 'Bedrock extension',
	    'Concealed', 'No trace'
	];
    }

    if (name == "dis_category") {
	choices = [
	    '0.1 - <0.5', '0.5 - <1', '1 - <5',
	    '5 - <10', '10 - <30' ];
    }

    if (faulted_earth.isCompulsory(name)) {
	field.allowBlank = false;
    }
    
    if (choices) {
	choice_data = [];
	for (var i = 0; i < choices.length; i++) {
	    choice_data.push([choices[i], choices[i]]);
	}
	field.autoSelect = false;
	field.forceSelection = true;
	field.xtype = "combo";
	field.mode = "local";
	field.store = new Ext.data.ArrayStore({
            id: 0,
            fields: [ 'value', 'text' ],
            data: choice_data
	});
	field.triggerAction = 'all';
	field.disableKeyFilter = true;
	field.valueField = 'value';
	field.displayField = 'text';
    }

    return field;
}
GeoExt.form.recordToField.REGEXES = origRecordToField.REGEXES;