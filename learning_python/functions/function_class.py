def print_ip(ip_addr, username='admin', password='cisco123'):
    print("My IP address is: {}".format(ip_addr))
    print(username)
    print(password)
    return

my_dict = {
    'ip_addr': '10.1.1.1',
    'username': 'admin',
    'password': 'admin123',
}

print_ip(**my_dict)
# if you have the *, it passes items in individually, otherwise it passes the whole list as ip_addr

# research classes and methods

class MyClass(object):
    def __init__(self, ip_addr, username, password):
