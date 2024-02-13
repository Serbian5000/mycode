#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library"""

import netifaces

def find_mac(interface_name):
    """Passed interface name (String), returns MAC of that interface (String)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_LINK])[0]['addr']

def find_ip(interface_name):
    """passed interface namne (string), returns the IP of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_INET])[0]['addr']
def main():
    """runtime"""

    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ', find_mac(i))
            
            print('IP: ', find_ip(i))
            
        except:
            print('Could not collect adapter information')

if __name__ == "__main__":
    main()
            
