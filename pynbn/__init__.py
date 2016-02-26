import requests

baseurl = 'https://data.nbn.org.uk'

class Connection:
    'pynbn connection to the NBN server'
    
    def __init__(self, session):
        'session - session object from requests'
        self.session = session

    def getObservations(self):
        print "getObs" #TODO put together URL with urlliby function
        url = '/'.join([baseurl, 'api', 'taxonObservations?']) 
        tvks = ['NBNSYS0000007094','NBNSYS0000007095']
        for tvk in tvks:
            url += 'ptvk=%s&' % tvk
        #can't use params parameter as requests can't handle duplicate keys. The server can't handle commar seperated keys.
        url += 'datasetKey=SGB00001&'
        url += 'startYear=1990&' 
        url += 'endYear=2010'
        print url
        r = self.session.get(url)
        print r.text
    
def connect(username, password):
    print "Trying to log in"
    session = requests.session()
    p = session.post('https://data.nbn.org.uk/User/SSO/Login', data = {'username':username, 'password':password})
    #print 'headers', p.headers
    #print 'cookies', requests.utils.dict_from_cookiejar(session.cookies)
    #print 'html',  p.text
    #r = requests.post('https://data.nbn.org.uk/User/SSO/Login', data = {'username':username, 'password':password})
    #for h in r.headers:
    #    print(h)
    #for c in r.cookies:
    #    print(c)
    print("Connected")
    #TODO CHECK IF IT WORKED
    return Connection(session)
    

