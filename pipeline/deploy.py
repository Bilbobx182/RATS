import paramiko
import sys

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('35.214.32.187', port = '22', username='onuallainc')
stdin, stdout, stderr = client.exec_command('docker pull gcr.io/rats-290113/backendrats')
stdin, stdout, stderr = client.exec_command('docker pull gcr.io/rats-290113/frontendrats')

print(stdout.read())
client.close()