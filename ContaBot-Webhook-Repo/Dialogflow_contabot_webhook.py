from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Contabot Webhook está corriendo correctamente 🚀"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    if intent == "SOLICITAR_FACTURA":
        respuesta = {"fulfillmentText": "Claro, envíame tu RFC y razón social para continuar."}
    else:
        respuesta = {"fulfillmentText": "Lo siento, no entendí tu solicitud."}

    return jsonify(respuesta)

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))