import console1


console = console1.open_console()
# console is object returned by openconsole function
console1.check_initial_configuration_dialog(console)

with open('config.txt') as f:
    command = f.readlines()
    for cmd in command:
        console1.run_command(console, cmd)


#console1.run_command('enable')
#console1.run_command('configure terminal')
#console1.run_command('username u1 secret cisco')
#console1.run_command('end')


## nothing got displayed in the console because the file closed the connection; last command is exit # you can check the stauts on the router

#usinng an encode function and adding a b'' is the same thing
# always use /n
# always use time.sleep

output = console1.read_from_console(console)
print(output)
