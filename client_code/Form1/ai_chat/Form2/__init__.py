from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  @handle("done_button", "click")
  def done_button_click(self, **event_args):
    history = self.responselog.items
    summary_text = anvil.server.call('summarize_conversation', history)

    # 2. Transition to Step 4 (The Check/Verification Step)
    # Open an alert or change the content_panel to your Verification Form
    check_form = VerificationForm(summary_content=summary_text)
    save_clicked = alert(content=check_form, large=True, buttons=[("Confirm & Save", True), ("Cancel", False)])

    if save_clicked:
      # Proceed to Step 5
      anvil.server.call('save_final_summary', check_form.text_area_edit.text)