# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class AccessKey(models.Model):
    _inherit = 'project.project'

    keys_clients = fields.Many2one('access.keys', string='Acceso a pass')
  


class AccessKeys(models.Model):
    _name = 'access.keys'
    
    client_name = fields.Many2one('res.partner', string='Cliente')
  
    client_shh = fields.Char(string='SSH')
    client_key = fields.Char(string='Pass')
    client_port = fields.Char(string='Port')
    client_user_ssh = fields.Char(string='SSH User')

    client_host = fields.Char(string='Host')

    client_datebase = fields.Char(string='Base de Datos')
    client_datebase_key = fields.Char(string='Base de Datos Acceso Pass')
    client_datebase_user = fields.Char(string='Base de Datos Acceso Usuario')
    
    client_project = fields.Many2one('project.project', string='Proyecto')
    

    key_visibility = fields.Boolean(string='Visibilidad', compute='_compute_visibility')
    
    # usuario_entorno = fields.Char(string='Usuario Entonro') 
    # usuario_proyecto = fields.Char(string='Usuario Proyecto') 
    # @api.depends('client_project')
    # def _compute_visibility(self):
    #     for record in self:
    #         if record.client_project.user_id.name != self.env.user.name:
    #             record.key_visibility = True
                
    #         else:
    #             record.key_visibility = False
    
    @api.depends('client_project','client_project.task_ids')
    def _compute_visibility(self):
        for record in self:
            num = 0
            if self.env.user not in record.client_project.task_ids.mapped('user_ids') and record.client_project.user_id.name != self.env.user.name:
                
                record.key_visibility = False
                _logger.info('#######Falso###########',record.key_visibility)
            else:
                record.key_visibility = True  
                _logger.info('#######Verdad###########',record.key_visibility)
            
            
            
           
  