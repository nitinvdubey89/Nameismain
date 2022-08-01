
#
#PCMCIA is an acronym for Personal Computer Memory Card International Association; the acronym is pronounced as separate letters. PCMCIA is a non-profit trade association and standards body consisting of some 500 companies.18 Jan 2018

#   config t
    #username u1 priv 15 secret cisco  ## priv 15 is an admin user so that we can run enable command
    #ip scp server enable
    ### AAA config
    #aaa new-model
    #aaa authentication login default local
    #aaa authorization exec default local none
    ########configure domain-name
    ## ip domain-name python-automation.com
    ## crypto key generate rsa
    # line vty 0 1869
    # transport input telnet ssh

    ## in gns router does not have flash memory therefore pcmcia card is needed

    ## dir all-filesystems
    ## disk0:/
    ## format disk0:/


from netmiko import file_transfer
from netmiko import ConnectHandler

cisco_device = {
                  device_type:'cisco_ios',
                  host : ip ,
                  username: 'admin', ## user should match the privilege user of the router 
                  password: 'cisco',
                  port:'22',
                  secret: 'cisco' ,
                  verbose: True
                }

connection = ConnectHandler(**cisco_device)

transfer_output = file_transfer(connection, source_file='ospf.txt' , dest_file= 'ospf1.txt' , file_system='disk0:' , direction='put'
                                , overwrite_file= True)

print(transfer_output)

connection.disconnect()