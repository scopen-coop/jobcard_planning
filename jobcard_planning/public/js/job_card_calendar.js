/*frappe.views.Calendar = Class.extend({
  setup_options: function (defaults) {
    var me = this;
    console.log(me);
    parent.setup_options(defaults);
  }
})*/

frappe.views.Calendar = frappe.views.Calendar.extend({

  init: function(options) {
    this._super(options);
    if (this.list_view.calendar_name=='Job Card Planning') {
      this.get_events_method='jobcard_planning.controllers.jobcard_planning.get_jobcard_planning_details';
      this.field_map= {
        "start": "planned_start_date",
        "end": "planned_end_date",
        "id": "name",
        "title": "subject",
        "color": "color",
        "allDay": "allDay",
        "progress": "progress"
      };

      this.filters= [
        {
          "fieldtype": "Link",
          "fieldname": "planned_employee",
          "options": "Employee",
          "label": __("Planned Employee")
        }
      ];
      this.update_event_method='jobcard_planning.controllers.jobcard_planning.update_jobcard_planned_date';
     }
	},
})
