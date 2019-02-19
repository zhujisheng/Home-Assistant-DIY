"""
This is the HomeAssistant Client for voice_assistant.
Only complete the service call and conversation api.
"""

import requests

class ha_cli(object):
    def __init__(self, token, base_url='http://localhost:8123', verify=False):
        assert base_url[-1] != '/'
        self._base_url = base_url

        self._session = requests.Session()
        self._session.verify = verify
        self._session.headers = {
            'Authorization': 'Bearer '+ token,
            'Content-Type': 'application/json'
            }


    def process(self, input_sentence):
        data = {'text': input_sentence}
        url = self._base_url + '/api/conversation/process'

        r = self._session.post(url=url, json = data)
        ouput_sentence = r.json()['speech']['plain']['speech']

        return(ouput_sentence)


    def call_service(self, domain, service, data=None):
        url = self._base_url + '/api/services/' + domain + '/' + service
        r = self._session.post(url = url, json = data)
        return


    def speak(self, sentence, tts='google_say', media_player='all'):
        data = { 'message': sentence,
                 'entity_id': media_player
                 }
        self.call_service( 'tts',
                           tts,
                           data
                           )
        return


    def note(self, message='', title='不能理解的语音命令'):
        data = { 'message': message,
                 'title': title
                 }
        self.call_service( 'persistent_notification',
                           'create',
                           data
                           )
        return
