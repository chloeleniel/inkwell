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