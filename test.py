import asyncio
import websockets
import cv2
i = 0
async def send_frame(websocket,frame):
    global i
    i += 1
    print(i)
    await websocket.send(frame)

async def main():
    video_path = "video.mp4"
    cap = cv2.VideoCapture(video_path)
    websocket = await websockets.connect('ws://localhost:8000/ws')
    while cap.isOpened():
        tasks = list()
        ret, frame = cap.read()
        if not ret:
            break
        _, encoded_frame = cv2.imencode('.jpg', frame)
        frame_bytes = encoded_frame.tobytes()
        tasks.append(asyncio.create_task(send_frame(websocket, frame_bytes)))
        await asyncio.gather(*tasks)
    cap.release()

asyncio.get_event_loop().run_until_complete(main())