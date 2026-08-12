import socket

print("GHOST-SCANNER V1")
ip = input("MASUKIN {TARGET} URL/IP: ")

port_list = [21, 22, 23, 80, 443, 8080]

print(f"\n[`] Scanning {ip}..")
for port in port_list:
    s = socket.socket()
    s.settimeout(1)
    hasil = s.connect_ex((ip, port))
    if hasil == 0:
        print(f"[+] port {port} OPEN")
    else:
        print(f"[+] port {port} CLOSED")
    
    print("SELESAI SCANNER")
    s.close()