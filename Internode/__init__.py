"""Abstraction of the Internode API"""
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import Timeout
from xml.etree import ElementTree

class api:

    def __init__(self, username, password):
        self.Error = None
        self.url = 'https://customer-webtools-api.internode.on.net/api/v1.5'  
        api_adapter = HTTPAdapter(max_retries=2)
        
        """Create a session and perform all requests in the same session"""
        session = requests.Session()
        session.mount(self.url, api_adapter)
        session.headers.update({'Accept': 'application/json', 'User-Agent': 'Internode.py', 'Accept-Encoding' : 'gzip, deflate, br', 'Connection' : 'keep-alive' })
        self.session = session

        """Get ServiceAgreementID"""
        try:
            self.auth = (username, password)
            auth = self.session.get(self.url, auth=self.auth, timeout=(2, 5))
            xml = ElementTree.fromstring(auth.content)
            error = xml.find('error/msg')

            if (error is None):
                """Get ServiceAgreementID"""
                servicexml = xml.find('api/services/service')
                self.serviceAgreementID = servicexml.text
            else:
                self.Error = 'Auth request failed: ' + error.text
        except Timeout:
            self.Error = 'Auth request timed out'

    def request(self, type): 
        try:
            request = self.session.get(self.url + '/' + self.serviceAgreementID + '/' + type, auth=self.auth)
            requestxml = ElementTree.fromstring(request.content)

            error = requestxml.find('error/msg')
            if (error is None):
                return request
            else:
                self.Error = 'Data request failed: ' + request.reason  
        except Timeout:
            self.Error = 'Data request timed out'

    def getservice(self):
        servicedata = self.request('service')
        self.service = servicedata.text

    def getusage(self):
        usagedata = self.request('usage')
        tree = ElementTree.fromstring(usagedata.content)
        usagexml = tree.find('api/traffic')
        usage = float(usagexml.text)/1000000000
        self.usage = "{:.2f}".format(usage)
        self.rollover = usagexml.get('rollover')
        self.planinterval = usagexml.get('plan-interval')
        self.quota = float(usagexml.get('quota'))/1000000000

    def gethistory(self):
        historydata = self.request('history')
        tree = ElementTree.fromstring(historydata.content)
        historyxml = tree.find('api/usagelist/usage/traffic')
        history = float(historyxml.text)/1000000000
        self.history = "{:.2f}".format(history)