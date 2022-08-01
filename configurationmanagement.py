from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco',}
ios  = driver('10.1.1.10','admin','cisco', optional_args=optional_args)
ios.open()

## napalm uses scp for configuration management
ios.load_replace_candidate(filename='config.txt')

diff = ios.compare_config()
print(diff)

if len(diff):
    print(diff)
    print('Commit changes...')
    ios.commit_config()
    print('Done')
else:
    print('No changes required')
    ios.discard_config()

## two ways to deal with device config
##replace old configuration or merge with existing configuratino 
ios.close()
