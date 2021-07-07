from odoo import models,fields 

class Data(models.Model):
    _name="library.data"

    name=fields.Char(string="Book's name")
    author_id=fields.Many2one('library.author', string="Author's name")
    date_e=fields.Date(string="Realese date") 
    quan_e=fields.Integer( string="Quantity in stock")
    state=fields.Selection(selection = [("available", "Available"), ("not available", "Not available")], string="State")
    belongs=fields.Boolean(string="It belongs to a collection?")
    series =fields.Char(string="Collection's name" )

class Authors(models.Model):
    _name="library.author"

    name=fields.Char(string="Author's name" )
    books_ids=fields.One2many('library.data', inverse_name = 'author_id', string="Books")


