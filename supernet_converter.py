def ip_to_bin_spaced(ip):
    return ' '.join(f'{int(octet):08b}' for octet in ip.split('.'))

def ip_to_bin(ip):
    return ''.join(f'{int(octet):08b}' for octet in ip.split('.'))

def common_prefix(bits_list):
    prefix = ""
    for i in range(len(bits_list[0])):
        bit = bits_list[0][i]
        if all(bits[i] == bit for bits in bits_list):
            prefix += bit
        else:
            break
    return prefix

def bin_to_ip(bin_str):
    octets = [str(int(bin_str[i:i+8], 2)) for i in range(0, 32, 8)]
    return '.'.join(octets)

def main():
    # Eingabe der IP-Adressen
    input_ips = input("Gib IP-Adressen durch Komma getrennt ein (z.B. 193.5.87.0,193.5.88.0): ")
    ip_list = [ip.strip() for ip in input_ips.split(',')]

    # Binär-Darstellungen
    bin_list = [ip_to_bin(ip) for ip in ip_list]

    print("\n📘 Binäre Darstellung (8 Bit gruppiert):")
    for ip, binary in zip(ip_list, bin_list):
        spaced = ' '.join([binary[i:i+8] for i in range(0, 32, 8)])
        print(f"{ip:<15} → {spaced}")

    # Gemeinsames Präfix ermitteln
    prefix = common_prefix(bin_list)
    cidr = len(prefix)
    network_bin = prefix.ljust(32, '0')
    network_ip = bin_to_ip(network_bin)

    # IP-Anzahl berechnen
    total_ips = 2 ** (32 - cidr)
    usable_hosts = total_ips - 2 if cidr < 31 else 0

    print("\n🧠 Ergebnis:")
    print(f"CIDR-Notation:        {network_ip}/{cidr}")
    print(f"Gemeinsames Präfix:   {prefix}")
    print(f"Netzadresse:          {network_ip}")
    print(f"Anzahl IPs:           {total_ips}")
    print(f"Nutzbare Hosts:       {usable_hosts if usable_hosts > 0 else 'Keine (Point-to-Point oder Einzelgerät)'}")

if __name__ == "__main__":
    main()

