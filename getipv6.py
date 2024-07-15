import socket

def get_ipv6_address():
    try:
        hostname = socket.gethostname()
        addresses = socket.getaddrinfo(hostname, None, socket.AF_INET6)


        family, _, _, _, sockaddr = addresses[2]
        if family == socket.AF_INET6:
            ipv6_address = sockaddr[0]
            return ipv6_address
        return None
    except socket.error:
        return None

if __name__ == "__main__":
    local_ipv6 = get_ipv6_address()
    if local_ipv6:
        print(f"Local ipv6 address is: ", local_ipv6 )
    else:
        print("Unable to retrieve the local ipv6 address.")