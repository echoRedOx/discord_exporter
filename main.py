import json
import os
import sys
from classes import Conversation


def get_data(filepath:str):
    with open(filepath, 'r') as file:
        data = json.load(file)
    
    return data


def main(data_folder, output_dir):
    for filename in os.listdir(data_folder):
        if filename.endswith('json'):
            filepath = os.path.join(data_folder, filename)
            docname, ext = os.path.splitext(filename)
            data = get_data(filepath=filepath)
            conversation = Conversation(data=data)
            output_path = f"{output_dir}/{docname}"
            conversation.export_to_txt(output_path=output_path + '.txt')
            conversation.export_to_csv(output_path=output_path + '.csv')
            conversation.export_to_yaml(output_path=output_path + '.yaml')


if __name__ == "__main__":
    data_folder = sys.argv[1]
    output_dir = sys.argv[2]
    main(data_folder=data_folder, output_dir=output_dir)