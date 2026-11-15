from ._anvil_designer import Form1Template
from anvil import *
import m3.components as m3


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)
