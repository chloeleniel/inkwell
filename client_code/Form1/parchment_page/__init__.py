from ._anvil_designer import parchment_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .ArticleEdit import ArticleEdit


class parchment_page(parchment_pageTemplate):
    def refresh_articles(self):
      self.articles_panel.items = anvil.server.call('get_articles')
      
    def __init__(self, **properties):
      self.init_components(**properties)
      self.refresh_articles()

      @handle("home", "click")
      def home_click(self, **event_args):
        open_form("Form1")
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

    @handle("add_article", "click")
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
  
    @handle('articles_panel', 'x-delete-article')
    def delete_article(self, article, **event_args):
      # Delete the article
      anvil.server.call('delete_article', article)
      self.refresh_articles()



    

