from pathlib import Path
import omni.usd
import omni.kit.app
import omni.kit.commands

from pxr import Sdf


TEAPOT_USD = Path(__file__).parent.parent.parent.parent / "data" / "teapot.usd"

class TeapotSpawn:
    def __init__(self) -> None:
        #print(TEAPOT_USD)
        omni.kit.commands.execute('CreateReference', 
        path_to=Sdf.Path('/World/teapot'),
        asset_path=str(TEAPOT_USD),
        usd_context=omni.usd.get_context()
        
        )
        
#Thank you Mati from Nvidia Omniverse Discord        
