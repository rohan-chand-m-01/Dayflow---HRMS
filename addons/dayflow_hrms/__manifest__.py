# addons/dayflow_hrms/__manifest__.py
# Dayflow HRMS — Odoo 18.0 module manifest.
{
    'name': 'Dayflow HRMS',
    'version': '18.0.1.0.0',
    'summary': 'Human Resource Management System for Dayflow',
    'description': """
Dayflow HRMS
============
A custom Human Resource Management System built on Odoo 18.0 Community.

Developed for the Odoo × NMIT Bengaluru online screening hackathon.

Features (to be implemented across phases):
- Employee profile management
- Attendance tracking
- Leave / time-off management
- Approval workflows
- Payroll / salary visibility
- HR and Admin dashboards
    """,
    'author': 'Dayflow Team',
    'category': 'Human Resources',
    'license': 'LGPL-3',

    # Phase 1: only 'base' is strictly required for an empty skeleton.
    # HR-specific dependencies (hr, hr_attendance, hr_holidays, payroll)
    # will be added in the phases where they become necessary.
    'depends': ['base'],

    'data': [],
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}
