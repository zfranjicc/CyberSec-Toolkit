# 🐧 Linux Commands Cheat Sheet

Personal cheat sheet with essential Linux commands for beginners and intermediate users.

---

## 🐧 Linux Commands Cheat Sheet – Table of Contents

- 🔰 [First Command: Update System](#first-command-update-system)
- 🐧 [Top 20 Linux Commands](#top-20-linux-commands)
- 📂 [File Permissions & Ownership](#file-permissions--ownership)
- 🔍 [Searching and Finding Files](#searching-and-finding-files)
- 🧑‍💻 [Process Management](#process-management)
- 📡 [Networking](#networking)
- 📦 [Package Management (Debian/Ubuntu)](#package-management-debianubuntu)
- 💾 [Disk Usage and Monitoring](#disk-usage-and-monitoring)
- 🔧 [System Information and Control](#system-information-and-control)
- 📜 [Viewing Logs](#viewing-logs)
- 📚 [Miscellaneous Useful Commands](#miscellaneous-useful-commands)
- 🎯 [Example Usage](#example-usage)


---

## FIRST COMMAND

Update and upgrade system

```bash
sudo apt update && sudo apt upgrade -y
```
# 🐧 Top 20 Linux Commands


---

| 🧾 Command              | 🧠 Description                                                |
|------------------------|--------------------------------------------------------------|
| `ls`                   | List files and directories                                   |
| `cd [dir]`             | Change current directory                                     |
| `pwd`                  | Show current working directory                               |
| `mkdir [dir]`          | Create a new directory                                       |
| `rm [file]`            | Delete a file                                                |
| `rm -r [dir]`          | Delete a directory and its contents                         |
| `cp [src] [dest]`      | Copy file or directory                                       |
| `mv [src] [dest]`      | Move or rename files                                         |
| `touch [file]`         | Create an empty file                                         |
| `cat [file]`           | Display content of a file                                    |
| `nano [file]`          | Open file in Nano text editor                               |
| `clear`                | Clear the terminal screen                                    |
| `history`              | View previously used commands                                |
| `top`                  | Real-time process viewer                                     |
| `htop`                 | Interactive process viewer (better version of `top`)        |
| `ps aux`               | Display all running processes                                |
| `kill [PID]`           | Terminate a process by its PID                               |
| `chmod +x [file]`      | Make a file executable                                       |
| `ifconfig` / `ip a`    | Show IP addresses and interfaces                             |
| `sudo [command]`       | Run a command with superuser privileges                      |

---
---

# View More ⬇️

---
---

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `ls`                         | List files and directories             |
| `ls -la`                     | List all files (including hidden) with details |
| `cd /path/to/directory`      | Change directory                       |
| `pwd`                        | Print current working directory        |
| `mkdir dirname`              | Create new directory                    |
| `rm filename`                | Remove file                            |
| `rm -r dirname`              | Remove directory recursively           |
| `cp source destination`      | Copy files or directories               |
| `mv source destination`      | Move or rename files/directories        |
| `touch filename`             | Create empty file or update timestamp  |
| `cat filename`               | Display file content                    |
| `head filename`              | Show first 10 lines of a file           |
| `tail filename`              | Show last 10 lines of a file            |
| `file filename`              | Identify file type                      |

---

## 📂 File Permissions & Ownership

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `chmod 755 filename`         | Change file permissions (rwxr-xr-x)    |
| `chmod +x filename`          | Add execute permission                   |
| `chown user:group filename` | Change file owner and group              |
| `ls -l`                     | Show permissions and ownership           |

---

## 🔍 Searching and Finding Files

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `find /path -name filename`  | Find files by name                      |
| `grep "text" filename`       | Search for text in a file               |
| `grep -r "text" /path`       | Recursively search text in files       |
| `locate filename`            | Quickly find files by name (database)  |

---

## 🧑‍💻 Process Management

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `ps aux`                     | List running processes                   |
| `top`                       | Interactive process viewer               |
| `htop`                      | Enhanced interactive process viewer (if installed) |
| `kill PID`                  | Terminate process by PID                  |
| `kill -9 PID`               | Force kill process                        |
| `pkill process_name`        | Kill processes by name                    |

---

## 📡 Networking

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `ip a`                      | Show network interfaces and IP addresses|
| `ifconfig`                  | Show network interfaces (deprecated, but still used) |
| `ping 8.8.8.8`              | Ping a remote host                       |
| `netstat -tulnp`            | Show listening ports and programs       |
| `ss -tulnp`                 | Modern alternative to netstat            |
| `traceroute example.com`    | Show route packets take to host          |
| `curl http://example.com`   | Fetch web page or data                    |
| `wget http://example.com/file` | Download file from internet             |

---

## 📦 Package Management (Debian/Ubuntu)

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `sudo apt update`            | Update package lists                    |
| `sudo apt upgrade`           | Upgrade installed packages              |
| `sudo apt install package`  | Install new package                      |
| `sudo apt remove package`   | Remove package                           |
| `dpkg -i package.deb`       | Install .deb package                     |

---

## 💾 Disk Usage and Monitoring

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `df -h`                     | Show disk usage of file systems         |
| `du -sh /path/to/dir`       | Show total size of directory             |
| `free -h`                   | Show memory usage                        |
| `uptime`                    | Show system uptime and load average      |

---

## 🔧 System Information and Control

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `uname -a`                  | Show system information                  |
| `hostname`                  | Show or set the system hostname          |
| `date`                      | Show current date and time               |
| `whoami`                    | Show current user                        |
| `sudo reboot`               | Reboot the system                        |
| `sudo shutdown now`         | Shutdown immediately                     |

---

## 📜 Viewing Logs

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `journalctl -xe`            | Show systemd logs                        |
| `tail -f /var/log/syslog`   | Follow system log file                   |
| `dmesg`                     | Show kernel messages                     |

---

## 📚 Miscellaneous Useful Commands

| Command                      | Description                              |
|------------------------------|----------------------------------------|
| `alias`                     | Show current command aliases            |
| `history`                   | Show command history                     |
| `clear`                     | Clear terminal screen                    |
| `echo $PATH`                | Show system PATH variable                |
| `env`                       | Show environment variables               |

---

## 🎯 Example Usage

```bash
# Update and upgrade system
sudo apt update && sudo apt upgrade -y

# Create a directory and navigate into it
mkdir myfolder && cd myfolder

# Search for "error" in log files recursively
grep -r "error" /var/log/

# Find all .txt files in home directory
find ~/ -name "*.txt"

# Show processes
ps aux

# Kill a process by name
pkill firefox

# Check disk usage of home directory
du -sh ~/
