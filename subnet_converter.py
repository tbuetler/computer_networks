#!/usr/bin/env python3
import ipaddress

def benötigte_cidr(hosts):
    """ Berechnet die kleinste Subnetzmaske (CIDR), die genug Hosts aufnehmen kann """
    for cidr in range(30, 0, -1):  # /30 ist das kleinste sinnvolle Subnetz
        if (2 ** (32 - cidr)) - 2 >= hosts:
            return cidr
    return None  # Falls keine passende Maske existiert

def subnetting(netzwerk, host_list):
    """ Erstellt Subnetze für die benötigten Host-Anzahlen """
    net = ipaddress.ip_network(netzwerk, strict=False)
    host_list.sort(reverse=True)  # Größte zuerst

    subnets = []
    start_ip = net.network_address
    remaining_ips = net.num_addresses  # Verbleibende IPs berechnen

    for hosts in host_list:
        cidr = benötigte_cidr(hosts)
        if cidr is None or remaining_ips < 2 ** (32 - cidr):
            print(f"❌ Fehler: {hosts} Hosts passen nicht ins verfügbare Netzwerk.")
            continue
        
        subnet = ipaddress.ip_network(f"{start_ip}/{cidr}", strict=False)
        subnets.append((subnet, hosts))

        # Nächstes freie Subnetz berechnen
        start_ip = subnet.broadcast_address + 1
        remaining_ips -= subnet.num_addresses  # Verbleibende IPs anpassen

        if start_ip > net.broadcast_address:
            print("⚠️ Keine weiteren IP-Adressen verfügbar.")
            break

    return subnets, remaining_ips

def mögliche_subnetze(remaining_ips):
    """ Berechnet, wie viele /30-Subnetze noch möglich wären """
    if remaining_ips < 4:
        return 0
    return remaining_ips // 4  # /30 hat immer 4 IPs

def validate_host_list(host_list, total_ips):
    """ Prüft, ob die angeforderte Menge an Hosts überhaupt ins Netzwerk passt """
    benötigte_ips = sum((2 ** (32 - benötigte_cidr(hosts)) for hosts in host_list if benötigte_cidr(hosts)))
    if benötigte_ips > total_ips:
        return False, benötigte_ips
    return True, benötigte_ips

def main():
    netzwerk = input("Gib die IPv4-Adresse mit Präfix (z.B. 193.5.86.0/24) ein: ").strip()
    hosts_input = input("Gib die benötigten Hosts als Liste an (z.B. 4,12,17,67): ").strip()

    try:
        host_liste = list(map(int, hosts_input.split(",")))
    except ValueError:
        print("❌ Fehler: Die Eingabe muss eine kommagetrennte Liste von Zahlen sein.")
        return

    try:
        ip_net = ipaddress.ip_network(netzwerk, strict=False)
    except ValueError:
        print("❌ Fehler: Ungültige Netzwerkadresse.")
        return

    print("\n📊 Netzwerkinformationen:")
    print(f"🌍 Netzwerkadresse: {netzwerk}")
    print(f"📏 Verfügbare IPs: {ip_net.num_addresses}")
    
    # Prüfe ob alle Hostanforderungen ins Netzwerk passen
    valid, benötigte_ips = validate_host_list(host_liste, ip_net.num_addresses)
    if not valid:
        print(f"❌ Fehler: Die benötigten Subnetze erfordern {benötigte_ips} IP-Adressen, "
              f"aber das Netzwerk hat nur {ip_net.num_addresses}.")
        return

    # Berechnung der Subnetze
    subnets, remaining_ips = subnetting(netzwerk, host_liste)

    if not subnets:
        print("❌ Fehler: Keine passenden Subnetze gefunden.")
        return

    # Ausgabe der berechneten Subnetze
    print("\n📊 Berechnete Subnetze:")
    for i, (subnet, hosts) in enumerate(subnets, start=1):
        print(f"\n🔹 **Subnetz {i}:**")
        print(f"   🌐 Netzwerk-Adresse: {subnet.network_address}")
        print(f"   📏 Netmask: {subnet.netmask}")
        print(f"   🔢 CIDR-Notation: /{subnet.prefixlen}")
        print(f"   💻 Benötigte Hosts: {hosts}")
        print(f"   🏠 Erster Host: {subnet.network_address + 1}")
        print(f"   🏠 Letzter Host: {subnet.broadcast_address - 1}")
        print(f"   📢 Broadcast-Adresse: {subnet.broadcast_address}")

    # Berechnung der noch möglichen Subnetze
    freie_subnetze = mögliche_subnetze(remaining_ips)
    print("\n📊 **Zusätzliche Subnetze möglich**")
    print(f"   🏗️ Verbleibende IPs: {remaining_ips}")
    print(f"   🏠 Anzahl zusätzlicher /30-Subnetze: {freie_subnetze}")

if __name__ == "__main__":
    main()