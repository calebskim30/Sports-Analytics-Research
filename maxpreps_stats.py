import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import numpy as np

test_url = 'https://production.api.maxpreps.com/gatewayweb/react/team-season-player-stats/rollup/v1?teamId=cb3c4816-4749-4381-8c4c-5613ef8c89c9&sportSeasonId=77be7c75-cdf9-483d-867f-ea2af557e731'
url_json = requests.get(url=test_url).json()

'''normalized
df_normal = pd.json_normalize(url_json)
print(df_normal)
'''

print(url_json)