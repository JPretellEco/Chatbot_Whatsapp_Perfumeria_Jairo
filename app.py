from flask import Flask, request
import os
import util
import whatsappservice

app = Flask(__name__)

# 🔐 Variables de entorno
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


@app.route('/welcome', methods=['GET'])
def index():
    return 'welcome developer'


# ✅ Verificación del webhook
@app.route('/whatsapp', methods=['GET'])
def verify_token():
    try:
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return challenge
        return "Token inválido", 403

    except Exception as e:
        print("ERROR VERIFY:", e)
        return "Error", 500


# ✅ Recepción de mensajes
@app.route('/whatsapp', methods=['POST'])
def receive_message():
    try:
        body = request.get_json()
        print("BODY:", body)  # 🔍 debug clave

        entry = body.get("entry", [])[0]
        changes = entry.get("changes", [])[0]
        value = changes.get("value", {})

        messages = value.get("messages")

        # 🔒 Evita errores cuando no hay mensajes (status updates)
        if not messages:
            return "EVENT_RECEIVED"

        message = messages[0]
        number = message.get("from")

        text = util.GetTextUser(message)
        print("MENSAJE:", text)

        generate_message(text, number)

        return "EVENT_RECEIVED"

    except Exception as e:
        print("ERROR POST:", e)
        return "EVENT_RECEIVED"


# 🧠 Lógica principal
def generate_message(text, number):
    text = text.lower()

    if "hola" in text:
        data = util.TextMessage("👋 Hola, ¿cómo puedo ayudarte?", number)

    elif "gracias" in text:
        data = util.TextMessage("🙏 Gracias por escribir.", number)

    elif "menu" in text or "opciones" in text:
        data = util.ListMessage(number)

    elif "imagen" in text:
        data = util.ImageMessage(number)

    elif "video" in text:
        data = util.VideoMessage(number)

    elif "documento" in text:
        data = util.DocumentoMessage(number)

    elif "audio" in text:
        data = util.AudioMessage(number)

    elif "ubicacion" in text:
        data = util.LocationMessage(number)

    elif "boton" in text:
        data = util.BotonesMessage(number)

    else:
        data = util.TextMessage(f"Echo: {text}", number)

    send_message(data)


# 📤 Envío centralizado
def send_message(data):
    try:
        response = whatsappservice.SendMessageWhatsapp(data)

        if not response:
            print("❌ Error enviando mensaje")

    except Exception as e:
        print("ERROR SEND:", e)


# 🚀 Producción
if __name__ == "__main__":
    app.run(debug=True)