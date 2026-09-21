import socket
import subprocess
import platform


def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "Unavailable"


def get_hostname():
    return socket.gethostname()


def get_gateway():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["ipconfig"],
                capture_output=True,
                text=True
            )

            for line in result.stdout.splitlines():
                if "Default Gateway" in line:
                    gateway = line.split(":")[-1].strip()

                    if gateway:
                        return gateway

    except Exception:
        pass

    return "Unavailable"


def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "CONNECTED"
    except OSError:
        return "NOT CONNECTED"


def main():
    print("=" * 45)
    print("          NETWORK ANALYZER")
    print("=" * 45)

    print(f"\nHostname:       {get_hostname()}")
    print(f"Local IP:       {get_local_ip()}")
    print(f"Default Gateway:{get_gateway()}")
    print(f"Internet:       {check_internet()}")

    print("\n" + "=" * 45)
    print("Network diagnostic complete.")
    print("=" * 45)


if __name__ == "__main__":
    main()