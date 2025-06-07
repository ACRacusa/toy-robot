import sys
from src.simulator import Simulator


def main():
    simulator = Simulator()

    # If a file is provided as argument
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        try:
            with open(file_path) as f:
                for line in f:
                    simulator.execute(line)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
    else:
        # Interactive mode
        print("Toy Robot Simulator (type EXIT to quit)")
        while True:
            try:
                command = input("Enter command: ")
                if command.strip().upper() == "EXIT":
                    break
                simulator.execute(command)
            except KeyboardInterrupt:
                print("\nExiting.")
                break


if __name__ == "__main__":
    main()
