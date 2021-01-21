
import os
import json
import pandas as pd
import numpy as np
import sys 


def load_configuration(file_name):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    with open(os.path.join(fileDir, "../Json/" + file_name + ".json")) as json_file:
        configuration = json.load(json_file)
    return configuration

def load_dataframe(config):
    path_data = config['data']
    df = pd.read_csv(path_data, sep = ',', header = None)

    print(df)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Error")
    else:
        # initialize
        config = load_configuration(sys.argv[1])
        load_dataframe(config)