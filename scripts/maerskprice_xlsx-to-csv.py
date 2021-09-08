#!/usr/bin/env python3

import os
import pandas as pd

data_path = os.path.join("D:/", "data", "eikon")

maersk_df = pd.read_excel(os.path.join(data_path, "maerskb_price-history_01072021-01092021.xlsx"))
colnames = list(maersk_df.iloc[15, 0:9])
maersk_df = maersk_df.iloc[16:, 0:9].reset_index(drop = True)
maersk_df = maersk_df.set_axis(colnames, axis = 1, inplace = False)

maersk_df.to_csv(os.path.join(data_path, 'maerskb_price-history_01072021-01092021.csv'), index = False)