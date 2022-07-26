# -*- coding: utf-8 -*-
# Copyright (c) 2021, scopen.fr and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def upd_work_order(doc, method):

    for jobcards_to_update in frappe.db.get_all("Job Card", fields=["name"],
                                            filters={"work_order": doc.name,
                                                     "expected_delivery_date": ["!=", doc.expected_delivery_date],
                                                     "status": ["in", ('Open','Submitted')]}):
        jobcard_to_update = frappe.get_doc("Job Card", jobcards_to_update.name)
        jobcard_to_update.expected_delivery_date = doc.expected_delivery_date
        jobcard_to_update.save()
