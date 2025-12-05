import asyncio

async def check_port(host, port, timeout=1):
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout)
        writer.close()
        await writer.wait_closed()
        return True, None
    except Exception as e:
        return False, e


async def main():

    IP = input("IP or domain: ")
    PORTS = input("Ports to check(separate by ','):")
    if PORTS == "all":
        PORTS = list(range(1, 65536))
    elif PORTS == "preset 1":
        PORTS = [22, 80, 443, 8080, 3306]
    else:
        PORTS = [int(p.strip()) for p in PORTS.split(",")]
    for port in PORTS:
        is_open, error = await check_port(IP, port)
        if is_open:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is closed. Error: {error}")

asyncio.run(main())

    
