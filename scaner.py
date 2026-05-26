import socket

host = input("Ingrese la IP del host: ")

for port in range(7999, 8090):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.settimeout(1)

    try:

        result = client.connect_ex((host, port))

        if result == 0:

            print(f"Puerto {port} abierto")

        else:

            range(7999, 8090)

    except Exception as e:

        print(f"Error: {e}")

    client.close()