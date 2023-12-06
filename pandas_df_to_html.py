


import pandas as pd
data = [(1, 'aa', '2020-01-01'), (2, 'bb', '2021-01-01'), (3, 'cc', '2021-12-01')]
dataDF = pd.DataFrame(data, columns=['id', 'name', 'login_date'])

dataDF.to_html('C:\km\km_test_html.html', index=False, col_space=100, justify="center")
dataDF.to_html('C:\km\km_test_html.html', index=False, col_space=[20, 30, 200])
-->justify: for header row only

dataDF.to_html('C:\km\km_test_html.html', col_space=[20, 30, 200], index=False, formatters={'name': lambda x: '\<b\>' + x + '\</b\>'})
--> TO FIX: writing this to: <b>aa</b>
