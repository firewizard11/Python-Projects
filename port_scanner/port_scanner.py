import socket

target_host = '8.8.8.8'
target_ports = [21,22,80,443]

def test_port(target_host: str, target_port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        
        try:
            sock.connect((target_host, target_port))
            print(f'Connection Success: {target_port}')
        except:
            print(f'Connection Failed: {target_port}')


if __name__ == '__main__':
    for port in target_ports:
        test_port(target_host, port)