# -*- coding: utf-8 -*-
{
    'name': 'Unique Partner Email',
    'version': '19.0.1.0.0',
    'category': 'Tools',
    'summary': 'Prevent duplicate partner email addresses',
    'description': """
Unique Partner Email
======================

This module prevents creating multiple partners with the same email address
in the Odoo system. It ensures data integrity by enforcing email uniqueness
at both the database level and application level.

Key Features:
-------------
* **SQL Constraint**: Enforces email uniqueness at the database level
* **Python Validation**: Additional validation with detailed error messages
* **Case-Insensitive**: Email comparison is case-insensitive
* **Multi-Record Support**: Works correctly with batch operations

Technical Details:
------------------
* Extends ``res.partner`` model
* Adds SQL UNIQUE constraint on email field
* Implements ``@api.constrains`` for additional validation
* Compatible with Odoo 19.0

Usage:
------
Simply install the module. The system will automatically prevent
creating or updating partners with duplicate email addresses.

If a duplicate email is detected, users will see a clear error message
indicating which partner already uses that email address.

Supported Odoo Versions:
------------------------
* Odoo 19.0
    """,
    'author': 'Kostiantyn Liapkalo',
    'website': 'https://github.com/KonstantinAL/unique_partner_email',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [],
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'support': 'kosskoss59@gmail.com',
}
