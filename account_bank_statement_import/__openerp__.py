# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    "name"      : "Bank statement import with specific filters",
    "version"   : "1.0",
    "author"    : "Julius Network Solutions",
    "category"  : "Accounting & Finance",
    "description": """
    Module provides functionality to import
    bank statements from another files than coda with parser.
    """,
    "depends"   : [
        "account",
        "account_voucher",
#       "l10n_fr_coda",
    ],
    "demo_xml"  : [],
    "init_xml"  : [],
    "update_xml": [
        "security/ir.model.access.csv",
        "data/filters_data.xml",
        "config_view.xml",
        "wizard/statement_import.xml",
#        "account_coda_view.xml",
    ],
    "active"    : False,
    "installable" : True,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
