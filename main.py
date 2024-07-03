# Define PMR446 channel frequencies and CTCSS tones
pmr446_channels = {
    1: {"frequency": 446.00625, "tones": [67.0, 71.9, 74.4, 77.0, 79.7, 82.5, 85.4, 88.5]},
    2: {"frequency": 446.01875, "tones": [91.5, 94.8, 97.4, 100.0, 103.5, 107.2, 110.9, 114.8]},
    3: {"frequency": 446.03125, "tones": [118.8, 123.0, 127.3, 131.8, 136.5, 141.3, 146.2, 151.4]},
    4: {"frequency": 446.04375, "tones": [156.7, 162.2, 167.9, 173.8, 179.9, 186.2, 192.8, 203.5]},
    5: {"frequency": 446.05625, "tones": [210.7, 218.1, 225.7, 233.6, 241.8, 250.3, 69.4, 159.8]},
    6: {"frequency": 446.06875, "tones": [183.5, 189.9, 196.6, 206.5, 229.1, 254.1, 263.5, 276.6]},
    7: {"frequency": 446.08125, "tones": [79.9, 91.5, 151.4, 179.9, 254.1, 203.5, 114.8, 131.8]},
    8: {"frequency": 446.09375, "tones": [77.0, 88.5, 103.5, 123.0, 141.3, 162.2, 186.2, 210.7]},
    9: {"frequency": 446.10625, "tones": [72.4, 79.7, 85.4, 100.0, 114.8, 127.3, 141.3, 156.7]},
    10: {"frequency": 446.11875, "tones": [167.9, 173.8, 179.9, 186.2, 192.8, 203.5, 229.1, 254.1]},
    11: {"frequency": 446.13125, "tones": [67.0, 71.9, 74.4, 77.0, 79.7, 82.5, 85.4, 88.5]},
    12: {"frequency": 446.14375, "tones": [91.5, 94.8, 97.4, 100.0, 103.5, 107.2, 110.9, 114.8]},
    13: {"frequency": 446.15625, "tones": [118.8, 123.0, 127.3, 131.8, 136.5, 141.3, 146.2, 151.4]},
    14: {"frequency": 446.16875, "tones": [156.7, 162.2, 167.9, 173.8, 179.9, 186.2, 192.8, 203.5]},
    15: {"frequency": 446.18125, "tones": [210.7, 218.1, 225.7, 233.6, 241.8, 250.3, 69.4, 159.8]},
    16: {"frequency": 446.19375, "tones": [183.5, 189.9, 196.6, 206.5, 229.1, 254.1, 263.5, 276.6]}
}

def translate_channel(channel):
    if channel in pmr446_channels:
        data = pmr446_channels[channel]
        print(f"Channel {channel}:")
        print(f"  Frequency: {data['frequency']} MHz")
        print("  Tones: ", ", ".join(map(str, data["tones"])))
    else:
        print(f"Channel {channel} not found.")

def main():
    while True:
        try:
            user_input = input("Enter PMR446 channel number (1-16) or 'q' to quit: ").strip().lower()
            if user_input == 'q':
                break
            channel = int(user_input)
            translate_channel(channel)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 16 or 'q' to quit.")

if __name__ == "__main__":
    main()
