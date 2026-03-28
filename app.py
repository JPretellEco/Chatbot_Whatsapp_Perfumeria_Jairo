from flask import Flask, request
import os
import util
import whatsappservice

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


@app.route('/welcome', methods=['GET'])
def index():
    return 'Perfumería Bot Activo 🌸'


# 🔐 Verificación webhook
@app.route('/whatsapp', methods=['GET'])
def verify_token():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge
    return "Error de verificación", 403


# 📩 Recepción mensajes
@app.route('/whatsapp', methods=['POST'])
def receive_message():
    try:
        body = request.get_json()

        entry = body.get("entry", [])[0]
        changes = entry.get("changes", [])[0]
        value = changes.get("value", {})

        messages = value.get("messages")

        if not messages:
            return "EVENT_RECEIVED"

        message = messages[0]
        number = message.get("from")

        text = util.GetTextUser(message)
        print("Cliente:", text)

        generate_response(text, number)

        return "EVENT_RECEIVED"

    except Exception as e:
        print("ERROR:", e)
        return "EVENT_RECEIVED"


# 🧠 Lógica del negocio
def generate_response(text, number):
    text = text.lower()

    # 👋 Bienvenida
    if "hola" in text or "buenas" in text:
        data = util.TextMessage(
            "🌸 ¡Hola! Bienvenido a nuestra perfumería\n\n"
            "Puedes preguntarme por:\n"
            "💰 precios\n"
            "🧴 perfumes disponibles\n"
            "🚚 envío\n"
            "📍 ubicación",
            number
        )

    # 🧴 Catálogo
    elif "perfumes" in text or "catalogo" in text:
        data = util.TextMessage(
            "🧴 Tenemos:\n\n"
            "• Dior Sauvage\n"
            "• Chanel No.5\n"
            "• Bleu de Chanel\n"
            "• Versace Eros\n\n"
            "Escríbeme el nombre para ver el precio 😉",
            number
        )

    # 💰 Precios
    elif "precio" in text:
        data = util.TextMessage(
            "💰 Precios referenciales:\n\n"
            "• Dior Sauvage → S/350\n"
            "• Chanel No.5 → S/420\n"
            "• Versace Eros → S/300\n\n"
            "Pregunta por uno específico 👀",
            number
        )

    # 🚚 Envío
    elif "envio" in text or "delivery" in text:
        data = util.TextMessage(
            "🚚 Envíos:\n\n"
            "• Trujillo → S/10\n"
            "• Provincias → S/20\n\n"
            "Tiempo: 24-48 horas ⏳",
            number
        )

    # 📍 Ubicación
    elif "ubicacion" in text or "donde" in text:
        data = util.LocationMessage(number)

    # 🙏 Gracias
    elif "gracias" in text:
        data = util.TextMessage(
            "🙏 ¡Gracias a ti! Estamos para ayudarte 🌸",
            number
        )

    # 🤖 Default
    else:
        data = util.TextMessage(
            "🤖 No entendí bien.\n\n"
            "Puedes escribir:\n"
            "• perfumes\n"
            "• precios\n"
            "• envío\n"
            "• ubicación",
            number
        )

    send_message(data)


# 📤 Envío
def send_message(data):
    try:
        whatsappservice.SendMessageWhatsapp(data)
    except Exception as e:
        print("ERROR ENVÍO:", e)


if __name__ == "__main__":
    app.run(debug=True)