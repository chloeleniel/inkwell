from ._anvil_designer import referenceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class reference(referenceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_references.items = anvil.server.call('show_ref')

  @handle("home", "click")
  def home_click(self, **event_args):
    open_form("Form1")
  pass

  @handle("parchment", "click")
  def parchment_click(self, **event_args):
    open_form("Form1.parchment_page")
    pass

  @handle("feedback", "click")
  def feedback_click(self, **event_args):
    open_form("Form1.feedback_form")
    pass

  @handle("ai_chat", "click")
  def ai_chat_click(self, **event_args):
    open_form("Form1.ai_chat")
    pass

