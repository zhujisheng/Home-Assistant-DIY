"""
This is the client to public AIs' API for voice_assistant.
"""

import requests

class tuling123(object):
    def __init__(self, user_id, api_key, base_url='http://openapi.tuling123.com/openapi/api/v2'):
        self._session = requests.Session()

        self._base_url = base_url
        self._base_data = { 'reqType': 0,
                            'userInfo': {
                                'apiKey': api_key,
                                'userId': user_id
                                },
                            'perception': {
                                'inputText': {
                                    'text': ''
                                    }
                                }
                            }


    def command(self, input_sentence):
        data = self._base_data
        data['perception']['inputText']['text'] = input_sentence

        r = self._session.post(url=self._base_url, json = data)
        output = r.json()

        ouput_sentence = None
        for result in output['results']:
            if result['resultType']=='text':
                ouput_sentence = result['values']['text']
                break

        return(ouput_sentence)
