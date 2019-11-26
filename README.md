# Twitter API 2019 with Django

Recently Twitter made some changes into their API. I made this django project with custom functions so you don't need any third party library to hit twitter. I used twython library only for auth process. 
## Installation

Create virtual environment and install requirements file.

```bash
pip install requirements.tx
```

## Important changes

```python

APP_KEY = 'YOUR_APP_KEY'
APP_SECRET = 'YOUR_SECRET_KEY'
callback_url='https://example.com/complete/twitter/'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
