from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco',}
ios  = driver('10.1.1.10','admin','cisco', optional_args=optional_args)
ios.open()

ios.load_merge_candidate('acl.txt')

## we can add jinja2 templates too

diff = ios.compare_config()
#print(diff)

if len(diff) > 0:
    print(diff)
    answer = input('Commit changes?<yes|no>')
    if answer == 'yes':
        print('Commit changes...')
        ios.commit_config()
        print('Done')
    else:
        print('No changes required')
        ios.discard_config()


ios.close()
