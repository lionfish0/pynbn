import requests

baseurl = 'https://data.nbn.org.uk'

class Connection:
    'pynbn connection to the NBN server'
    
    def __init__(self, session):
        'session - session object from requests'
        self.session = session

    def getObservations():
        path = '/'.join([baseurl, 'api', 'taxonObservations?']) 
        payload = {}
        payload['ptvk']
>>> r = requests.get('http://httpbin.org/get', params=payload)

        ptvk=NBNSYS0000007094&ptvk=NBNSYS0000172195&datasetKey=SGB00001&startYear=1990&endYear=2010
    
def connect(username, password):
    session = requests.session()
    p = session.post('https://data.nbn.org.uk/User/SSO/Login', data = {'username':username, 'password':password})
    print 'headers', p.headers
    print 'cookies', requests.utils.dict_from_cookiejar(session.cookies)
    #print 'html',  p.text
    #r = requests.post('https://data.nbn.org.uk/User/SSO/Login', data = {'username':username, 'password':password})
    #for h in r.headers:
    #    print(h)
    #for c in r.cookies:
    #    print(c)
    print("Connected")
    return 123
    

