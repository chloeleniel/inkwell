from ._anvil_designer import ai_chatTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
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

  @handle("reference", "click")
  def reference_click(self, **event_args):
    open_form('Form1.reference')
  pass

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    current_user = anvil.users.get_user()
    user_prompts = self.user_prompts.text
    responses = anvil.server.call('generate_questions', user_prompts)
    self.response_box.text = responses
    self.prompt_panel.items = app_tables.responselog.search(user=current_user)
    pass

  @handle('clear_button', 'click')
  def clear_button_click(self, **event_args):
    self.user_prompts.text = ""
    self.prompt_panel.items = app_tables.responselog.search()
    pass
  
  @handle("done_button", "click")
  def done_button_click(self, **event_args):
    summary_data = anvil.server.call('summarize_chat')
    summary_content = chat_summary(summary_text=summary_data)
    save_clicked = alert(
      content=summary_content,
      title="Confirm Responses",
      large=True,
      buttons=[("Save", True), ("Cancel", False)],
    )

    if save_clicked:
      anvil.server.call('add_ref', summary_data)