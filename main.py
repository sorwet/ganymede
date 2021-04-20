import configparser, logging, quinnat

config = configparser.ConfigParser()
config.read('default.ini')

urbitUrl = config['URBIT']['urbitUrl']
urbitId = config['URBIT']['urbitId']
urbitCode = config['URBIT']['urbitCode']
urbitChat = config['URBIT']['urbitChat']
urbitHost = config['URBIT']['urbitHost']
logFileName = config['LOGGING']['logFilename']

logging.basicConfig(filename=logFileName, filemode='w', level=logging.INFO, format='[%(asctime)s] %(message)s')

urbitClient = quinnat.Quinnat(urbitUrl, urbitId, urbitCode)

messageWelcome = config['MESSAGES']['messageWelcome']
messageAck = config['MESSAGES']['messageAck']

logging.info('connecting to ~' + urbitId + ' @ ' + urbitUrl)
urbitClient.connect()

logging.info('sending welcome message "' + messageWelcome + '" to ' + urbitChat + ' @ ~' + urbitHost)
urbitClient.post_message(urbitHost, urbitChat, {"text": messageWelcome})

def dot_ack(message, replier):
    if 1 == len(message.full_text):
        logging.info('received dotpost "' + message.full_text + '" from ~' + message.author)
        logging.info('sending "' + messageAck + '" to ~' + message.author)
        replier({"mention": "~" + message.author})
        replier({"text": messageAck})

urbitClient.listen(dot_ack)
