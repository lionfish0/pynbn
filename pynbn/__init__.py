import requests
import json

baseurl = 'https://data.nbn.org.uk'

class Connection:
    'pynbn connection to the NBN server'
    
    def __init__(self, session):
        'session - session object from requests'
        self.session = session

    def get_observations(self, tvks=[], start_year=1990, end_year=2010):
        """Get species observations
        
        :param tvks: list of speicies codes, e.g. ['NBNSYS0000007094','NBNSYS0000007095']
        :param startYear: default 1990
        :param endYear: default 2010
        
        :returns json list of observations"""
        
        #TODO put together URL with urlliby function
        url = '/'.join([baseurl, 'api', 'taxonObservations?'])

        for tvk in tvks:
            url += 'ptvk=%s&' % tvk
        #can't use params parameter as requests can't handle duplicate keys. The server can't handle commar seperated keys.
        url += 'datasetKey=SGB00001&'
        url += 'startYear=%d&' % start_year
        url += 'endYear=%d' % end_year
        #print(url)
        r = self.session.get(url)
        return json.loads(r.text)
        #print(r.text)

    def get_ancestry(self, tvk):
        """Details of ancestry (don't know what this does yet).
        
        :param tvk: a single code, e.g. 'NBNSYS0000007094'
   
        :returns json info about the species"""
        
        #TODO put together URL with urlliby function
        url = '/'.join([baseurl, 'api', 'taxa',tvk]) 

        print(url)
        r = self.session.get(url)
        return json.loads(r.text)
        
    def get_tvk(self,species_name):
        """Get TVK code for a species
        
        :param species_name: name of the species"""
        
    
def connect(username, password):
    print("Trying to log in")
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
    

