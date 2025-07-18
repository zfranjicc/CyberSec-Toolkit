# 🔐 Common Ports Cheat Sheet

This table lists the most commonly used network ports, their purpose, and security notes. Useful for learning, pentesting, and security analysis.

## 📒 Ports and Their Purpose

| Port | Protocol | Service                | Description                                      | Security Note                                   |
|------|----------|------------------------|--------------------------------------------------|-------------------------------------------------|
| 20   | TCP      | FTP (Data)             | File transfer (data channel)                     | Unencrypted – vulnerable to MITM attacks        |
| 21   | TCP      | FTP (Control)          | Manages FTP sessions                             | Weak auth, no encryption                        |
| 22   | TCP      | SSH                    | Remote login, tunneling                          | Bruteforce attacks common if exposed            |
| 23   | TCP      | Telnet                 | Remote login (deprecated)                        | Unencrypted – highly insecure                   |
| 25   | TCP      | SMTP                   | Sending emails                                   | Can be abused for spam (open relay)            |
| 53   | UDP/TCP  | DNS                    | Resolves domain names to IPs                     | DNS spoofing, amplification attacks             |
| 67   | UDP      | DHCP (server)          | Assigns IPs to clients                           | Can be spoofed (rogue DHCP)                     |
| 68   | UDP      | DHCP (client)          | Receives IP from DHCP server                     | —                                               |
| 80   | TCP      | HTTP                   | Unencrypted web traffic                          | Use HTTPS instead – vulnerable to MITM          |
| 110  | TCP      | POP3                   | Email retrieval                                  | Use POP3S (995) instead                         |
| 123  | UDP      | NTP                    | Time synchronization                             | Can be used for DDoS reflection                 |
| 135  | TCP      | Microsoft RPC          | Windows network services                         | Target of exploits (e.g., EternalBlue)          |
| 139  | TCP      | NetBIOS                | Windows file sharing                             | Can reveal shared resources                     |
| 143  | TCP      | IMAP                   | Reading emails                                   | Use IMAPS (993) instead                         |
| 161  | UDP      | SNMP                   | Network device management                        | Default creds, info disclosure risk             |
| 389  | TCP/UDP  | LDAP                   | Directory access (users, devices)                | LDAP injection, use LDAPS (636)                 |
| 443  | TCP      | HTTPS                  | Encrypted web traffic                            | Safer, but certs/configs can be weak            |
| 445  | TCP      | SMB                    | Windows file sharing                             | Critical – common ransomware entry point        |
| 465  | TCP      | SMTPS                  | Secure email sending                             | Secure version of SMTP                          |
| 514  | UDP      | Syslog                 | Network log reporting                            | Can expose sensitive data                       |
| 993  | TCP      | IMAPS                  | Secure email reading                             | Encrypted – safer than IMAP                     |
| 995  | TCP      | POP3S                  | Secure email retrieval                           | Encrypted – safer than POP3                     |
| 1433 | TCP      | MS SQL Server          | Microsoft SQL databases                          | Target for bruteforce/SQL injection             |
| 1521 | TCP      | Oracle DB              | Oracle databases                                 | Vulnerable to remote exploits if exposed        |
| 1723 | TCP      | PPTP VPN               | VPN tunneling                                    | Weak encryption – not recommended               |
| 3306 | TCP      | MySQL                  | MySQL database access                            | Dangerous if internet-facing                    |
| 3389 | TCP      | RDP                    | Windows Remote Desktop                           | Common bruteforce/ransomware entry point        |
| 5432 | TCP      | PostgreSQL             | PostgreSQL database access                       | Bruteforce risk if exposed                      |
| 5900 | TCP      | VNC                    | Remote desktop access                            | Unencrypted – MITM risk                         |
| 8080 | TCP      | HTTP (proxy/test)      | Alternate HTTP port, dev/test servers            | Often forgotten, can leak sensitive info        |

---

> ✅ **Tip**: If you find any of these ports open on a public system (e.g., 23, 445, 3306), it's often a **red flag** and a common entry point in real-world attacks.
