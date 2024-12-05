import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def fill_values(tests, values_dict):
    if isinstance(tests, dict):
        if 'id' in tests and tests['id'] in values_dict:
            tests['value'] = values_dict[tests['id']]
        if 'values' in tests:
            for sub_test in tests['values']:
                fill_values(sub_test, values_dict)
    elif isinstance(tests, list):
        for item in tests:
            fill_values(item, values_dict)

def main(values_path, tests_path, report_path):
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_dict)

    save_json(tests_data, report_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Введите: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    main(values_path, tests_path, report_path)
