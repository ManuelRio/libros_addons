from odoo import models,fields,api

class Extension(models.Model):
    _inherit='library.data'

    cover=fields.Binary('Cover page')
    score=fields.Float(string="Score")

    @api.onchange('status')
    def _onchage_state(self):
        if self.quan_e==0:
            self.status="not available"

    @api.onchange('belongs')
    def _onchage_series(self):
        self.series=""


    
       
