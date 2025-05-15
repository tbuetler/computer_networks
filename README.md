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

```bash
$ python3 converter.py
🔢 Give a number or IPv4 address: 193.5.80.10

📊 Results:
Input:                 193.5.80.10 (ipv4)
Decimal:               3238350858
Binary (8-bit):        11000001 00000101 01010000 00001010
Octal:                 30101250012
Hexadecimal:           C105500A

🌐 IPv4 Information:
IPv4 Address:          193.5.80.10
Binary:                11000001 00000101 01010000 00001010
Network Address:       193.5.80.0
Broadcast Address:     193.5.80.255
Subnet Mask:           255.255.255.0
First Host Address:    193.5.80.1
Last Host Address:     193.5.80.254
CIDR Notation:         193.5.80.10/24
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
$ python3 subnet_converter.py
Enter the IPv4 address with prefix (e.g., 193.5.86.0/24): 193.5.86.0/24
Enter the required hosts as a list (e.g., 4,12,17,67): 12,25,8

📊 Network Information:
🌍 Network Address: 193.5.86.0/24
📏 Available IPs: 256

📊 Calculated Subnets:

🔹 **Subnet 1:**
   🌐 Network Address: 193.5.86.0
   📏 Netmask: 255.255.255.224
   🔢 CIDR Notation: /27
   💻 Requested Hosts: 25
   🏠 First Host: 193.5.86.1
   🏠 Last Host: 193.5.86.30
   📢 Broadcast Address: 193.5.86.31

🔹 **Subnet 2:**
   🌐 Network Address: 193.5.86.32
   📏 Netmask: 255.255.255.240
   🔢 CIDR Notation: /28
   💻 Requested Hosts: 12
   🏠 First Host: 193.5.86.33
   🏠 Last Host: 193.5.86.46
   📢 Broadcast Address: 193.5.86.47

🔹 **Subnet 3:**
   🌐 Network Address: 193.5.86.48
   📏 Netmask: 255.255.255.248
   🔢 CIDR Notation: /29
   💻 Requested Hosts: 8
   🏠 First Host: 193.5.86.49
   🏠 Last Host: 193.5.86.54
   📢 Broadcast Address: 193.5.86.55

📊 **Additional Subnets Possible**
   🏗️ Remaining IPs: 200
   🏠 Number of additional /30 Subnets: 50
```

#### Error Handling:
- If the requested subnets require more IPs than the given network can provide, the program will display an error:
  ```bash
  ❌ Error: The requested subnets require 300 IPs, but the network only has 256 available.
  ```
- If specific host requirements cannot fit within the remaining available addresses, they are skipped with a warning.

---

## Additional Notes

- The script assumes a CIDR network (e.g., `/24`), so please provide input in this format.
- The subnetting process starts with the largest host requirement to optimize the allocation of IPs.

For any issues or questions, feel free to open an issue in this repository!