from ._anvil_designer import ai_chatTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .chat_summary import chat_summary


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
    self.response_box.text = responses
    anvil.server.call('getmyprompts', {
      "user_prompts": user_prompts,
      "responses": responses
    })
    self.prompt_panel.items = app_tables.responselog.search()
    pass

  @handle('clear_button', 'click')
  def clear_button_click(self, **event_args):
    self.user_prompts.text = ""
    self.prompt_panel.items = app_tables.responselog.search()
    pass

  @handle("done_button", "click")
  def done_button_click(self, **event_args):
    alert(
      content=chat_summary,
      self.edit_summary.text = anvil.server.call("summarize conversation", chat_history)
    )

    if save_clicked:
      # Proceed to Step 5
      anvil.server.call('save_final_summary', check_form.text_area_edit.text)
      pass