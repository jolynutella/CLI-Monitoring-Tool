import argparse
from .snapshot import SystemMonitor

def main():
    parser = argparse.ArgumentParser(description="System monitoring tool.")
    parser.add_argument("-i", "--interval", type=int, default=30, help="Interval between snapshots in seconds")
    parser.add_argument("-f", "--output-file", default="snapshot.json", help="Output file name")
    args = parser.parse_args()

    monitor = SystemMonitor(args.interval, args.output_file)
    monitor.run()

if __name__ == "__main__":
    main()
