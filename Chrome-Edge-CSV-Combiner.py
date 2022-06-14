import os
import glob
import pandas as pd

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)

combined_csv.dropna().to_csv("Synced.csv", index=False, encoding='utf-8-sig')
