def print_ip(ip_addr, username='admin', password='cisco123'):
    print("My IP address is: {}".format(ip_addr))
    print(username)
    print(password)
    return

my_list = '10.1.1.1', 'admin', 'admin123'

print_ip(*my_list)
# if you have the *, it passes items in individually, otherwise it passes the whole list as ip_addr