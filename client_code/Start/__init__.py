from ._anvil_designer import StartTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Start(StartTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  @handle("sign_up", "click")
  def sign_up_click(self, **event_args):
    anvil.users.login_with_form()

    if anvil.users.get_user():
      open_form("Form1")
    else:
      self.form_show()
    pass
