import json
from types import SimpleNamespace

with open('myfile.json', 'r', encoding='utf-8') as f:
    x = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    print(x.house, x.locality, x.landmark, x.area, x.city, x.state, x.country, x.pin_code)