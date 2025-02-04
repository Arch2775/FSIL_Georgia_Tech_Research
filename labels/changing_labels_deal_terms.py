import json
import os

JSON_PATH: str = r'C:\Users\archishman vb\OneDrive\Desktop\FSIL-GA-Tech\Round-2\archishmanvb27@gmail.com.json' # TODO
OLD_NEW_NAME_PAIRS: dict = {'': 'Date', 
                            '': 'Date Type', 
                            '': 'Deal Class', 
                            '': 'Deal Sub-Class', 
                            '': 'Amount Type', 
                            '': 'Amount Value', 
                            '': 'Principal of Value', 
                            '': 'Fee Type', 
                            '': 'Fee Value', 
                            '': 'Fee Principal of Value', 
                            '': 'Fee Condition', 
                            '': 'Loan Amount Type', 
                            '': 'Loan Amount Value', 
                            '': 'Loan Principal of Value', 
                            '': 'Loan Amount Condition', 
                            '': 'Spread Index', 
                            '': 'Spread Type', 
                            '': 'Spread Value', 
                            '': 'Spread Condition'
                           } # TODO


def change_labels(file_path: str, old_new_name_pairs: dict) -> None:
    with open(file_path, 'r') as file:
        data = json.load(file)

    for task in data:
        for annotation in task['annotations']:
            for result in annotation['result']:
                old_labels = result['value']['hypertextlabels']
                new_labels = []
                for old_label in old_labels:
                    new_labels.append(old_new_name_pairs[old_label])
                result['value']['hypertextlabels'] = new_labels

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def main() -> None:
    change_labels(JSON_PATH, OLD_NEW_NAME_PAIRS)


if __name__ == '__main__':
    main()

