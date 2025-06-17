
# ContaBot Webhook (Python + Flask + Docker)

Este es un proyecto de webhook para integrar Dialogflow con la API de Contalink y automatizar procesos como emisión, consulta, cancelación de CFDIs y generación de reportes de facturación.

## 📦 Contenido

- `dialogflow_contabot_webhook.py` - Webhook en Flask para Dialogflow
- `requirements.txt` - Lista de dependencias Python
- `Dockerfile` - Configuración para contenerizar el webhook

## 🚀 Despliegue rápido

### Opción 1: Docker local
```bash
docker build -t contabot-webhook .
docker run -p 5000:5000 contabot-webhook
```

### Opción 2: Render.com
1. Crea un nuevo servicio web.
2. Conecta tu repositorio con estos archivos.
3. Establece el comando de inicio:
```bash
python dialogflow_contabot_webhook.py
```
4. Usa el puerto 5000 como público.

## 🔐 Configuración de Contalink

1. Obtén tu token desde el panel de Contalink.
2. Reemplaza el placeholder `"Bearer TU_TOKEN"` en el webhook.
3. Usa el endpoint: `https://api.contalink.com/v1/cfdi`

## 🤖 Intents soportados

- EmitirFactura
- CancelarFactura
- ConsultarFactura
- ReporteFacturacion

## 📂 Integración con Dialogflow

1. Importa los intents desde el ZIP generado anteriormente.
2. Configura el webhook en Dialogflow:
   - URL: `https://tuservidor.com/webhook`
   - Método: POST
   - Habilita la opción "Use webhook"

---

¡Listo! Este sistema permite automatizar todo el flujo de facturación electrónica directamente desde una conversación con el cliente.
