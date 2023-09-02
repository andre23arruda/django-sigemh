import socket, subprocess

PORT = '8000'

get_ip_address = lambda: socket.gethostbyname(socket.gethostname())

def main():
    '''Run'''
    subprocess.call(f'python manage.py runserver { get_ip_address() }:{ PORT }', shell=True)
    # subprocess.call(f'python manage.py runserver { PORT }', shell=True)


if __name__ == '__main__':
    main()