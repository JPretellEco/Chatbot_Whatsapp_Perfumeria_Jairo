from flask import Flask,request
import util
import whatsappservice

app = Flask(__name__)
@app.route('/welcome',methods = ['GET'])
def index():
    return 'welcome developer'

@app.route('/whatsapp',methods = ['GET'])
def VerifyToken():

    try:
            
        accessToken = "3007884515151151515"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "",400
    except:
        return "",400
    

@app.route('/whatsapp',methods = ['POST'])
def ReceivedMessage():

    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry['changes'])[0]
        value = changes['value']
        message = (value["messages"])[0]
        number = message["from"]

        text = util.GetTextUser(message)
        GenerateMessage(text,number)
        print(text)

        return "EVENT_RECEIVED"
    except: 
        return "EVENT_RECEIVED"
    

def ProcessMessges(text,number):
    text = text.lower()

    if "Hola" in text:
        data = util.TextMessage("Hola,¿cómo puedo ayudarte?",number)
    elif "Gracias" in text:
        data = util.TextMessage("Gracias por contactarte conmigo",number)
    else:
        data = util.TextMessage("Perdóname, no logro comprenderte.")

    whatsappservice.SendMessageWhatsapp(data)


def GenerateMessage(text, number):

    text = text.lower()

    if "format" in text:
        data = util.TextFormatMessage(number)
    elif "image" in text:
        data = util.ImageMessage(number)
    elif "video" in text:
        data = util.VideoMessage(number)
    elif "document" in text:
        data = util.DocumentoMessage(number)
    elif "audio" in text:
        data = util.AudioMessage(number)
    elif "location" in text:
        data = util.LocationMessage(number)
    elif "button" in text:
        data = util.BotonesMessage(number)
    elif 'list' in text:
        data = util.ListMessage(number)
    else:
        data = util.TextMessage("Echo: " + text, number)

    whatsappservice.SendMessageWhatsapp(data)

    
if __name__ == "__main__":
    app.run()