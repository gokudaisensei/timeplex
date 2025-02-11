import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Timeplex(toga.App):
    def startup(self):
        """Construct and show the Toga application with tabs and table view."""
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Tabbed Interface
        tab_container = toga.OptionContainer()

        # Instructors Tab
        instructors_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        add_button = toga.Button("Add Instructor", style=Pack(padding=5))
        import_button = toga.Button("Import from CSV", style=Pack(padding=5))
        button_box.add(add_button)
        button_box.add(import_button)

        table = toga.Table(
            headings=["Available", "Name", "Hours", "Operation"], style=Pack(flex=1)
        )
        instructors_box.add(button_box)
        instructors_box.add(table)

        # Empty placeholders for other tabs
        rooms_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        subjects_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        sections_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        scenario_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Add tabs
        tab_container.content.append("Instructors", instructors_box)
        tab_container.content.append("Rooms", rooms_box)
        tab_container.content.append("Subjects", subjects_box)
        tab_container.content.append("Sections", sections_box)
        tab_container.content.append("Scenario Manager", scenario_box)

        self.main_window.content = tab_container
        self.main_window.show()


def main():
    return Timeplex()
