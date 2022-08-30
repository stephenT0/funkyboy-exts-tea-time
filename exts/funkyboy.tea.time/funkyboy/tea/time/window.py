import omni.ui as ui
from .tea_pot_gen import TeapotSpawn
 

LABEL_WIDTH = 120
SPACING = 4

class TeaWindow(ui.Window):
    def __init__(self, title: str, delegate=None, **kwargs):
        self.__label_width = LABEL_WIDTH

        super().__init__(title, **kwargs)

        
        self.frame.set_build_fn(self._build_fn)
  

    def destroy(self):
        # It will destroy all the children
        super().destroy()

    @property
    def label_width(self):
        """The width of the attribute label"""
        return self.__label_width

    @label_width.setter
    def label_width(self, value):
        """The width of the attribute label"""
        self.__label_width = value
        self.frame.rebuild()

    def _build_fn(self):
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

