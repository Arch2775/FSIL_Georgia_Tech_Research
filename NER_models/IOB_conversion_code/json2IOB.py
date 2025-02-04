import json
import glob
import os
import sys
import csv

def get_paths(input_folder):
    """
    Stores all .json files in a list
    Returns a list of strings of filepaths from the input folder
    :param inputfolder: inputfolder used in main
    """
    list_files = []
    conll_folder = glob.glob(input_folder + '/*.json')
    
    for filename in conll_folder:
        list_files.append(filename)

    return list_files

def load_text(json_path):
    """
    Opens the container and reads the elements (JSON objects)
    Returns the loaded JSON content
    :param json_path: list with filepaths
    """
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json_file.read()
        content = json.loads(data)
    
    return content

def process_and_write(loaded_dicts, input_folder, json_path):
    """
    Process each JSON and write to CoNLL file in IOB format
    :param loaded_dicts: content of json file
    :param input_folder: folder with json files
    :param json_path: pathname of json file
    """
    directory = 'test-dir'
    
    # Check if dir exists, if not make one
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Get basename of path and change extension to '.conll'
    base = os.path.basename(json_path)[:-5]
    conll_str = '.conll'
    basename = base + conll_str
    
    # Add directory with files to the input folder
    path = os.path.join(directory, basename)
    
    # Open write file
    with open(path, 'w', encoding='utf-8') as f:
        for item in loaded_dicts:
            for annotation in item.get('annotations', []):
                # Create a dictionary to keep track of entities within a sentence
                entity_dict = {}
                for result in annotation.get('result', []):
                    value = result.get('value', {})
                    text = value.get('text', '')
                    label = ','.join(value.get('hypertextlabels', []))
                    if text and label:
                        # Split the text into words
                        words = text.split()
                        for i, word in enumerate(words):
                            if i == 0:  # First word of entity
                                entity_dict[word] = "B-" + label
                            else:  # Subsequent words in the same entity
                                entity_dict[word] = "I-" + label
                        for word in entity_dict:
                            f.write(f"{word} {entity_dict[word]}\n")
                f.write("\n")  # Separate different annotations with a new line

def main():
    input_folder = sys.argv[1]
    
    json_paths = get_paths(input_folder)
    for json_path in json_paths:
        loaded_dicts = load_text(json_path)
        process_and_write(loaded_dicts, input_folder, json_path)

if __name__ == "__main__":
    main()

# to run:- python json2IOB.py json_folder_name

