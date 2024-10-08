import requests
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

test_url = 'https://production.api.maxpreps.com/gatewayweb/react/team-season-player-stats/rollup/v1?teamId=cb3c4816-4749-4381-8c4c-5613ef8c89c9&sportSeasonId=77be7c75-cdf9-483d-867f-ea2af557e731'
url_json = requests.get(url=test_url).json()

df_dict = {}
for group_idx, group in enumerate(url_json['data']['groups']):
    group_dict = {}
    for subgroup in group['subgroups']:
        for row_idx, row in enumerate(subgroup['stats']['rows']):
            row_dict = {}
            for col_idx, col in enumerate(subgroup['stats']['columns']):
                header = col['displayName']
                value = row['columns'][col_idx]['value']
                row_dict[header] = value
            group_dict[row_idx] = row_dict
        df_dict[group_idx] = group_dict

df_list = []
for df in df_dict:
    df = pd.DataFrame(df_dict[df]).T
    df_list.append(df)
df_out = pd.concat(df_list)

#How to fix "NaN"?
print(df_out)