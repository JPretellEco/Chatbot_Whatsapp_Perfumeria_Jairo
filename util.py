def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"]["body"])
    elif typeMessage == 'interactive':
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        
        if typeInteractive == 'button_reply':
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == 'list_reply':
            text = (interactiveObject["list_reply"])["title"]
        else:
            print('sin mensaje')
    else:
        print("sin message")

    return text

def TextMessage(text,number):
    data =  {
                "messaging_product": "whatsapp",    
                "to": number,
                "type": "text",
                "text": {
                    "body": text
                }
            }
    return data


def TextFormatMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": "*Hola causa* - _Hola causa_ - ```Hola causa```"
        }
    }
    return data

def ImageMessage(number):
    data = {
    "messaging_product": "whatsapp",    
    "to": number,
    "type": "image",
    "image": {
        "link": "https://ascenty.com/wp-content/uploads/2023/04/1169640_Ascenty_BLOG1-1920x1000-c-default.png"
    }
            }
    return data

def AudioMessage(number):
    data = {
    "messaging_product": "whatsapp",    
    "to": number,
    "type": "audio",
    "audio": {
        "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
    }}
    return data

def VideoMessage(number):
    data = {
    "messaging_product": "whatsapp",    
    "to": "51929796785",
    "type": "video",
    "video": {
        "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4",
        "caption": "Video"
    }}
    return data

def DocumentoMessage(number):
    data = {
    "messaging_product": "whatsapp",    
    "to": "51929796785",
    "type": "document",
    "document": {
        "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf",
        "caption": "Udemy document"
    }}
    return data


def LocationMessage(number):
    data = {
    "messaging_product": "whatsapp",    
    "to": number,
    "type": "location",
    "location": {
        "latitude": "-8.145343029466018",
        "longitude":"-79.04987239929702",
        "name": "Mi hogar",
        "address": "Calle José Santos Chocano Mz.17 - Lt.10, Trujillo 13009"
    }}
    return data


def BotonesMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "51929796785",
    "type": "interactive",
    "interactive": {
        "type": "button",
        "body": {
            "text": "¿Confirmas tu registro?"
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "001",
                        "title": "Oh, me vengo."
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "002",
                        "title": "Oh, me voy."
                    }
                }
            ]
        }
    }
    }
    return data

def ListMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": "51929796785",
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ I have these options"
        },
        "footer": {
            "text": "Select an option"
        },
        "action": {
            "button": "See options",
            "sections": [
                {
                    "title": "Buy and sell products",
                    "rows": [
                        {
                            "id": "main-buy",
                            "title": "Buy",
                            "description": "Buy the best product your home"
                        },
                        {
                            "id": "main-sell",
                            "title": "Sell",
                            "description": "Sell your products"
                        }
                    ]
                },
                {
                    "title": "📍center of attention",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "Agency",
                            "description": "Your can visit our agency"
                        },
                        {
                            "id": "main-contact",
                            "title": "Contact center",
                            "description": "One of our agents will assist you"
                        }
                    ]
                }
            ]
        }
    } }
    return data