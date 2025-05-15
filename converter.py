#!/usr/bin/env python3
import socket
import struct

# ANSI Farben
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
CYAN = "\033[96m"

def dezimal_zu_binär(dezimalzahl):
    return bin(dezimalzahl)[2:]

def binär_in_8bit_blöcke(binärzahl):
    binärzahl = binärzahl.zfill(32)  
    return ' '.join([binärzahl[i:i+8] for i in range(0, len(binärzahl), 8)])

def dezimal_zu_oktal(dezimalzahl):
    return oct(dezimalzahl)[2:]

def dezimal_zu_hexadezimal(dezimalzahl):
    return hex(dezimalzahl)[2:].upper()

def ip_zu_dezimal(ip_adresse):
    return struct.unpack("!L", socket.inet_aton(ip_adresse))[0]

def dezimal_zu_ip(dezimalzahl):
    try:
        return socket.inet_ntoa(struct.pack("!L", dezimalzahl))
    except struct.error:
        return "Nicht darstellbar"

def ip_to_bin(ip):
    return binär_in_8bit_blöcke(dezimal_zu_binär(ip_zu_dezimal(ip)))

def subnetz_berechnung(ip, subnetzmaske=24):
    ip_int = ip_zu_dezimal(ip)
    netmask_int = (0xFFFFFFFF << (32 - subnetzmaske)) & 0xFFFFFFFF
    netzwerk_int = ip_int & netmask_int
    broadcast_int = netzwerk_int | (~netmask_int & 0xFFFFFFFF)

    return {
        "Netzwerkadresse": dezimal_zu_ip(netzwerk_int),
        "Broadcast-Adresse": dezimal_zu_ip(broadcast_int),
        "Subnetzmaske": dezimal_zu_ip(netmask_int),
        "Erste Hostadresse": dezimal_zu_ip(netzwerk_int + 1),
        "Letzte Hostadresse": dezimal_zu_ip(broadcast_int - 1),
        "CIDR": f"{ip}/{subnetzmaske}"
    }

def parse_eingabe(eingabe):
    if eingabe.count('.') == 3:  # IPv4-Adresse erkannt
        try:
            return ip_zu_dezimal(eingabe), "ipv4"
        except socket.error:
            print(f"{RED}❌ Ungültige IPv4-Adresse!{RESET}")
            exit(1)

    try:
        if eingabe.startswith("0b"):
            return int(eingabe, 2), "bin"
        elif eingabe.startswith("0x"):
            return int(eingabe, 16), "hex"
        elif eingabe.startswith("0o"):
            return int(eingabe, 8), "okt"
        else:
            return int(eingabe), "dez"
    except ValueError:
        print(f"{RED}❌ Ungültige Eingabe!{RESET}")
        exit(1)

def main():
    eingabe = input(f"{CYAN}🔢 Gib eine Zahl oder IPv4-Adresse ein:{RESET} ").strip()
    dezimalzahl, typ = parse_eingabe(eingabe)

    binärzahl = dezimal_zu_binär(dezimalzahl)
    binär_8bit = binär_in_8bit_blöcke(binärzahl)

    print(f"\n{BOLD}📊 Ergebnisse:{RESET}")
    print(f"{YELLOW}{'Eingabe:':<24}{RESET}{GREEN}{eingabe} ({typ}){RESET}")
    print(f"{YELLOW}{'Dezimal:':<24}{RESET}{GREEN}{dezimalzahl}{RESET}")
    print(f"{YELLOW}{'Binär (8-Bit):':<24}{RESET}{GREEN}{binär_8bit}{RESET}")
    print(f"{YELLOW}{'Oktal:':<24}{RESET}{GREEN}{dezimal_zu_oktal(dezimalzahl)}{RESET}")
    print(f"{YELLOW}{'Hexadezimal:':<24}{RESET}{GREEN}{dezimal_zu_hexadezimal(dezimalzahl)}{RESET}")

    if dezimalzahl <= 0xFFFFFFFF:  
        ip_adresse = dezimal_zu_ip(dezimalzahl)
        if ip_adresse != "Nicht darstellbar":
            subnetz = subnetz_berechnung(ip_adresse, 24)
            print(f"\n{BOLD}{BLUE}🌐 IPv4-Informationen:{RESET}")
            print(f"{YELLOW}{'IPv4-Adresse:':<24}{RESET}{GREEN}{ip_adresse}{RESET}")
            print(f"{YELLOW}{'Binär:':<24}{RESET}{GREEN}{ip_to_bin(ip_adresse)}{RESET}")
            print(f"{YELLOW}{'Netzwerkadresse:':<24}{RESET}{GREEN}{subnetz['Netzwerkadresse']}{RESET}")
            print(f"{YELLOW}{'Broadcast-Adresse:':<24}{RESET}{GREEN}{subnetz['Broadcast-Adresse']}{RESET}")
            print(f"{YELLOW}{'Subnetzmaske:':<24}{RESET}{GREEN}{subnetz['Subnetzmaske']}{RESET}")
            print(f"{YELLOW}{'Erste Hostadresse:':<24}{RESET}{GREEN}{subnetz['Erste Hostadresse']}{RESET}")
            print(f"{YELLOW}{'Letzte Hostadresse:':<24}{RESET}{GREEN}{subnetz['Letzte Hostadresse']}{RESET}")
            print(f"{YELLOW}{'CIDR-Notation:':<24}{RESET}{GREEN}{subnetz['CIDR']}{RESET}")

if __name__ == "__main__":
    main()

