from odoo import models,fields,api

class Extension(models.Model):
    _inherit='library.data'

    cover=fields.Binary('Cover page')
    score=fields.Float(string="Score")

    @api.onchange('state')
    def _onchage_state(self):
        if self.quan_e==0:
            self.state="not available"

    @api.onchange('series')
    def _onchage_series(self):
        if self.belongs:
            belongs= False 
            self.series=""


    
       
