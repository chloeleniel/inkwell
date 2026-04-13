from ._anvil_designer import parchment_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class parchment_page(parchment_pageTemplate):
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