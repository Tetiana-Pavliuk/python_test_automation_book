steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"]  # duplicate steps

test_scenarios = {
    "test_case_1": frozenset(steps_1),
    "test_case_2": frozenset(steps_2),
    "test_case_3": frozenset(steps_3)
}


def check_scenario_exists(test_case_name, test_scenarios):
    if test_case_name in test_scenarios:
        print(f"Scenario '{test_case_name}' already exists.")
    else:
        print(f"Scenario '{test_case_name}' does not exist.")


# Check if certain scenarios exist
print(check_scenario_exists("test_case_1", test_scenarios))
print(check_scenario_exists("test_case_2", test_scenarios))
print(check_scenario_exists("test_case_4", test_scenarios))
