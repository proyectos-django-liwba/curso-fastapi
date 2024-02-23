import asyncio
from fastapi import WebSocket
from typing import List

class WebSocketManager:
    def __init__(self):
        self.connections: List = []
        print("WebSocketManager created")
    
    async def connect(self, websocket: WebSocket):
        print("WebSocket connected")
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        print("WebSocket disconnected")
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        await asyncio.gather(
            *[connection.send_text(message) for connection in self.connections]
        )

