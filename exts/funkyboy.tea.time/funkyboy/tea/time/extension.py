import omni.ext
import omni.ui as ui
from .tea_pot_gen import TeapotSpawn

class MyExtension(omni.ext.IExt):

    def on_startup(self, ext_id):
        print("[funkyboy.tea.test] MyExtension startup")

        self._window = ui.Window("Tea Time", width=250, height=250)
        with self._window.frame:
            with ui.VStack():
                style = {"margin_width": 20}
                style={"background_color": 0x33FFF86}
                ui.Button("Is it Tea Time?", style=style,)

                def on_click():
                    TeapotSpawn()

                ui.Button("Make Tea", clicked_fn=lambda: on_click(), style={"Button": {"background_color":  0xFF00B976}}, tooltip="  spawns teapot at world center  ")

    def on_shutdown(self):
        print("[funkyboy.tea.test] MyExtension shutdown")
