# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Improved find_or_create for Partners',
    'category': 'CRM',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': [],
    'description': """
Improved find_or_create for Partners
====================================
 * By default, the partner model's find_or_create() function accepts any matching e-mail addresses with no additional criteria.
 * This can cause confusion in the mail composition wizard in some situations where the same e-mail address is used for different partners (the wrong partner is shown in the wizard, even though the e-mail address is correct).
 * This module customizes the function to primarily search for email addresses that are related to the Partner of the object that triggered the opening of the composition wizard. 
 * If no match is found with this module's search, the core's search is still used as a fallback.
""",
    'data': [],
}
