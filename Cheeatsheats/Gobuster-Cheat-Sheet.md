


# 🚪 Gobuster Cheat Sheet
Personal cheat sheet with Gobuster commands used in CTFs, pentesting, and SOC analysis.

---

## 📚 Table of Contents

- [🚪 Gobuster Cheat Sheet](#gobuster-cheat-sheet)
- [What is Gobuster?](#what-is-gobuster)
- [Example](#example)
- [🌐 Basic Gobuster Commands](#basic-gobuster-commands)
- [🧭 Advanced Modes](#advanced-modes)
- [🛡️ Bypass Techniques](#bypass-techniques)
- [🧪 Example Use Cases](#example-use-cases)
- [💬 Author's Note](#authors-note)


---

## What is Gobuster?
Gobuster is a tool used for directory and file brute-forcing on web servers. It helps discover hidden directories, files, and DNS subdomains by systematically trying many possible names from a wordlist. This is useful for penetration testing to find resources that are not linked publicly but exist on the server.

### Example 

Website:` http://example.com`

Hidden directory: `/admin`

Usually, if you visit `http://example.com/admin`, you might find an admin panel or some control page that isn't linked publicly on the main site.

Gobuster tries to discover such directories by brute forcing many possible names from a wordlist, for example:
```
gobuster dir -u http://example.com -w /path/to/wordlist.txt
```


---

## 🌐 Basic Gobuster Commands

| Command | Description |
|--------|-------------|
| `gobuster dir -u http://example.com -w wordlist.txt` | Basic directory brute-force scan |
| `gobuster dir -u https://example.com -w wordlist.txt -k` | Ignore SSL certificate errors |
| `gobuster dir -u http://example.com -w wordlist.txt -x php,txt,html` | Try file extensions (e.g., .php, .txt, .html) |
| `gobuster dir -u http://example.com -w wordlist.txt -t 50` | Set 50 threads for faster scanning |
| `gobuster dir -u http://example.com -w wordlist.txt -b 403,404` | Ignore status codes (403, 404) |
| `gobuster dir -u http://example.com -w wordlist.txt -a "Googlebot"` | Spoof user-agent (bypass basic protections) |
| `gobuster dir -u http://example.com -w wordlist.txt -H "X-Forwarded-For: 127.0.0.1"` | Spoof IP address via HTTP header |

---

## 🧭 Advanced Modes

| Command | Description |
|--------|-------------|
| `gobuster vhost -u http://example.com -w subdomains.txt` | Discover virtual hosts |
| `gobuster dns -d example.com -w subdomains.txt` | Discover DNS subdomains |
| `gobuster fuzz -u http://example.com/FUZZ -w wordlist.txt` | General-purpose fuzzing using FUZZ keyword |

---

## 🛡️ Bypass Techniques

| Technique | Command |
|----------|---------|
| **User-Agent Spoofing** | `-a "Mozilla/5.0"` or `-a "Googlebot"` |
| **Fake IP Address** | `-H "X-Forwarded-For: 127.0.0.1"` |
| **Ignore SSL Errors** | `-k` |
| **Ignore Status Codes** | `-b 403,404` |
| **Try File Extensions** | `-x php,html,txt,bak,zip` |

---

## 🧪 Example Use Cases

1. **Fast, stealthy directory brute-force**
   ```bash
   gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -t 50 -a "Mozilla/5.0" -b 403



💬 Author's Note
This list was compiled for your own use and practice through CTF challenges and test environments like TryHackMe and Hack The Box.
Do not use these commands on networks without permission. 🛡️
