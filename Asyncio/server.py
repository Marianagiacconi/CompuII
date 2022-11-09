import asyncio
import time
import subprocess
import argparse
import socket


async def handler(reader, writer):
        
    addr = writer.get_extra_info('peername')
    print(f"Client {addr!r}")
    data = await reader.read(100)
    command = data.decode()
    print(f"Command :  {command!r} ")
    proceso = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out,err = proceso.communicate()
    response = out + err
    writer.write(response)
    await writer.drain()
    writer.close()


async def main():

    parser = argparse.ArgumentParser(description=None)
    parser.add_argument("--port", type=int, help="int")
    args = parser.parse_args()

    try:
        if( not args.port):
            server = await asyncio.start_server(
            handler, '127.0.0.1', 8888)
            print("Default Mode")
        else:
            server = await asyncio.start_server(
            handler, '127.0.0.1', args.port)
    except ValueError:
        server = await asyncio.start_server(
        handler, '127.0.0.1', 8888)
        print("Default Mode")

    addr = server.sockets[0].getsockname()
    print(f'---> Serving on {addr}')

    async with server:
        await server.serve_forever()


asyncio.run(main())


