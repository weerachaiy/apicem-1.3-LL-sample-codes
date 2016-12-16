"""
Script name: lab1-1-get-host.py
This script prints out all hosts that are connected to APIC-EM network devices in a tabular list format.
"""

from apicem import * 

def get_host():
    """
    This function returns a tabular list of all hosts that are connected to APIC-EM network devices.  
    Return:
    ------
    list: a list of all hosts and netwrok devices with a number tag  
    """
    host_list=[]
    try:
        resp = get(api="host") # The get() function is the simplify version for "get" function in requests module, defined in apicem.py
        response_json = resp.json() # Get the json-encoded content from response
        print ("Status: ",resp.status_code)  # This is the http request status
        # print (json.dumps(response_json,indent=4)) # Convert "response_json" object to a JSON formatted string and print it out    
    except:
        print ("Something wrong with GET /host request!")
        return host_list
    # Now create a list of host summary
    i=0
    for item in response_json["response"]:
        i+=1
        host_list.append([i,item["hostIp"],item["hostType"],item["connectedNetworkDeviceIpAddress"]])
    return host_list

if __name__ == "__main__": # Execute only if run as a script
    host=get_host()
    # We use tabulate module here to print a nice table format. You should use "pip" tool to install in your local machine
    # The tabulate module is imported in apicem.py
    # For the simplicity we just copy the source code in working directory without installing it
    print (tabulate(host,headers=['number','host IP','type','connected to network device'],tablefmt="rst"))


    
