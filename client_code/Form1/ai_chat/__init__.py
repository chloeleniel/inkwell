from ._anvil_designer import ai_chatTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ai_chat(ai_chatTemplate):
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

  @handle("feedback", "click")
  def feedback_click(self, **event_args):
    open_form("Form1.feedback_form")
    pass

  @handle("ai_chat", "click")
  def ai_chat_click(self, **event_args):
    open_form("Form1.ai_chat")
    pass



  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    user_prompts = self.user_prompts.text
    responses = anvil.server.call('generate_questions', user_prompts)
    self.response_card.visible = True
    self.response_box.text = responses
    self.updateprompts()
    pass

    def clear_button_click(self, **event_args):
      self.user_prompt.text = ""
    self.form_show()
    self.updateprompts()
    pass

  def updateprompts(self,**kwargs):
    self.prompt_panel.items = anvil.server.call('getmyprompts')
  pass
    