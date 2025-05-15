# Computer Networks Utilities

This repository contains helper programs that work with networks, subnetting, conversions, and more.

## Programs Included

1. **`converter.py`**
   - Converts IP addresses or numbers between different formats (binary, decimal, octal, hexadecimal).
   - Provides detailed network information for a given IPv4 address, including subnet masks and broadcast addresses.

2. **`subnet_converter.py`**
   - Splits a given network into smaller subnets based on user-specified host requirements per subnet.
   - Ensures efficient subnet allocation and provides clear feedback about leftover IP addresses and additional possible subnets.

---

## Usage Instructions

### `converter.py`

This program can process and convert numbers and IP addresses into various formats.

#### Example Execution:

```commandline
 ~/Documents/programs/computer_networks ❯ python3 converter
🔢 Gib eine Zahl oder IPv4-Adresse ein: 1040336008

📊 Ergebnisse:
Eingabe:                1040336008 (dez)
Dezimal:                1040336008
Binär (8-Bit):          00111110 00000010 01000100 10001000
Oktal:                  7600442210
Hexadezimal:            3E024488

🌐 IPv4-Informationen:
IPv4-Adresse:           62.2.68.136
Binär:                  00111110 00000010 01000100 10001000
Netzwerkadresse:        62.2.68.0
Broadcast-Adresse:      62.2.68.255
Subnetzmaske:           255.255.255.0
Erste Hostadresse:      62.2.68.1
Letzte Hostadresse:     62.2.68.254
CIDR-Notation:          62.2.68.136/24
```
```commandline
 ~/Doc/programs/computer_networks ❯ python3 converter
🔢 Gib eine Zahl oder IPv4-Adresse ein: 0x3E024488

📊 Ergebnisse:
Eingabe:                0x3E024488 (hex)
Dezimal:                1040336008
Binär (8-Bit):          00111110 00000010 01000100 10001000
Oktal:                  7600442210
Hexadezimal:            3E024488

🌐 IPv4-Informationen:
IPv4-Adresse:           62.2.68.136
Binär:                  00111110 00000010 01000100 10001000
Netzwerkadresse:        62.2.68.0
Broadcast-Adresse:      62.2.68.255
Subnetzmaske:           255.255.255.0
Erste Hostadresse:      62.2.68.1
Letzte Hostadresse:     62.2.68.254
CIDR-Notation:          62.2.68.136/24
```
```commandline
 ~/Doc/programs/computer_networks ❯ python3 converter
🔢 Gib eine Zahl oder IPv4-Adresse ein: 0b00111110000000100100010010001000

📊 Ergebnisse:
Eingabe:                0b00111110000000100100010010001000 (bin)
Dezimal:                1040336008
Binär (8-Bit):          00111110 00000010 01000100 10001000
Oktal:                  7600442210
Hexadezimal:            3E024488

🌐 IPv4-Informationen:
IPv4-Adresse:           62.2.68.136
Binär:                  00111110 00000010 01000100 10001000
Netzwerkadresse:        62.2.68.0
Broadcast-Adresse:      62.2.68.255
Subnetzmaske:           255.255.255.0
Erste Hostadresse:      62.2.68.1
Letzte Hostadresse:     62.2.68.254
CIDR-Notation:          62.2.68.136/24
```
```commandline
 ~/Doc/programs/computer_networks ❯ python3 converter
🔢 Gib eine Zahl oder IPv4-Adresse ein: 193.5.80.10

📊 Ergebnisse:
Eingabe:                193.5.80.10 (ipv4)
Dezimal:                3238350858
Binär (8-Bit):          11000001 00000101 01010000 00001010
Oktal:                  30101250012
Hexadezimal:            C105500A

🌐 IPv4-Informationen:
IPv4-Adresse:           193.5.80.10
Binär:                  11000001 00000101 01010000 00001010
Netzwerkadresse:        193.5.80.0
Broadcast-Adresse:      193.5.80.255
Subnetzmaske:           255.255.255.0
Erste Hostadresse:      193.5.80.1
Letzte Hostadresse:     193.5.80.254
CIDR-Notation:          193.5.80.10/24
```

This tool is ideal for educational purposes, troubleshooting, or understanding IP address representations.

---

### `subnet_converter.py`

This program takes a Class C (or larger) network (e.g., `193.5.86.0/24`) and splits it into smaller subnets based on user-specified host requirements.

#### Features:
- Automatically calculates the needed subnet masks (CIDR) for the requested host counts.
- Lists unused IPs and additional possible subnet allocations.
- Provides detailed information for each generated subnet.

#### Example Execution:

```bash
 ~/Documents/programs/computer_networks master +3 ❯ python3 subnet_converter
Gib die IPv4-Adresse mit Präfix (z.B. 193.5.86.0/24) ein: 193.5.86.0/24
Gib die benötigten Hosts als Liste an (z.B. 4,12,17,67): 4,12,17,67

📊 Netzwerkinformationen:
🌍 Netzwerkadresse: 193.5.86.0/24
📏 Verfügbare IPs: 256

📊 Berechnete Subnetze:

🔹 **Subnetz 1:**
   🌐 Netzwerk-Adresse: 193.5.86.0
   📏 Netmask: 255.255.255.128
   🔢 CIDR-Notation: /25
   💻 Benötigte Hosts: 67
   🏠 Erster Host: 193.5.86.1
   🏠 Letzter Host: 193.5.86.126
   📢 Broadcast-Adresse: 193.5.86.127

🔹 **Subnetz 2:**
   🌐 Netzwerk-Adresse: 193.5.86.128
   📏 Netmask: 255.255.255.224
   🔢 CIDR-Notation: /27
   💻 Benötigte Hosts: 17
   🏠 Erster Host: 193.5.86.129
   🏠 Letzter Host: 193.5.86.158
   📢 Broadcast-Adresse: 193.5.86.159

🔹 **Subnetz 3:**
   🌐 Netzwerk-Adresse: 193.5.86.160
   📏 Netmask: 255.255.255.240
   🔢 CIDR-Notation: /28
   💻 Benötigte Hosts: 12
   🏠 Erster Host: 193.5.86.161
   🏠 Letzter Host: 193.5.86.174
   📢 Broadcast-Adresse: 193.5.86.175

🔹 **Subnetz 4:**
   🌐 Netzwerk-Adresse: 193.5.86.176
   📏 Netmask: 255.255.255.248
   🔢 CIDR-Notation: /29
   💻 Benötigte Hosts: 4
   🏠 Erster Host: 193.5.86.177
   🏠 Letzter Host: 193.5.86.182
   📢 Broadcast-Adresse: 193.5.86.183

📊 **Zusätzliche Subnetze möglich**
   🏗️ Verbleibende IPs: 72
   🏠 Anzahl zusätzlicher /30-Subnetze: 18
```

#### Error Handling:
- If the requested subnets require more IPs than the given network can provide, the program will display an error:
  ```commandline
  ❌ Error: The requested subnets require 300 IPs, but the network only has 256 available.
  ```
- If specific host requirements cannot fit within the remaining available addresses, they are skipped with a warning.

---

## Additional Notes

- The script assumes a CIDR network (e.g., `/24`), so please provide input in this format.
- The subnetting process starts with the largest host requirement to optimize the allocation of IPs.

For any issues or questions, feel free to open an issue in this repository!