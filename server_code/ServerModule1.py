import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_feedback(name, writing_mode, feedback):
  app_tables.feedback.add_row(
    name=name, 
    writing_mode=writing_mode, 
    feedback=feedback, 
    created=datetime.now()
  )

@anvil.server.callable
def add_article(article_dict):
  app_tables.articles.add_row(
    created=datetime.now(),
    **article_dict
  )

@anvil.server.callable
def get_articles():
  return app_tables.articles.search(
    tables.order_by("created", ascending=False)
  )