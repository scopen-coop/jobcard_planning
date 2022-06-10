/*frappe.views.Calendar = Class.extend({
  setup_options: function (defaults) {
    var me = this;
    console.log(me);
    parent.setup_options(defaults);
  }
})*/

frappe.views.Calendar = frappe.views.Calendar.extend({

  init: function(options) {
		$.extend(true, this, options);
    if (this.list_view.calendar_name=='Job Card Planning') {
      this.get_events_method='jobcard_planning.controllers.jobcard_planning.get_jobcard_planning_details';

      this.field_map= {
        "start": "from_time",
        "end": "to_time",
        "id": "name",
        "title": "subject",
        "color": "color",
        "allDay": "allDay",
        "progress": "progress"
      };

      // this.gantt= {
      //   field_map: {
      //     "start": "started_time",
      //     "end": "started_time",
      //     "id": "name",
      //     "title": "subject",
      //     "color": "color",
      //     "allDay": "allDay",
      //     "progress": "progress"
      //   }
      // };

      this.filters= [
        {
          "fieldtype": "Link",
          "fieldname": "planned_employee",
          "options": "Employee",
          "label": __("Planned Employee")
        }
      ];
     }
		this.get_default_options();
	},
})
