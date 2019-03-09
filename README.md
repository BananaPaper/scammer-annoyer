# **Scammer Annoyer**


## Installation
```bash
git clone https://github.com/BananaPaper/scammer-annoyer.git
```

## Preparation
**Change, Add or Delete** request parameters to match the fake website **form data**.

#### Example
```Python
requests.post(url, allow_redirects=False, data={
    'phoneNumber': number,
    'login' : login,
    'pw': code
})
```

##### With submit button
```Python
requests.post(url, allow_redirects=False, data={
    'id': number,
    'pw': code,
    'submit': 'Send'
})
```


## Usage

```
python antiScam.py

Enter fake form url : http://totallylegitbank.fake
How many times : 1000000
```

```
1 - Sending id: (7293571981) and password: (615437) to http://totallylegitbank.fake form
2 - Sending id: (9452397203) and password: (485670) to http://totallylegitbank.fake form
3 - Sending id: (1485746714) and password: (544674) to http://totallylegitbank.fake form
4 - Sending id: (8869053810) and password: (964936) to http://totallylegitbank.fake form
5 - Sending id: (4847143096) and password: (825045) to http://totallylegitbank.fake form
...
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
