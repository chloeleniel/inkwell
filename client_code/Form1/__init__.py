from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  @handle("home", "click")
  def home_click(self, **event_args):
    open_form("Form1")
    pass

  @handle("parchment", "click")
  def parchment_click(self, **event_args):
    open_form("Form1.parchment_page")
    pass


  stages = ["prewriting", "drafting", "revising"]
    
  @handle("prewriting", "click")
  def prewriting_click(self, **event_args):
      stage = [0]
      pass
  
  @handle("drafting", "click")
  def drafting_click(self, **event_args):
    stage = [1]
    pass

  @handle("revising", "click")
  def revising_click(self, **event_args):
    stage = [2]
    pass