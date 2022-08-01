import paramikorefractoring

client = paramikorefractoring.connect('192.168.0.50','22','labroot','pass123')
shell =  paramikorefractoring.getsh(client)
paramikorefractoring.send_command(shell,'uname -a')

output = paramikorefractoring.show(shell)
print(output)

cmd = 'sudo  groupadd developers'
paramikorefractoring.send_command(shell,cmd)
paramikorefractoring.send_command(shell,'pass123',2)
## inorder to provide between view of the output , we use the show function defined in paramikorefractoring.py
paramikorefractoring.show(shell)
paramikorefractoring.send_command(shell,'tail -n 1 /etc/group')

paramikorefractoring.close(client)



