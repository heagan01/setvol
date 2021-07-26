import asyncio
import subprocess
import websockets
import math

# create handler for each connection

async def handler(websocket, path):

    data = await websocket.recv()

    if data == 'getvolume':
        volume = subprocess.check_output('getvol.bat', shell=True).strip()
        output = str(volume).replace('b', '')
        output = output.replace("'", '', 2)
        await websocket.send(output)
        print(type(output))
    elif "setvolume" in data:
        mystring = data.split()
        print(mystring[1])
        subprocess.run(['SetVol.exe', mystring[1]])
    elif "check":
        await websocket.send('checked')

    reply = f"Data received as:  {data}!"
    print(reply)

 

start_server = websockets.serve(handler, "192.168.18.15", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
print('Runned')
asyncio.get_event_loop().run_forever()
