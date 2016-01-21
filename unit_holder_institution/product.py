# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Julius Network Solutions SARL <contact@julius.fr>
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

from openerp.osv import fields, orm
from openerp import tools
from openerp.tools.translate import _

class unit_holder_institution(orm.Model):
    _name = 'unit.holder.institution'
    
    _columns = {
        'name' : fields.char('name', size=128),
    }


class product_product(orm.Model):
    _inherit = 'product.product'
    
    _columns = {
        'unit_holder_id': fields.many2one('unit.holder.institution', 'Unit Holder Institution'),
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: