import netmiko
from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.0.15.113',
    port = 22,
    username = 'admin',
    password = 'cisco'
    )

config_commands = [
    'int loopback 61070182',
    'ip add 192.168.1.1 255.255.255.0',
    'description 61070182\'s loopback'
    ]

sentConfig = sshCli.send_config_set(config_commands)

print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))