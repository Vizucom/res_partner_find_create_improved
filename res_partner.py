# -*- coding: utf-8 -*-
from openerp.osv import osv
from openerp import tools

class res_partner(osv.Model):

    _inherit = 'res.partner'

    def find_or_create(self, cr, uid, email, context=None):
        assert email, 'an email is required for find_or_create to work'
        emails = tools.email_split(email)
        if emails:
            email = emails[0]
        
        try:
            ids = []
            # Get the model we are dealing with, e.g. Sale Order
            # and the record id, e.g. 84
            model = self.pool.get(context.get('active_model'))        
            record_id = context.get('active_id')
            
            # Find out the partner related to the record. Use that partner 
            # as an extra criteria in the search domain when looking for 
            # existing partners with the same email address. 
            
            record_partner = model.browse(cr, uid, record_id).partner_id
            
            if record_partner:
                ids = self.search(cr, uid, [('email','ilike',email),
                                            ('id','=',record_partner.id)], 
                                  context=context)
            
            # If no matches, try to search children
            if not ids:
                ids = self.search(cr, uid, [('email','ilike',email),
                                            ('parent_id','=',record_partner.id)],
                                  context=context) 
            
            # If still no matches were found, use the default implementation as fallback
            if ids:
                return ids[0]
            else:
                return super(res_partner, self).find_or_create(cr, uid, email, context)
            
        except:
            # Fallback also in case e.g. the partner_id field does not exist
            return super(res_partner, self).find_or_create(cr, uid, email, context)    