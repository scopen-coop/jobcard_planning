
$.extend(frappe.listview_settings['Job Card'], {
   onload(listview) {
     console.log(listview);
      $('div.custom-actions').removeClass('hidden-md');        // triggers once before the list is loaded
    }
})
console.log(frappe.listview_settings['Job Card']);

