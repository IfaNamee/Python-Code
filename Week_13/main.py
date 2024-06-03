import webbrowser
webbrowser.open('https://docs.python.org/3/tutorial/index.html')
webbrowser.open('https://ifanamee.github.io/portfolio/javascript.html')

import requests
res = requests.get('https://ifanamee.github.io/portfolio')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])