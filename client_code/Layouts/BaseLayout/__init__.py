from ._anvil_designer import BaseLayoutTemplate
from anvil import *
from routing import router
import m3.components as m3


class BaseLayout(BaseLayoutTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
