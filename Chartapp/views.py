from django.shortcuts import render
from .models import Account
import requests
import re
from bs4 import BeautifulSoup
from etherscan import Etherscan


def index(request):
    Account.delete_everything(self=Account)
    eth = Etherscan("QD73SVAYFQ8DFYFRDI3G6QVV74KG1EW1K4")
    data = []
    balance = []
    for i in range(4):
        url = "https://etherscan.io/accounts/%s"
        new_url = url %(i + 1)
        cookies = dict(BCPermissionLevel='PERSONAL')
        req = requests.get(new_url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies)
        soup = BeautifulSoup(req.content, 'html.parser')
        temp = soup.find_all('a', href=re.compile("/address/"))
        for i in temp:
            data.append(i.get('href'))
        data.pop()
    cnt = 0
    for i in data:
        data[cnt] = i[9:]
        cnt += 1
    cnt2 = 0

    for j in data:
        bal = eth.get_eth_balance(j)
        balance.append(float(bal) / 1000000000000000000)
    for k in range(0, 100):
        Account.save(Account.objects.create(address=data[k], balance=balance[k]))
    accounts = Account.objects.all()
    context = {
        "accounts": accounts
    }
    return render(request, 'Chartapp/index.html', context)
