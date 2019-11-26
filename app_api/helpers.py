import oauth2

APP_KEY = 'YOUR_APP_KEY'
APP_SECRET = 'YOUR_SECRET_KEY'

'''
	This function is used to hit twiiter API after auth. So pass your url of endpoint.
'''

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=APP_KEY, secret=APP_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=bytes(post_body, "utf-8"), headers=http_headers )
    return content