
import os
import json
import pandas as pd
import numpy as np
import sys 

class Dataframe:
    def load_dataframe(self, config):
        path_data = config['data_path']
        df = pd.read_csv(path_data, sep = ',', header = 0)
        df['Date'] = pd.to_datetime(df['Date'], format = "%Y-%m-%d")

        return df

    def merge_vix(self, config, df_index):
        path_vix = config['path_vix']
        df_vix = pd.read_csv(path_vix, sep = ',', header = 0)
        df_vix['Date'] = pd.to_datetime(df_vix['Date'], format = "%Y-%m-%d")
        merge = pd.merge(df_index, df_vix, on = 'Date') # merge both index df and vix df

        return merge
        