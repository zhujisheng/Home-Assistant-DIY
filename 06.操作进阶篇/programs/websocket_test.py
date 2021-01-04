import asyncio
import json

import aiohttp

ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmYTRkMTg4YTkwNDQ0ZmI0YmM4MDNiZmFkODNkNmU2MyIsImlhdCI6MTYwOTcyNzM5MywiZXhwIjoxOTI1MDg3MzkzfQ.OR2ckMLqAzM1fZWWd5hwbM9WC-LjQ-H3O4Y3aWab2tU'


async def main():
    """Simple WebSocket client for Home Assistant."""
    async with aiohttp.ClientSession().ws_connect(
            'http://192.168.3.7:8123/api/websocket') as ws:
            
            await ws.send_str(json.dumps(
                {'type': 'auth', 
                 'access_token': ACCESS_TOKEN}
            ))
        
            await ws.send_str(json.dumps(
                {'id': 1, 'type': 'subscribe_events',
                 'event_type': 'state_changed'}
            ))
            
            while True:
                msg = await ws.receive()
                print(msg)
                if msg.type == aiohttp.WSMsgType.ERROR:
                    break
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    break
                    
loop = asyncio.get_event_loop()  
loop.run_until_complete(main())
loop.close()  
