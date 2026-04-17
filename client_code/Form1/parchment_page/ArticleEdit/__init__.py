from ._anvil_designer import ArticleEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ArticleEdit(ArticleEditTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  @handle("send_button", "click")
  def send_button_click(self, **event_args):
    input = self.text_area_1.text
    response = anvil.server.call('generate_questions', input)
    self.rich_text_1.content = response
    pass