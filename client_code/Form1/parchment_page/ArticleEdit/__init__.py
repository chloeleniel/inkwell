from ._anvil_designer import ArticleEditTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ArticleEdit(ArticleEditTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.title_box.text = self.item['title']
    self.content_box.text = self.item['content']

    self.last_saved_title = self.title_box.text
    self.last_saved_content = self.content_box.text

  @handle('timer_1', 'tick')
  def timer_1_tick(self, **event_args):
    current_title = self.title_box.text
    current_content = self.content_box.text

    if current_title != self.last_saved_title or current_content != self.last_saved_content:
      self.last_saved_title = current_title
      self.last_saved_content = current_content

      self.save_status.text = "Saving..."

      anvil.server.call_s('update_article', self.item, {
        'title': current_title,
        'content': current_content
    })

      self.save_status.text = "All changes saved."