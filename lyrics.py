import sys
import time

def main():
    lirik = [
        ("Maybe we get married one day, but who knows?", 0.1, 3.0),
        ("Think I'll take that thought to the grave, but who knows?", 0.09, 3.0  ),
        ("I know that I'll love you always", 0.11, 0.25),
        ("Yeah girl you, and I like that", 0.13, 7.0)
    ]

    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    print(f"\n{BOLD}{CYAN}>>> Daniel Caesar - Who Knows <<<{RESET}\n")

    for baris, speed, pause in lirik:
        for char in baris:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        
        print("")
        time.sleep(pause)
 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBerhenti...")