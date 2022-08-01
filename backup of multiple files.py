import paramikorefractoring
import threading

router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'user': 'labroot', 'passwd': 'cisco'}
router2 = {'server_ip': '10.1.1.20', 'server_port': '22', 'user': 'labroot', 'passwd': 'cisco'}
router3 = {'server_ip': '10.1.1.30', 'server_port': '22', 'user': 'labroot', 'passwd': 'cisco'}

routersss = [router1,router2,router3]

client = paramikorefractoring.connect(**routerss)
shell = paramikorefractoring.shell(client)

def backup(router): # backups config of router, it will have one argument the router, so called target function ,
    # function executed by each thread
    client = paramikorefractoring.connect(**router)
    shell = paramikorefractoring.getsh(client)

    paramikorefractoring.send_command(shell, 'terminal length 0')
    paramikorefractoring.send_command(shell, 'enable')
    paramikorefractoring.send_command(shell, 'cisco')
    paramikorefractoring.send_command(shell, 'show run')

    now = datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'{router1["server-ip"]}_{year}--{month}-{day}.txt'
    print(file_name)

    # an
    # f - string is a
    # literal
    # string, prefixed
    # with 'f', which contains expressions inside braces.The expressions are replaced with their values

    output = paramikorefractoring.show(shell)
    print(output)

    ## save the output to a file but we do not want to save the send_commd outputs to the file
    ## remove the first and last lines of the output from the output string
    ## we can use the splitlines functions and then we will remove the elements from the list

    output_list = output.splitlines()
    print(output_list)
    ## we can do slicing here
    output_list = output_list[11: -1]
    print(output_list)

    ## we can write a list and not a python string to  a file
    ## to get string fromm a list , we can use a join method
    output = '\n'.join(output_list)
    # Join all items in a tuple into a string, using a hash character as separator:
    # The join() method takes all items in an iterable and joins them into one string.
    # A string must be specified as the separator.

    # myDict = {"name": "John", "country": "Norway"}
    # mySeparator = "TEST"
    # nameTESTcountry
    # x = mySeparator.join(myDict)
    # Join all items in a dictionary into a string, using the word "TEST" as separator:
    # print(x)

    print(output)

    with open(file_name, 'w') as f:
        f.write(output)

    paramikorefractoring.close(client)

##python list can store any type of object including abstract one's i.e threads
threads = list() ## you can convert a varable into list by using list()
for router in routersss:
    th = threading.Thread(target=backup, args =(router,))  ## Thread is constructor that creates a thread
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
    # join methods waits for each thread to complete
    # there is difference in parallelism and concurrenty and infact the cpu does not execute the threads in parallel
## when you want a tuple with single element then you should put a comma after that single element i.e. args =(router,)

    #client = paramikorefractoring.connect(**router1)
    #shell = paramikorefractoring.getsh(client)

    #paramikorefractoring.send_command(shell, 'terminal length 0')
    #paramikorefractoring.send_command(shell, 'enable')
    #paramikorefractoring.send_command(shell, 'cisco')
    #paramikorefractoring.send_command(shell, 'show run')

    #now = datetime.now()
    #print(now)
    #year = now.year
    #month = now.month
    #day = now.day
    #hour = now.hour
    #minute = now.minute

    #file_name = f'{router1["server-ip"]}_{year}--{month}-{day}.txt'
    #print(file_name)

    # an
    # f - string is a
    # literal
    # string, prefixed
    # with 'f', which contains expressions inside braces.The expressions are replaced with their values

    #output = paramikorefractoring.show(shell)
    #print(output)

    ## save the output to a file but we do not want to save the send_commd outputs to the file
    ## remove the first and last lines of the output from the output string
    ## we can use the splitlines functions and then we will remove the elements from the list

    #output_list = output.splitlines()
    #print(output_list)
    ## we can do slicing here
    #output_list = output_list[11: -1]
    #print(output_list)

    ## we can write a list and not a python string to  a file
    ## to get string fromm a list , we can use a join method
    #output = '\n'.join(output_list)
    # Join all items in a tuple into a string, using a hash character as separator:
    # The join() method takes all items in an iterable and joins them into one string.
    # A string must be specified as the separator.

    # myDict = {"name": "John", "country": "Norway"}
    # mySeparator = "TEST"
    # nameTESTcountry
    # x = mySeparator.join(myDict)
    # Join all items in a dictionary into a string, using the word "TEST" as separator:
    # print(x)

    #print(output)

    #with open(file_name, 'w') as f:
     #   f.write(output)

    #paramikorefractoring.close(client)

################################## MULTI-THREADING IS NEEDED BECAUSE THE ABOVE FOR LOOP IS VERY VERY SLOW AS ITS A ONE BY ONE APPROACH###########
## BY DEFAULT A PYTHON SCRIPT RUNS AS A SINGLE PROCESS WITH A SINGLE THREAD INSIDE IT
## if we have a big network with 500 routers and if a single backup takes 5 seconds
###connect routers at the same  and execute backup tasks concurrently

