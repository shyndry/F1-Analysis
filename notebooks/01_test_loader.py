import sys
sys.path.append(".")
import src.data_loader as loader

loader.setup_cache("data/cache")
test_session = loader.load_session(2024, "Bahrain", "R")
test_driver = loader.get_all_drivers(test_session)
test_laps_ham = loader.get_driver_laps(test_session, "HAM")
test_best_laps_ham = loader.get_driver_best_lap(test_session, "HAM")

print(f"La gara: {test_session}")
print(f"I piloti: {test_driver}")
print(f"I giri di Hamilton: {test_laps_ham}")
print(f"Il miglior giro di Hamilton è: {test_best_laps_ham}")