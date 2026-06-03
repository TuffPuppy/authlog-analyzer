import re

def main():
    log_file = "sample-logs/secure.log"
    pattern = r"Failed password for (invalid user)?(?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
    try:
        with open(log_file, "r") as file:
            ip_counts = {}
            for line in file:
                match = re.search(pattern, line)

                if match:                    
                    user = match.group("user")
                    ip = match.group("ip")

                    if ip in ip_counts:
                        ip_counts[ip] += 1
                    else:
                        ip_counts[ip] = 1
                    print()
        print("\n=========================")
        print("Suspicious IP Report")
        print("=========================\n")
        for ip, count in ip_counts.items():

            if count <= 3:
                severity = "LOW"
            elif count <= 5:
                severity = "MEDIUM"
            else:
                severity = "HIGH"

            print(f"IP Address: {ip}")
            print(f"Failed Attempts: {count}")
            print(f"Severity: {severity}")
            print()

    except FileNotFoundError:
        print(f"Error: {log_file} not found.")


if __name__ == "__main__":
    main()

