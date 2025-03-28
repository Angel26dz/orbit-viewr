import pandas as pd
import os

#input_csv = 'orbit-viewer/PSCompPars_2024.09.30_17.09.44.csv'
output_json = 'orbit-viewer/PSCompPars_2024.09.30_17.09.44.json'

#os.makedirs('orbit-viewer', exist_ok=True)

#df = pd.read_csv(input_csv, skiprows=78)
#df.to_json(output_json, orient='records', lines=True)

df=pd.read_json(output_json , lines=True)
max_s_teff = df['st_teff'].dropna().max()
min_s_teff = df['st_teff'].dropna().min()

print(f"Máximo s_teff: {max_s_teff}")
print(f"Mínimo s_teff: {min_s_teff}")


