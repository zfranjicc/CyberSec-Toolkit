##  🛠️What is Meterpreter?
Meterpreter is an advanced Metasploit payload that allows interaction with the target system through a command-line interface. It runs in memory (RAM) without writing files to disk, helping it evade antivirus detection.

---

## 🛠️ Meterpreter Cheat Sheet – Table of Contents

- 🛠️ [What is Meterpreter?](#what-is-meterpreter)
- 🔍 [How it Works?](#how-it-works)
- 📁 [Core Commands](#core-commands)
- 📂 [File System Commands](#file-system-commands)
- 🌐 [Networking Commands](#networking-commands)
- 🖥️ [System Commands](#system-commands)
- 🧠 [User Activity & Keystroke Logging](#user-activity--keystroke-logging)
- 📸 [Webcam & Audio Commands](#webcam--audio-commands)
- 🔐 [Privilege & Credential Commands](#privilege--credential-commands)
- ⚠️ [Important Notes](#important-notes)


---

### 🔍How it works?
- Does not leave traces on disk (no .exe or .dll files).
- Uses encrypted communication to avoid detection by IDS/IPS systems.
- Masquerades as legitimate processes like spoolsv.exe instead of appearing as "meterpreter.exe".
Example:
After exploiting a target (via MS17-010), the getpid command shows the active Meterpreter process ID.
For instance, PID 1304 → spoolsv.exe.
Even checking the loaded DLLs won’t reveal anything suspicious like “meterpreter.dll”


> Although stealthy, modern antivirus software 🧩 can still detect Meterpreter.


🛠️ Meterpreter Commands Cheat Sheet
Use help in any Meterpreter session to list available commands:
```
meterpreter > help
```

## 📁 Core Commands

| Command     | Description                                    |
|-------------|------------------------------------------------|
| `?`, `help` | Show help menu                                 |
| `background`| Backgrounds the current session                |
| `bg`        | Alias for `background`                         |
| `bgkill`    | Kill a background Meterpreter script           |
| `bglist`    | List running background scripts                |
| `bgrun`     | Run a script in background                     |
| `channel`   | Manage active channels                         |
| `close`     | Close a channel                                |
| `exit`      | Exit the Meterpreter session                   |
| `guid`      | Get the session GUID                           |
| `info`      | Show info about a post module                  |
| `irb`       | Open interactive Ruby shell                    |
| `load`      | Load Meterpreter extensions                    |
| `migrate`   | Migrate Meterpreter to another process         |
| `run`       | Run a Meterpreter script or post module        |
| `sessions`  | Switch between active sessions                 |

---

## 📂 File System Commands

| Command  | Description                  |
|----------|------------------------------|
| `cd`     | Change directory             |
| `ls`, `dir` | List files in current directory |
| `pwd`    | Print working directory      |
| `edit`   | Edit a file                 |
| `cat`    | Show file content           |
| `rm`     | Delete a file               |
| `search` | Search for files            |
| `upload` | Upload file or folder       |
| `download` | Download file or folder    |

---

## 🌐 Networking Commands

| Command   | Description                      |
|-----------|----------------------------------|
| `arp`     | View ARP cache                   |
| `ifconfig`| Show network interfaces          |
| `netstat` | Display active network connections |
| `portfwd` | Forward local port to remote service |
| `route`   | View or modify routing table     |

---

## 🖥️ System Commands

| Command   | Description                      |
|-----------|----------------------------------|
| `clearev` | Clear event logs                 |
| `execute` | Execute a system command          |
| `getpid`  | Get current process ID            |
| `getuid`  | Get current user ID               |
| `kill`    | Kill a process by PID             |
| `pkill`   | Kill a process by name            |
| `ps`      | List running processes            |
| `reboot`  | Reboot the remote system          |
| `shell`   | Drop into system shell            |
| `shutdown`| Shut down the remote system       |
| `sysinfo` | Display system information        |

---

## 🧠 User Activity & Keystroke Logging

| Command        | Description                  |
|----------------|------------------------------|
| `idletime`     | Show seconds of user inactivity |
| `keyscan_start`| Start logging keystrokes     |
| `keyscan_dump` | Dump captured keystrokes     |
| `keyscan_stop` | Stop logging keystrokes      |

---

## 📸 Webcam & Audio Commands

| Command        | Description                  |
|----------------|------------------------------|
| `screenshare`  | Share live desktop screen    |
| `screenshot`   | Take a screenshot of desktop |
| `record_mic`   | Record microphone audio for X seconds |
| `webcam_chat`  | Start webcam video chat      |
| `webcam_list`  | List available webcams       |
| `webcam_snap`  | Take a snapshot from a webcam|
| `webcam_stream`| Stream webcam video          |

---

## 🔐 Privilege & Credential Commands

| Command    | Description                           |
|------------|-------------------------------------|
| `getsystem`| Attempt to elevate privileges to SYSTEM level |
| `hashdump` | Dump contents of SAM password database |


## ⚠️ Important Notes
> This guide is for educational purposes only and for testing in your own controlled environments.
> Do NOT use these techniques on networks or machines without explicit permission!
