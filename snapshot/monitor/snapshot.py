import json
import os
import psutil
import time
import argparse


class SystemMonitor:
    def __init__(self, interval, output_file):
        self.interval = interval
        self.output_file = output_file


    def get_system_snapshot(self):
        # Get system information using psutil
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        cpu = psutil.cpu_times_percent(interval=1, percpu=False)
        tasks = psutil.Process().num_threads()

        # Prepare snapshot dictionary
        snapshot = {
            "Tasks": {
                "total": tasks,
                "running": len(psutil.pids()),
                "sleeping": len(psutil.STATUS_SLEEPING),  
                "stopped": len(psutil.STATUS_STOPPED),   
                "zombie": len(psutil.STATUS_ZOMBIE)     
            },
            "%CPU": {
                "user": cpu.user,
                "system": cpu.system,
                "idle": cpu.idle
            },
            "KiB Mem": {
                "total": mem.total,
                "free": mem.available,
                "used": mem.used
            },
            "KiB Swap": {
                "total": swap.total,
                "free": swap.free,
                "used": swap.used
            },
            "Timestamp": int(time.time())
        }

        return snapshot


    def run(self):
        # Clear screen
        os.system('clear')

        # Clean output file
        open(self.output_file, 'w').close()

        try:
            with open(self.output_file, 'a') as file:
                # Infinite loop for continuous monitoring
                while True:
                    snapshot = self.get_system_snapshot()

                    # Print to console
                    print(json.dumps(snapshot), end="\r")

                    # Write to JSON file
                    json.dump(snapshot, file)
                    file.write('\n')  # Separate snapshots in JSON file by new line
                    file.flush()      # Force data to be written to disk

                    # Wait for the specified interval
                    time.sleep(self.interval)

                    # Clear screen for next output
                    os.system('clear')

        except KeyboardInterrupt:
            print("\nMonitoring stopped.")


def main():
    parser = argparse.ArgumentParser(description="System monitoring tool.")
    parser.add_argument("-i", "--interval", type=int, default=30, help="Interval between snapshots in seconds")
    parser.add_argument("-f", "--output-file", default="snapshot.json", help="Output file name")
    args = parser.parse_args()

    monitor = SystemMonitor(args.interval, args.output_file)
    monitor.run()

if __name__ == "__main__":
    main()
