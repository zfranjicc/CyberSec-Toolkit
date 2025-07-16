## ⚙️What is SSH?

----


## ⚙️ SSH Cheat Sheet – Table of Contents

- ⚙️ [What is SSH?](#what-is-ssh)
- 📡 [What is SSH Used For?](#what-is-ssh-used-for)
- 💻 [How to Use SSH](#how-to-use-ssh)
- 🛠️ [Useful SSH Command Options](#useful-ssh-command-options)
- 🔑 [Security Tips](#security-tips)
- ⚠️ [For Educational Purposes Only](#for-educational-purposes-only)



---
**SSH** (Secure Shell) is a protocol that allows secure connection and management of a remote computer (server) over a network. It is used for secure access to the shell on a remote machine, meaning you can control the server as if you were physically in front of it.

## 📡What is SSH used for?

- Secure login to a remote server
- Managing files and directories on the remote machine
- Running commands on the remote system
- Secure data transfer between computers (using e.g. `scp` or `rsync` over SSH)
- Tunneling and port forwarding

## 💻How to use SSH?

---

📝Basic syntax to connect:
---
```bash
ssh username@ip_address_or_domain

```
Example
```
ssh ssh@39.133.13

```
"ssh" is the command to start the SSH client

"ssh@39.133.13" means you want to connect to the server at IP 39.133.13 with username ssh(or someting diffrent)

What happens after running the command?
You will be prompted to enter the password for the ssh user on the server 39.133.13

If it’s your first time, you may see a message asking to add the server to the known hosts (known_hosts file)

After successful authentication, you get access to the remote machine’s terminal

## 🛠️Useful SSH command options

---

```
-p PORT — specify a port if SSH server uses a non-standard port (default is 22)

```

```
ssh -p 2222 user@server.com

```

-i /path/to/private_key — specify a private key file for authentication


```
ssh -i ~/.ssh/id_rsa user@server.com
```

ssh -v — verbose mode for detailed connection info, useful for debugging


```
ssh -v user@server.com

```
## 🔑Security tips

---

○ Use strong passwords or SSH key authentication

○ Avoid logging in as root; use a regular user with sudo instead

○ Keep the SSH server updated

○ Consider disabling password login and use only key-based authentication


## ⚠️ For Educational Purposes Only

This cheat sheet is provided for learning and practicing SSH in a safe and responsible manner.  
Always use your skills ethically and with permission on systems you own or are authorized to access.
