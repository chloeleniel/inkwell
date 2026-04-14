from ._anvil_designer import ArticleEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ArticleEdit(ArticleEditTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
