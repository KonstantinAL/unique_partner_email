# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.exceptions import ValidationError
from odoo import _


class ResPartner(models.Model):
    """
    Extend res.partner to enforce email uniqueness.
    
    This model prevents creating multiple partners with the same
    email address through SQL constraints and Python validation.
    """
    _inherit = 'res.partner'

    _sql_constraints = [
        ('email_unique',
         'UNIQUE(email)',
         'A partner with this email address already exists. '
         'Email addresses must be unique across all partners.'),
    ]

    @api.constrains('email')
    def _check_email_unique(self):
        """
        Validate email uniqueness across all partners.
        
        This constraint prevents creating or updating partners
        with an email address that is already used by another partner.
        
        Raises:
            ValidationError: If email is already assigned to another partner.
        """
        for partner in self:
            if partner.email:
                # Search for partners with the same email (excluding current partner)
                duplicate = self.search([
                    ('email', '=ilike', partner.email),
                    ('id', '!=', partner.id),
                    ('id', 'not in', partner.ids),  # Handle multiple records in self
                ], limit=1)
                
                if duplicate:
                    raise ValidationError(
                        _('A partner with email "%(email)s" already exists: %(partner)s') % {
                            'email': partner.email,
                            'partner': duplicate[0].display_name,
                        }
                    )
