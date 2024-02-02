import socket

def print_dict_pretty(dictionary, indent=0):

    for key, value in dictionary.items():
        print(f"{'  ' * indent}{key}:")
        if isinstance(value, dict):
            print_dict_pretty(value, indent + 1)
        elif isinstance(value, list):
            print(f"{'  ' * (indent + 1)}[")
            for item in value:
                if isinstance(item, dict):
                    print_dict_pretty(item, indent + 2)
                else:
                    print(f"{'  ' * (indent + 2)}{item}")
            print(f"{'  ' * (indent + 1)}]")
        else:
            print(f"{'  ' * (indent + 1)}{value}")

def scan_ports(ip:str, ports:list) -> dict:
    scan_info = {}
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))
            sock.close()

            if result == 0:
                scan_info[port] = True
            else:
                scan_info[port] = False
        except Exception as e:
            print(f"Error: {e}")
            scan_info[port] = "Error"
    return scan_info

def scan_alumnes(alumnes: dict, ports = [22, 80]) -> dict:
    for nom_alumne in alumnes:
        port_status = scan_ports(alumnes[nom_alumne], ports)
        alumnes[nom_alumne] = {"IP" : alumnes[nom_alumne]}
        for port in port_status:
            alumnes[nom_alumne][port] = port_status[port]
    return alumnes

alumnes = {
    "Nom de exemple": "127.0.0.1"
}

alumnes = scan_alumnes(alumnes)

print_dict_pretty(alumnes)