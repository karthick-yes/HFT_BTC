import json
import websocket
import sys


counter = 0


def on_open(ws):
    print("connection secured")
    data = json.dumps({
        "type": "subscribe",
        "channels": [
            {
                "name": "full",
                "product_ids": [
                    "BTC-USD"
                ]
            }
        ]
    })
    ws.send(data)


def on_message(ws, message):
    global counter
    counter += 1

    print(str(message) + '\n')

    with open("BTC.csv", "a") as f:
        f.write(str(message) + '\n')
        if counter == 1000000:
            ws.close()
            sys.exit()


socket = "wss://ws-feed-public.sandbox.exchange.coinbase.com"

while True:
    try:
        ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
        ws.run_forever()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Restarting the script...")

