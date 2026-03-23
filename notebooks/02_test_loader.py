import sys
sys.path.append(".")
import src.data_loader as loader

loader.setup_cache("data/cache")
test_session = loader.load_session(2024, "Bahrain", "R")
test_laps_ham = loader.get_driver_laps(test_session, "HAM")

print(f"La gara: {test_session}")
print(f"I giri di Hamilton: {test_laps_ham[["LapTime", "TyreLife", "Compound"]]}")