
$.extend(frappe.listview_settings['Job Card'], {
   onload(listview) {
     //On small screen resolution the Report select Type must be available to select Calendar Type
      $('div.custom-actions').removeClass('hidden-md');
    }
})
