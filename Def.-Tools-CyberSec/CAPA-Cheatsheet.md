# CAPA Output – What to Analyze

## 1. Basic File Information
- Hashes (MD5 / SHA1 / SHA256)  
- OS, file format, architecture  
Used for sample identification and verification.

## 2. MITRE ATT&CK Techniques
Examples: T1027, T1059.001, T1053.005  
Shows which techniques the malware implements (obfuscation, execution, persistence, etc.).

## 3. MBC Objective & Behavior
Examples: DATA :: Encode Data, ANTI-STATIC :: Executable Code Obfuscation  
Explains malware behavior, capabilities, and purpose.

## 4. Micro-Behaviors
- Process creation  
- Memory allocation  
- File read/write/delete  
Low-level actions the malware performs.

## 5. Persistence Indicators
Example: Scheduled Task  
Shows the ability to remain active across reboots.

## 6. Communication Capabilities
Example: HTTP communication  
Indicates possible command-and-control or data exfiltration.

## 7. Anti-Analysis / Evasion
Examples: VM detection, argument obfuscation, stack strings  
Shows attempts to evade sandboxes, debuggers, and static/static analysis.

---

# Short Interpretation Example
- Creates processes → can launch commands, scripts, or other binaries.  
- Allocates memory → possible unpacking or code injection.  
- File operations → reads, writes, deletes, or creates directories.  
- Persistence via Scheduled Tasks → stays active.  
- HTTP communication → can send and receive data.  
- Evasion and obfuscation → avoids analysis.  
- MAEC: "Launcher" → acts as a loader for another payload.

Summary: A suspicious loader with evasion, persistence, and external communication capabilities.
