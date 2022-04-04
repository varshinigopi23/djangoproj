import paramiko
client=paramiko.SSHClient()
client.load_system_host_keys()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def para(i,vm,u,p):
    client=paramiko.SSHClient()
    client.load_system_host_keys()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=vm+'.athenahealth.com',port=22,username=u,password=p)
    (stdin, stdout, stderr) = client.exec_command(i+" | wc -l")
    cmd_output=stdout.read()
    cmd_output=str(cmd_output)
    cmd_output=cmd_output.replace("b'","")
    cmd_output=cmd_output.replace("n'","")
    cmd_output=cmd_output[:-1]
    return cmd_output