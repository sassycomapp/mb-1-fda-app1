from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from routing import router
import m3.components as m3


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)
