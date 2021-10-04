from requests.auth import HTTPBasicAuth
import requests
import configparser

# Read local file `config.ini`.
config = configparser.ConfigParser()
config.read("config.ini")

if __name__ == '__main__':
    client_id = config.get('GRAVITEE', 'CLIENTID')
    client_secret = config.get('GRAVITEE', 'CLIENTSECRET')

    token_url = config.get('GRAVITEE', 'GATEWAY') + 'oauth/token'
    revoke_url = config.get('GRAVITEE', 'GATEWAY') + 'oauth/revoke'
    introspection_url = config.get('GRAVITEE', 'GATEWAY') + 'oauth/introspect'

    # Get Token
    d = {'grant_type': 'client_credentials'}

    auth = HTTPBasicAuth(client_id, client_secret)
    t = requests.post(url=token_url,
                      auth=auth,
                      data=d
                      ).json()
    print("Token: " + t["access_token"])

    # Introspect
    d = {'token': t["access_token"]}
    i = requests.post(url=introspection_url,
                      auth=auth,
                      data=d
                      )
    print("Introspection is active token: " + str(i.json()['active']))
    print(i.text)

    # Revoke
    r = requests.post(url=revoke_url,
                      auth=auth,
                      data=d
                      )
    print("Revoke : ")
    print("HTTTP " + str(r.status_code))
    print(r.text)

    # Introspect
    d = {'token': t["access_token"]}
    i = requests.post(url=introspection_url,
                      auth=auth,
                      data=d
                      )
    print("Introspection is active token: " + str(i.json()['active']))
    print(i.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
