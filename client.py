import asyncio
import websockets
import base64
from io import BytesIO
from PIL import Image
import cv2

async def send_frame():
    async with websockets.connect('ws://192.168.28.27:8085/ws') as websocket:
        capture = cv2.VideoCapture(0) 
        while True:
            ret, frame = capture.read()  
            _, jpeg_frame = cv2.imencode('.jpg', frame)
            frame_bytes = jpeg_frame.tobytes()
            await websocket.send(frame_bytes)

asyncio.get_event_loop().run_until_complete(send_frame())