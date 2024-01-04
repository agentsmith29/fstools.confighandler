# -*- coding: utf-8 -*-
"""
Author(s): Christoph Schmidt <christoph.schmidt@tugraz.at>
Created: 2023-10-19 12:35
Package Version: 0.0.1
Description:
"""



from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QTreeWidgetItem, QMessageBox

import confighandler.controller.Field as Field


class FieldView(QWidget):
    value_changed = Signal(Field.T)

    def __init__(self, parent_field):
        super().__init__()

        self.parent_field = parent_field

        self.label = None
        self.ui_edit_fields = []
        self.tree_items = []

        self.value_changed.connect(self._on_value_changed)
        #self.setToolTip(parent_field._description)

        if isinstance(Field.T, str):
            print(">>> String")

    def _on_value_changed(self, value):
        """
        Updates the UI when the value is changed.
        :param value:
        :return:
        """
        self._on_value_changed_partial(value)

    def _on_value_changed_partial(self, value):
        """
        Additional actions when the value is changed.
        :param value:
        :return:
        """
        raise NotImplementedError()

    def add_new_view(self, view: QWidget):
        self.ui_field(view)



    def ui_field(self, view: QWidget) -> QWidget:
        """
        Returns a QLineEdit for the UI.
        The UI is automatically updated when the value is changed.
        """
        raise NotImplementedError()

    def ui_tree_widget_item(self):
        """Returns a QItem for the QTreeView"""
        item = self.ui_field()
        tree_view_item = QTreeWidgetItem([self.parent_field.name, None, self.parent_field.description])
        # tree_view_item = QTreeWidgetItem([self.ui_field()])
        self.tree_items.append(tree_view_item)
        # tree_view_item.set
        return self.tree_items[-1], item

    def _input_validation(self, value):
        return value

    def _display_error(self, e: Exception):
        for edit in self.ui_edit_fields:
            edit.setStyleSheet("border: 1px solid red")

        self.parent_field.logger.error(e)
        # Display an error message
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText("Input is invalid")
        self.msg.setWindowTitle("Error")
        self.msg.show()


