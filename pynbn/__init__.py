import requests
import json

baseurl = 'https://data.nbn.org.uk'

class Connection:
    'pynbn connection to the NBN server'
    def __init__(self, session):
        'session - session object from requests'
        self.session = session

    def get_observations(self, tvks=[], start_year=1990, end_year=2010, dataset=None):
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
        if (dataset is not None):
            url += 'datasetKey=%s&' % dataset
        url += 'startYear=%d&' % start_year
        url += 'endYear=%d' % end_year
        #print(url)
        r = self.session.get(url)
        #print r.text
        if r.status_code != 200:
            print("Server status code: %d." % r.status_code)
            print("Printing server response:")
            print(r.text)
            #return []
        try:
            jsondata = json.loads(r.text)
        except ValueError:
            print("Unable to turn result from server into json")
            print("Printing server response:")
            print(r.text)
            return []
        return jsondata
        #print(r.text)

    def get_ancestry(self, tvk):
        """Details of ancestry
        
        :param tvk: a single code, e.g. 'NBNSYS0000007094'
   
        :returns json info about the species"""
        
        #TODO put together URL with urlliby function
        url = '/'.join([baseurl, 'api', 'taxa',tvk]) 

        #print(url)
        r = self.session.get(url)
        return json.loads(r.text)
        
    def get_species_in_group(self, grp):
        """?
        
        :param tvk: a single code, e.g. 'NBNSYS0000007094'
   
        :returns ...?"""
        
        #TODO put together URL with urlliby function
        url = '/'.join([baseurl, 'api', 'taxa?']) 
        url += 'taxonOutputGroupKey=%s&rows=5000' % grp
        
        #print(url)
        r = self.session.get(url)
        return json.loads(r.text)
        
    def get_tvk(self,query):
        """Get TVK code for a species ??
        
        :param species_name: name of the species"""
        
        #TODO put together URL with urlliby function
        url = '/'.join([baseurl, 'api', 'search/taxa?q=',query]) 

        #print(url)
        r = self.session.get(url)
        return json.loads(r.text)        
        
        
    
def connect(username, password):
    #print("Trying to log in")
    session = requests.session()
    p = session.post('https://data.nbn.org.uk/User/SSO/Login', data = {'username':username, 'password':password})   
    whoami = session.get('https://data.nbn.org.uk/api/user') #check if we're logged in
    #print(whoami.text)
    #print("Connected")
    #TODO CHECK IF IT WORKED
    return Connection(session)
    

