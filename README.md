# computer_networks

Some helper programs


## converter.py

Example output

```bash
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
```bash
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
```bash
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
```bash
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


## subnet_converter

example output

```bash
 ~/Doc/p/computer_networks master +3 ❯ python3 subnet_converter
Gib die IPv4-Adresse mit Präfix (z.B. 193.5.86.0/24) ein: 193.5.86.0/24
Gib die benötigten Hosts als Liste an (z.B. 4,12,17,67): 4

📊 Netzwerkinformationen:
🌍 Netzwerkadresse: 193.5.86.0/24
📏 Verfügbare IPs: 256

📊 Berechnete Subnetze:

🔹 **Subnetz 1:**
   🌐 Netzwerk-Adresse: 193.5.86.0
   📏 Netmask: 255.255.255.248
   🔢 CIDR-Notation: /29
   💻 Benötigte Hosts: 4
   🏠 Erster Host: 193.5.86.1
   🏠 Letzter Host: 193.5.86.6
   📢 Broadcast-Adresse: 193.5.86.7

📊 **Zusätzliche Subnetze möglich**
   🏗️ Verbleibende IPs: 248
   🏠 Anzahl zusätzlicher /30-Subnetze: 62
```
```bash
 ~/Doc/p/computer_networks master +3 ❯ python3 subnet_converter
Gib die IPv4-Adresse mit Präfix (z.B. 193.5.86.0/24) ein: 193.5.86.0/24
Gib die benötigten Hosts als Liste an (z.B. 4,12,17,67): 12

📊 Netzwerkinformationen:
🌍 Netzwerkadresse: 193.5.86.0/24
📏 Verfügbare IPs: 256

📊 Berechnete Subnetze:

🔹 **Subnetz 1:**
   🌐 Netzwerk-Adresse: 193.5.86.0
   📏 Netmask: 255.255.255.240
   🔢 CIDR-Notation: /28
   💻 Benötigte Hosts: 12
   🏠 Erster Host: 193.5.86.1
   🏠 Letzter Host: 193.5.86.14
   📢 Broadcast-Adresse: 193.5.86.15

📊 **Zusätzliche Subnetze möglich**
   🏗️ Verbleibende IPs: 240
   🏠 Anzahl zusätzlicher /30-Subnetze: 60
```
```bash
 ~/Doc/p/computer_networks master +3 ❯ python3 subnet_converter
Gib die IPv4-Adresse mit Präfix (z.B. 193.5.86.0/24) ein: 193.5.86.0/24
Gib die benötigten Hosts als Liste an (z.B. 4,12,17,67): 17

📊 Netzwerkinformationen:
🌍 Netzwerkadresse: 193.5.86.0/24
📏 Verfügbare IPs: 256

📊 Berechnete Subnetze:

🔹 **Subnetz 1:**
   🌐 Netzwerk-Adresse: 193.5.86.0
   📏 Netmask: 255.255.255.224
   🔢 CIDR-Notation: /27
   💻 Benötigte Hosts: 17
   🏠 Erster Host: 193.5.86.1
   🏠 Letzter Host: 193.5.86.30
   📢 Broadcast-Adresse: 193.5.86.31

📊 **Zusätzliche Subnetze möglich**
   🏗️ Verbleibende IPs: 224
   🏠 Anzahl zusätzlicher /30-Subnetze: 56
```
```bash
 ~/Doc/p/computer_networks master +3 ❯ python3 subnet_converter
Gib die IPv4-Adresse mit Präfix (z.B. 193.5.86.0/24) ein: 193.5.86.0/24
Gib die benötigten Hosts als Liste an (z.B. 4,12,17,67): 67

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

📊 **Zusätzliche Subnetze möglich**
   🏗️ Verbleibende IPs: 128
   🏠 Anzahl zusätzlicher /30-Subnetze: 32
```