import datetime

import frappe, json

@frappe.whitelist()
def get_jobcard_planning_details(start, end, filters=None):

    events = []

    event_color = {
        "Material Transferred": "#2acced",
        "Work In Progress": "#ed982a",
        "Open": "#cc5908",
    }

    from frappe.desk.reportview import get_filters_cond

    conditions = get_filters_cond("Job Card", filters, [])

    job_cards = frappe.db.sql(
        """  SELECT `tabJob Card`.name, `tabJob Card`.work_order,
            `tabJob Card`.status, ifnull(`tabJob Card`.remarks, ''),
            `tabJob Card`.operation,
            `tabCustomer`.customer_name,
            tabItem.item_name,
            `tabJob Card`.planned_start_date,
            `tabJob Card`.planned_end_date,
            `tabJob Card`.planned_employee_name,
            min(`tabJob Card Time Log`.from_time) as initial_start_date,
            max(`tabJob Card Time Log`.from_time) as initial_end_date,
            `tabWork Order`.planned_start_date as work_order_planned_start_date,
            `tabJob Card`.expected_delivery_date
        FROM `tabJob Card` LEFT JOIN `tabJob Card Time Log`
        ON `tabJob Card`.name = `tabJob Card Time Log`.parent
        INNER JOIN `tabWork Order` ON `tabWork Order`.name=`tabJob Card`.work_order
        INNER JOIN `tabItem` ON `tabItem`.item_name=`tabWork Order`.item_name
        LEFT JOIN `tabSales Order` ON `tabSales Order`.name=`tabWork Order`.sales_order
        LEFT JOIN `tabCustomer` ON `tabCustomer`.name=`tabSales Order`.customer
        WHERE
             `tabJob Card`.status<>'Completed'
             {0}
            group by `tabJob Card`.name""".format(
            conditions
        ),
        as_dict=1,
    )

    # Attemp to make it with query Builder, but there is no
    # to convert form filters to .where()

    # from frappe.query_builder.functions import Min, Max
    # JobCard = frappe.qb.DocType("Job Card")
    # JobCardTimeLog = frappe.qb.DocType("Job Card Time Log")
    # job_cards_query = (
    #     frappe.qb.from_(JobCard)
    #     .inner_join(JobCardTimeLog)
    #     .on(JobCard.name == JobCardTimeLog.parent)
    #     .groupby(JobCard.name)
    #     .having(Min(JobCardTimeLog.from_time) >= start)
    #     .having(Max(JobCardTimeLog.from_time) <= end)
    #     .select(
    #         JobCard.name,
    #         JobCard.work_order,
    #         JobCard.status,
    #         JobCard.remarks,
    #         JobCard.planned_start_date,
    #         JobCard.planned_end_date,
    #         Min(JobCardTimeLog.from_time).as_('initial_start_date'),
    #     )
    # )
    #job_cards = job_cards_query.run(as_dict=1)

    for d in job_cards:
        subject_data = []
        for field in ["customer_name", "item_name", "operation", "planned_employee_name", "work_order"
            , "expected_delivery_date"]:
            if not d.get(field):
                continue

            if type(d.get(field)) is datetime.date:
                data_txt = d.get(field).strftime('%Y-%m-%d')
            else:
                data_txt = d.get(field)
            subject_data.append(data_txt)


        if (d.planned_start_date is None):
            color = '#D3D3D3'
            if d.initial_start_date is None:
                start_date = d.work_order_planned_start_date
                end_date = d.work_order_planned_start_date
            else:
                start_date = d.initial_end_date
                end_date = d.initial_end_date
        else:
            color = event_color.get(d.status)
            start_date = d.planned_start_date
            end_date = d.planned_end_date

        job_card_data = {
            "planned_start_date": start_date,
            "planned_end_date": end_date,
            "name": d.name,
            "subject": "\n".join(subject_data),
            "color": color,
        }

        events.append(job_card_data)

    return events

@frappe.whitelist()
def update_jobcard_planned_date(args, field_map):
    """Updates Event (called via calendar) based on passed `field_map`"""
    args = frappe._dict(json.loads(args))
    field_map = frappe._dict(json.loads(field_map))
    w = frappe.get_doc(args.doctype, args.name)
    w.db_set(field_map.start, args[field_map.start])
    w.db_set(field_map.end, args.get(field_map.end))
