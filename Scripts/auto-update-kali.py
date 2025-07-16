import subprocess

def auto_update():
    print("[*] Running apt update...")
    subprocess.run(["sudo", "apt", "update"], check=True)

    print("[*] Running apt upgrade -y...")
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)

    print("[*] Running apt autoremove -y...")
    subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)

    print("[*] Update Done!")

if __name__ == "__main__":
    try:
        auto_update()
    except subprocess.CalledProcessError as e:
        print(f"[!] Fail,try agian! : {e}")

