#!/usr/bin/env python3

import pandas as pd
import os
import numpy as np

# Define paths and filenames
data_p = os.path.join('D:/', 'data', 'ESS', '2018')
save_p = os.path.join('..', 'datasets')

inname = 'ESS2018DK.csv'
outname = 'ESS2018DK_subset.csv'

# Read in original data
df = pd.read_csv(os.path.join(data_p, inname))

# Define columns to keep
keep_columns = ['idno',
                'netustm',
                'ppltrst',
                'vote',
                'prtvtddk',
                'lvpntyr',
                'tygrtr',
                'gndr',
                'yrbrn',
                'edlvddk',
                'eduyrs',
                'wkhct',
                'wkhtot',
                'grspnum',
                'frlgrsp',
                'inwtm']

# Subset data: Only monthly pay frequency and specific columns
df_select = df.loc[df['infqbst'] == 'Monthly', keep_columns]

# Define dictionaries for recoding
missing_dict = {'Not applicable': np.nan, 'No answer': np.nan, 'Refusal': np.nan, 'Don\'t know': np.nan}
trst_dict = {'Most people can be trusted': '10', 'You can\'t be too careful': '0'}

# List of columns to convert to numeric
numeric_cols = ['netustm', 'ppltrst', 'eduyrs', 'wkhct', 'grspnum', 'frlgrsp']

# Perform recoding and numeric coercion
for col in df_select:
    
    if df_select[col].dtypes == 'object':

        df_select[col] = df_select[col].replace(missing_dict)

        if col == 'ppltrst':
            df_select[col] = df_select[col].replace(trst_dict)

        if col in numeric_cols:
            df_select[col] = df_select[col].astype('float')

# Save data
df_select.to_csv(os.path.join(save_p, outname), index = False)