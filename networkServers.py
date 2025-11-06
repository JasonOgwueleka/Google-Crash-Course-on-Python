# This program defines a function that takes a dictionary of server names and their IP addresses
# It returns a formatted list showing each server and its corresponding IP
# When called, it prints out each server’s name and IP address on separate lines

def network(servers):
    # A string variable is initialized to hold the "result".
    result = ""

    for hostname, IP_address in servers.items():
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n"
    return result


# Call the "network" function with the dictionary.
print(network({"Domain Name Server": "8.8.8.8", "Gateway Server": "192.168.1.1", "Print Server": "192.168.1.33",
               "Mail Server": "192.168.1.190"}))
