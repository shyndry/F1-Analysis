import fastf1
from fastf1.core import DriverResult, Laps
import pandas as pd

from pathlib import path

def setup_cache( path: str ) -> None: 

    folder = Path (path)
    folder.mkdir(parents = True, exist_ok = True)
    fastf1.Cache.enable_cache(folder)

    print(f" La cache è stata attivata dentro: {path}, correttamente")


def load_session( year: int, gp: str, session_type: str) -> fastf1.core.Session: 
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    return session

def get_all_drivers(session: fastf1.core.Session ) -> list[str]:
    driver = session.laps["Driver"]
    unici = driver.unique()
    return sorted(unici.to_list())

def get_driver_laps(session: fastf1.core.Session, driver_code: str) -> pd.DataFrame:
    driver_lap = session.laps.pick_driver(driver_code)
    return driver_lap
    
def get_driver_best_lap (session: fastf1.core.Session, driver_code: str) -> pd.Series:
    best_driver_lap =session.laps.pick_driver(driver_code).pick_fastest()
    return best_driver_lap


