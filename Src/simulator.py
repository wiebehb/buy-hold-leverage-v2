
import os
import json
import pandas as pd
import numpy as np
import sys 

from dataframe import Dataframe

def load_configuration(file_name):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    with open(os.path.join(fileDir, "../Json/" + file_name + ".json")) as json_file:
        configuration = json.load(json_file)
    return configuration

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Error")
    else:
        # initialize
        config = load_configuration(sys.argv[1])
        df = Dataframe()

        df_index = df.load_dataframe(config)

        df_merged = df.merge_vix(config, df_index)

        print(df_merged)