# Django parsing with api https://docs.etherscan.io/ to create bar, pie and line charts.
This project was created as the assignment 2 for the Advanced Programming 2 course. 
It is a website where you can see Top-100 accounts on https://etherscan.io/accounts/ in 3 different charts such as Bar chart, Line Chart, Pie Chart. 
Connected database: PostgreSQL

### Installation
Copy from source
```bash
git clone https://github.com/Assylken/DjangoAss2.git
```

### Usage

```
from django.shortcuts import render
import requests
import re
from bs4 import BeautifulSoup
from etherscan import Etherscan
```

### Examples
Bar chart example: <br />
<img src="/images/bar.png" width="600" height="300"/> <br />
Pie chart example: <br />
<img src="/images/pie.png" width="600" height="300"/> <br />
Line chart example: <br />
<img src="/images/line.png" width="600" height="300"/>
