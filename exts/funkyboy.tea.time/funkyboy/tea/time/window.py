import omni.ui as ui
import omni.ext
import omni.kit.commands
from .tea_pot_gen import TeapotSpawn


WINDOW_TITLE = "Tea Time"

class TeaWindow(ui.Window):
    def __init__(self, title, menu_path):
        super().__init__(title, width=200, height=200)
        self._menu_path = menu_path
        self.set_visibility_changed_fn(self._on_visibility_changed)
        self._build_ui()
    
    def on_shutdown(self):
        self._win = None

    def show(self):
        self.visible = True
        self.focus()    
    
    def hide(self):
        self.visible = False

    def _build_ui(self):
        """
        The method that is called to build all the UI once the window is
        visible.
        """
  
        with self.frame:
            with ui.VStack():
                #style = {"margin_width": 20}
                style={"background_color": 0x33FFF86, "color": 0xFF00B976, "font_size": 16}
                ui.Button("Is it Tea Time?", style=style,)

                def on_click():
                    TeapotSpawn()

                ui.Button("Make Tea", clicked_fn=lambda: on_click(), style={"Button": {"background_color":  0xFF00B976}, "font_size": 16}, tooltip="  spawns teapot at world center  ")

    def _on_visibility_changed(self, visible):
        omni.kit.ui.get_editor_menu().set_value(self._menu_path, visible)