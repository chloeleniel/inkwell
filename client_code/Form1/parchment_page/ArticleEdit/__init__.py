from ._anvil_designer import ArticleEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ArticleEdit(ArticleEditTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    @handle("add_article_button", "click")
    def add_article_button_click(self, **event_args):
      new_article = {}
      save_clicked = alert(
        content=ArticleEdit(item=new_article),
        title="Add Article",
        large=True,
        buttons=[("Save", True), ("Cancel", False)],
      )

      if save_clicked:
        anvil.server.call('add_article', new_article)
        self.refresh_articles()

