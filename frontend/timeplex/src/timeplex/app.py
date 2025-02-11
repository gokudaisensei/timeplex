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
        instructors_button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        instructors_add_button = toga.Button("Add Instructor", style=Pack(padding=5))
        instructors_import_button = toga.Button(
            "Import from CSV", style=Pack(padding=5)
        )
        instructors_button_box.add(instructors_add_button)
        instructors_button_box.add(instructors_import_button)

        instructors_table = toga.Table(
            headings=["Available", "Name", "Hours", "Operation"], style=Pack(flex=10)
        )
        instructors_box.add(instructors_button_box)
        instructors_box.add(instructors_table)

        # Rooms tab
        rooms_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        rooms_button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        rooms_add_button = toga.Button("Add Room", style=Pack(padding=5))
        rooms_import_button = toga.Button("Import from CSV", style=Pack(padding=5))
        rooms_button_box.add(rooms_add_button)
        rooms_button_box.add(rooms_import_button)

        rooms_table = toga.Table(
            headings=["Available", "Name", "Operation"], style=Pack(flex=4)
        )
        rooms_box.add(rooms_button_box)
        rooms_box.add(rooms_table)

        # Subjects tab
        subjects_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        subjects_button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        subjects_add_button = toga.Button("Add Subject", style=Pack(padding=5))
        subjects_import_button = toga.Button("Import from CSV", style=Pack(padding=5))
        subjects_button_box.add(subjects_add_button)
        subjects_button_box.add(subjects_import_button)

        subjects_table = toga.Table(
            headings=["Code", "Name", "Type", "Instructors", "Operation"],
            style=Pack(flex=4),
        )
        subjects_box.add(subjects_button_box)
        subjects_box.add(subjects_table)

        # Empty placeholders for other tabs
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
