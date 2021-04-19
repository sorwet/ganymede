import configparser, quinnat

config = configparser.ConfigParser()
config.read('default.ini')

urbitUrl = config['URBIT']['urbitUrl']
urbitId = config['URBIT']['urbitId']
urbitCode = config['URBIT']['urbitCode']
urbitChat = config['URBIT']['urbitChat']
urbitHost = config['URBIT']['urbitHost']
urbitClient = quinnat.Quinnat(urbitUrl, urbitId, urbitCode)

messageWelcome = config['MESSAGES']['messageWelcome']
messageAck = config['MESSAGES']['messageAck']

urbitClient.connect()

urbitClient.post_message(urbitHost, urbitChat, {"text": messageWelcome})

def dot_ack(message, replier):
    if 1 == len(message.full_text):
        replier({"mention": "~" + message.author})
        replier({"text": messageAck})

urbitClient.listen(dot_ack)
