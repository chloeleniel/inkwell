from ._anvil_designer import ref_viewTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ref_edit import ref_edit


class ref_view(ref_viewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @handle("edit_ref_button", "click")
  def edit_ref_button_click(self, **event_args):
    ref_copy = dict(self.item)

    save_clicked = alert(
      content=ref_edit(item=ref_copy),
      title="Update Reference",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )

    if save_clicked:
      anvil.server.call('update_ref', self.item, ref_copy)
      self.refresh_data_bindings()

  @handle("delete_ref_button", "click")
  def delete_ref_button_click(self, **event_args):
    if confirm("Are you sure you want to delete {}?".format(self.item['ref_title'])):
      self.parent.raise_event('x-delete_ref', reference=self.item)
    pass
