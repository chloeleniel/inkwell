from ._anvil_designer import ai_chatTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ai_chat(ai_chatTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("send_button", "click")
  def send_button_click(self, **event_args):
    product_name = self.text_box_1.text
    notes = self.text_area_1.text
    input = f'The product name is {product_name} and the product notes are {notes}.'
    description = anvil.server.call('generate_description', input)
    self.rich_text_2.content = description

    
    pass
