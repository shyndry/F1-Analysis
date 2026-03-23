import fastf1
import pandas as pd

from pathlib import path

def setup_cache( path: str ) -> None: 

    folder = Path (path)
    folder.mkdir(parents = True, exist_ok = True)
    fastf1.Cache.enable_cache(folder)

    print(f" La cache è stata attivata dentro: {path}, correttamente")


