Unique Partner Email
====================

.. image:: https://img.shields.io/badge/Odoo-19.0-blue.svg
    :target: https://www.odoo.com/
    :alt: Odoo Version

.. image:: https://img.shields.io/badge/license-LGPL--3-green.svg
    :target: https://www.gnu.org/licenses/lgpl-3.0.en.html
    :alt: License: LGPL-3

Prevent duplicate partner email addresses in Odoo.

Overview
--------

This module prevents creating multiple partners with the same email address
in the Odoo system. It ensures data integrity by enforcing email uniqueness
at both the database level and application level.

Features
--------

* **SQL Constraint**: Enforces email uniqueness at the database level
* **Python Validation**: Additional validation with detailed error messages
* **Case-Insensitive**: Email comparison is case-insensitive
* **Multi-Record Support**: Works correctly with batch operations

Installation
------------

1. Download the module from GitHub repository
2. Place it in your Odoo addons directory
3. Update the apps list in Odoo
4. Install the module

Configuration
-------------

No configuration required. The module works automatically after installation.

Usage
-----

Simply install the module. The system will automatically prevent
creating or updating partners with duplicate email addresses.

If a duplicate email is detected, users will see a clear error message
indicating which partner already uses that email address.

Example error message::

    A partner with email "example@domain.com" already exists: John Doe

Technical Details
-----------------

* **Model**: Extends ``res.partner`` model
* **Dependencies**: base
* **Odoo Version**: 19.0
* **License**: LGPL-3

Supported Versions
------------------

* Odoo 19.0

Repository
----------

**GitHub**: https://github.com/KonstantinAL/unique_partner_email

Bug Tracker
-----------

Bugs are tracked on GitHub Issues.
In case of trouble, please check there if your issue has already been reported.

Credits
-------

Author
~~~~~~

* **Kostiantyn Liapkalo** - *Initial work*

Maintainer
~~~~~~~~~~

This module is maintained by the author.

License
-------

This module is licensed under the LGPL-3 License.
See https://www.gnu.org/licenses/lgpl-3.0.en.html for details.
