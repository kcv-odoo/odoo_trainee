# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date
from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression
import json

class CustomerPortal(CustomerPortal):
    @http.route(['/my/proposals/<int:proposal_id>'], type='http', auth="public", website=True)
    def portal_proposal_page(self, proposal_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            proposal_sudo = self._document_check_access('sale.proposal', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=proposal_sudo, report_type=report_type, report_ref='odoo_trainee.action_report_proposal', download=download)

        # use sudo to allow accessing/viewing orders for public user
        # only if he knows the private token
        # Log only once a day
        if proposal_sudo:
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_proposal%s' % proposal_sudo.id)
            if isinstance(session_obj_date, date):
                session_obj_date = session_obj_date.isoformat()
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_proposal%s' % proposal_sudo.id] = now
                body = _('Proposal viewed by customer %s') % proposal_sudo.customer_id.name
                _message_post_helper(
                    "sale.proposal",
                    proposal_sudo.id,
                    body,
                    token=proposal_sudo.access_token,
                    message_type="notification",
                    subtype="mail.mt_note",
                    partner_ids=proposal_sudo.salesman_id.sudo().partner_id.ids,
                )

        values = {
            'sale_proposal': proposal_sudo,
            'message': message,
            'token': access_token,
            'return_url': '/shop/payment/validate',
            'bootstrap_formatting': True,
            'partner_id': proposal_sudo.customer_id.id,
            'report_type': 'html',
            'action': proposal_sudo._get_portal_return_action(),
        }
        if proposal_sudo.company_id:
            values['res_company'] = proposal_sudo.company_id

        history = request.session.get('my_proposals_history', [])

        values.update(get_records_pager(history, proposal_sudo))
        return request.render('odoo_trainee.proposal_portal_template', values)

    @http.route(['/my/proposals/<int:proposal_id>/accept'], type='http', auth="public", website=True, methods=['POST'])
    def portal_proposal_accept(self, proposal_id, access_token=None, name=None,**post):
        # get from query string if not on json param
        try:
            proposal_sudo = self._document_check_access('sale.proposal', proposal_id, access_token=access_token)

        except (AccessError, MissingError):
            return request.redirect('/my')
        proposal_sudo.write({
            'proposal_status': 'accept',
            'accepted_total_price':float(post["final_price_accepted"])
        })

        request.env.cr.commit()
        line_key = 0
        lines_data = json.loads(post["lines_data"])
        for line in proposal_sudo.proposal_line_ids:
            proposal_line_sudo = request.env['proposal.line'].browse(line.id)
            proposal_line_sudo.write({
                'qty_accepted': int(lines_data["value_"+str(line_key)][0]),
                'price_accepted': float(lines_data["value_"+str(line_key)][1]),
                # 'accepted_sub_total':float(lines_data["value_"+str(line_key)][2])
            })
            request.env.cr.commit()
            line_key+=1

        message = post.get('accepting_message')

        _message_post_helper(
            'sale.proposal', proposal_sudo.id, _('Proposal is Accepted.'),
            **({'token': access_token} if access_token else {}))

        query_string = False
        if message:
            _message_post_helper('sale.proposal', proposal_id, message, **{'token': access_token} if access_token else {})
        else:
            query_string = "&message=cant_accept"

        return request.redirect(proposal_sudo.get_portal_url(query_string=query_string))


    @http.route(['/my/proposals/<int:proposal_id>/decline'], type='http', auth="public", methods=['POST'], website=True)
    def decline(self, proposal_id, access_token=None, **post):
        try: proposal_sudo = self._document_check_access('sale.proposal', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        proposal_sudo.write({
            'proposal_status': 'reject',
            'state':'cancel'
        })
        request.env.cr.commit()

        message = post.get('decline_message')

        query_string = False
        if message:
            _message_post_helper('sale.proposal', proposal_id, message, **{'token': access_token} if access_token else {})
        else:
            query_string = "&message=cant_reject"

        return request.redirect(proposal_sudo.get_portal_url(query_string=query_string))