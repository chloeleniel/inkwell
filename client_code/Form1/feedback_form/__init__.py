from ._anvil_designer import feedback_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class feedback_form(feedback_formTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  @handle("home", "click")
  def home_click(self, **event_args):
    open_form("Form1")
    pass

  @handle("parchment", "click")
  def parchment_click(self, **event_args):
    open_form("Form1.parchment_page")
    pass

  @handle("feedback_page", "click")
  def feedback_page_click(self, **event_args):
    open_form("Form1.feedback_form")
    pass

  @handle("ai_chat", "click")
  def ai_chat_click(self, **event_args):
    open_form("Form1.ai_chat")
  pass

  @handle("reference", "click")
  def reference_click(self, **event_args):
    open_form('Form1.reference')
    pass

  def clear_inputs(self):
    self.name.text = ""
    self.writing_mode.text = ""
    self.feedback.text = ""
  
  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    name = self.name.text
    writing_mode = self.writing_mode.text
    feedback = self.feedback.text
    anvil.server.call('add_feedback', name, writing_mode, feedback)
    alert("Thank you for your feedback!")
    self.clear_inputs()



