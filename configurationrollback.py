from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco',}
ios  = driver('10.1.1.10','admin','cisco', optional_args=optional_args)
ios.open()

answer = input('Rollback?<yes|no>')
if answer == 'yes':
    print('Rolling back .. ')
    ios.rollback() # last working configuration
    print('done')


ios.close()