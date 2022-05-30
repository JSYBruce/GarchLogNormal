# -*- coding: utf-8 -*-
"""
Created on Mon May 16 13:59:27 2022

@author: BruceKing
"""
from DoubleNormal import LogNormal
from Model import ARCHModel
from Garch import GARCH
from ArchResult import ARCHModelResult
import pickle
import numpy as np
import pandas as pd

def runModel(data_file_name):
    with open(data_file_name, 'rb') as f:
            coin_df = pickle.load(f).dropna()
    #coin_df = pd.read_pickle('BTC_skewtmixg')
    #df = pd.read_excel(data_file_name, header=None, names = ["bas"])
    archmodel = ARCHModel(y = coin_df.AR * 100, distribution = LogNormal(), volatility = GARCH())
    result = archmodel.fit(starting_values=[2, 0.23763582, 0.2    ,0.2])
    result = ARCHModelResult(result[0], None,  result[1],  result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12])
    return result
    
