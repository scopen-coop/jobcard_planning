
$.extend(frappe.listview_settings['Job Card'], {
   onload(listview) {
      $('div.custom-actions').removeClass('hidden-md');        // triggers once before the list is loaded
    }
})

