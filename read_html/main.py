import pandas as pd
import requests
from io import StringIO

url = "https://pl.wikipedia.org/wiki/Miasta_w_Polsce"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
print(response.status_code)

html = response.text

data = pd.read_html(StringIO(html), header=0)

print(data[0])
print(data[1])