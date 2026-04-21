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

  response = anvil.server.call('generate_questions', input)
  self.rich_text_1.content = response
