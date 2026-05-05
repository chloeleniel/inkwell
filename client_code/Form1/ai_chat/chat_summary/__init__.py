from ._anvil_designer import chat_summaryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class chat_summary(chat_summaryTemplate):
  def __init__(self, summary_text, **properties):
    self.init_components(**properties)

    self.edit_summary.text = summary_text
