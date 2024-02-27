import netmiko
from getpass import getpass

# Replace the following values with your own
routers = [
    {
        "ip": "192.168.1.1",
        "username": "cisco",
        "password": "cisco",
    },
    {
        "ip": "192.168.1.2",
        "username": "cisco",
        "password": "cisco",
    },
    {
        "ip": "192.168.1.3",
        "username": "cisco",
        "password": "cisco",
    },
]

# Function to update the router
def update_router(device):
    with netmiko.ConnectHandler(
        device_type="cisco_ios",
        host=device["ip"],
        username=device["username"],
        password=device["password"],
    ) as remote_connection:
        remote_connection.send_config_set(r"enable service password-encryption")
        remote_connection.send_config_set(r"enable secret cisco")
        remote_connection.send_config_set(r"line vty 0 4")
        remote_connection.send_config_set(r"password cisco")
        remote_connection.send_config_set(r"line con 0")
        remote_connection.send_config_set(r"password cisco")
        remote_connection.send_config_set(r"no service password-encryption")
        remote_connection.send_config_set(r"exit")
        remote_connection.send_command("write memory")

# Update each router in the range
for router in routers:
    update_router(router)