from . import __version__ as app_version

app_name = "jobcard_planning"
app_title = "Planning for Job Card"
app_publisher = "Scopen"
app_description = "Add planned date and calendar (updatable) view for Job Card"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "contact@scopen.fr"
app_license = "GPLv3"

# Includes in <head>
# ------------------
fixtures = [
    {
        "dt": ("Custom Field"),
        "filters": [["name", "in",
                     (
                         "Job Card-planification",
                         "Job Card-planned_start_date",
                         "Job Card-planned_end_date",
                         "Job Card-planned_employee",
                         "Job Card-planned_employee_name",
                         "Job Card-sales_order",
                         "Job Card-expected_delivery_date",
                         "Job Card-qty_to_manufacture_per_day",
                         "Workstation-custom_default_employee",)]
                    ]
    },
    {
        "dt": ("Calendar View"),
        "filters": [["name", "in", ('Job Card Planning')]]
    },
    {
        "dt": ("Report"),
        "filters": [["name", "in", ('Job Card Planning Qty')]]
    },
    {
        "dt": ("Role"),
        "filters": [["name", "in", ('Atelier')]]
    }
]



# include js, css files in header of desk.html
# app_include_css = "/assets/jobcard_planning/css/jobcard_planning.css"
# app_include_js = "/assets/jobcard_planning/js/jobcard_planning.js"

# include js, css files in header of web template
# web_include_css = "/assets/jobcard_planning/css/jobcard_planning.css"
# web_include_js = "/assets/jobcard_planning/js/jobcard_planning.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jobcard_planning/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {"Job Card": "public/js/job_card_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
doctype_calendar_js = {"Job Card": "public/js/job_card_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "jobcard_planning.install.before_install"
# after_install = "jobcard_planning.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jobcard_planning.uninstall.before_uninstall"
# after_uninstall = "jobcard_planning.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jobcard_planning.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    ("Work Order"): {
        "on_change": "jobcard_planning.custom_scripts_py.work_order.upd_work_order"
    },
}
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jobcard_planning.tasks.all"
# 	],
# 	"daily": [
# 		"jobcard_planning.tasks.daily"
# 	],
# 	"hourly": [
# 		"jobcard_planning.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jobcard_planning.tasks.weekly"
# 	]
# 	"monthly": [
# 		"jobcard_planning.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "jobcard_planning.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.calendar.update_event": "jobcard_planning.controllers.jobcard_planning.update_event_custom"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "jobcard_planning.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#     {
#         "doctype": "{doctype_1}",
#         "filter_by": "{filter_by}",
#         "redact_fields": ["{field_1}", "{field_2}"],
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_2}",
#         "filter_by": "{filter_by}",
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_3}",
#         "strict": False,
#     },
#     {
#         "doctype": "{doctype_4}"
#     }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"jobcard_planning.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
