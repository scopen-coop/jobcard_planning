frappe.views.Calendar = frappe.views.Calendar.extend({

  init: function(options) {

    //On small screen resolution the Report select Type must be available to select Calendar Type
    options.page.custom_actions.removeClass('hidden-md');
    options.page.custom_actions.find('.sort-selector').addClass('hidden-md');
    //options.page.sort_selector.addClass('hidden-md');

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

  update_event: function(event, revertFunc) {
    if (this.list_view.calendar_name=='Job Card Planning') {
      event.color='#0ecbb1';
      event.backgroundColor='#0ecbb1';
      this.$cal.fullCalendar("updateEvent",event);
    }
    this._super(event, revertFunc);
  }
})
