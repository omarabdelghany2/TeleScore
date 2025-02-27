from PyQt6.QtWidgets import QPushButton
from abstract.abstractcomp import AbstractComp
from attr import CompType

class MacroButtonComp(AbstractComp, QPushButton):
    def __init__(self, project, parent=None):
        super().__init__(project, "MacroButton", CompType.CONTROL, parent)
        self.setText("Macro")  # Default text for the button
        self.clicked.connect(self.on_macro_clicked)

    def on_macro_clicked(self):
        print("Macro Button Clicked!")  # Placeholder action for now

    def getName(self) -> str:
        return "Macro Button"

    def _firstTimeProp(self):
        """Initialize component-specific properties."""
        self._properties["Button Text"] = "Macro"

    def _derPropRequested(self):
        """Update properties when requested."""
        self.setText(self._properties["Button Text"])

    def _derPropChanged(self):
        """Update properties when changed."""
        self.setText(self._properties["Button Text"])
