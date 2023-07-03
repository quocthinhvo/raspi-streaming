from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from PIL import Image
from io import BytesIO
import base64

app = FastAPI()

connected_clients = set()
frames = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            frame_bytes = await websocket.receive_bytes()
            frames.append(frame_bytes)
            await send_frame_to_clients()
    except:
        connected_clients.remove(websocket)

async def send_frame_to_clients():
    if frames:
        frame_bytes = frames.pop(0)
        img = Image.open(BytesIO(frame_bytes))
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        for client in connected_clients:
            await client.send_text(img_str)

@app.get("/")
async def show_frame():
    return HTMLResponse(content="""
        <html>
        <head>
            <title>Real-time From Raspberry</title>
            <script>
                var socket = new WebSocket("ws://localhost:8000/ws");
                socket.onmessage = function(event) {
                    var img = document.getElementById("frame");
                    img.src = "data:image/jpeg;base64," + event.data;
                };
            </script>
        </head>
        <body>
            <img id="frame" src="" alt="">
        </body>
        </html>
    """)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)