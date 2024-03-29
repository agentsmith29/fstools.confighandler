# -*- coding: utf-8 -*-
"""
Author(s): Christoph Schmidt <christoph.schmidt@tugraz.at>
Created: 2023-10-19 12:35
Package Version: 0.0.1
Description:
"""

from confighandler.controller.Field import Field
from confighandler.view.fields.FieldViewString import FieldViewString


class FieldString(Field):
    def __init__(self, value, friendly_name: str = None, description: str = None):
        super().__init__(value, friendly_name, description)
        self._value_replaced_keywords = self.replace_keywords(self.value)

        self._allowed_types = (str, [])

    def create_view(self):
        return FieldViewString(self)

    def _yaml_repr(self):
        return f"\"{self.value}\""
