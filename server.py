import asyncio
import subprocess
import websockets
from pynput.keyboard import Key,Controller
import math
import time

keyboard = Controller()

# create handler for each connection

async def handler(websocket, path):

    data = await websocket.recv()

    if data == 'getvolume':
        volume = subprocess.check_output('getvol.bat', shell=True).strip()
        output = str(volume).replace('b', '')
        output = output.replace("'", '', 2)
        await websocket.send(output)
    elif "setvolume" in data:
        volume = data.split(' ')
        asdf = subprocess.check_output('getvol.bat', shell=True).strip()
        output = str(asdf).replace('b', '')
        output = output.replace("'", '', 2)
        realvolume = int(int(volume[1]) / 2)
        print(realvolume)
        for item in range(realvolume):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            time.sleep(0.1)
    elif "check":
        await websocket.send('checked')

    reply = f"Data received as:  {data}!"
    print(reply)

 

start_server = websockets.serve(handler, "localhost", 8008)

asyncio.get_event_loop().run_until_complete(start_server)
print('Runned')
asyncio.get_event_loop().run_forever()
