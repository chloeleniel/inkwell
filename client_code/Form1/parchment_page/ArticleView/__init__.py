from ._anvil_designer import ArticleViewTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ArticleEdit import ArticleEdit

class ArticleView(ArticleViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @handle("edit_article_button", "click")
  def edit_article_button_click(self, **event_args):
    article_copy = dict(self.item)
    
    save_clicked = alert(
      content=ArticleEdit(item=article_copy),
      title="Update Article",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )

    if save_clicked:
      anvil.server.call('update_article', self.item, article_copy)
      self.refresh_data_bindings()

  @handle("delete_article_button", "click")
  def delete_article_button_click(self, **event_args):
    if confirm("Are you sure you want to delete {}?".format(self.item['title'])):
      self.parent.raise_event('x-delete-article', article=self.item)
    pass
