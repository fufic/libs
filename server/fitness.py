import zero_messeger.zero_messeger as zm
import json

def handle(reqData):
    try:
        params= {}
        params['intent'] = reqData['queryResult']['intent']['displayName']
        if params['intent'] == 'set_weight':
            params['val'] = str(reqData['queryResult']['parameters']['number'])
            params['measure'] = reqData['queryResult']['parameters']['measurement']
            resp = sender.Send(json.dumps(params).encode())
            return params['measure'] + "set to" + params['val']  + "kg"
        elif params['intent'] == 'get_weight':
            params['date'] = str(reqData['queryResult']['parameters']['date'])
            params['measure'] = reqData['queryResult']['parameters']['measurement']
            resp = sender.Send(json.dumps(params).encode())
            data = json.loads(resp)
            print(data)
            return params['measure'] + " is " + str(data['weight'])  + "kg"
    except:
        return "error"
    
sender = zm.Sender('tcp://127.0.0.1:8088')
