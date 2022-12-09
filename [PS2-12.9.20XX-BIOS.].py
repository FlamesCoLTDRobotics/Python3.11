# Import the necessary libraries
import requests
import os

# Define the main function
def main():
    # Set the URL of the PS2 BIOS on archive.org
    url = "https://discord.com/channels/933105920605552650/980146618810646629/1050921818623594618"

    # Use the requests library to download the file
    response = requests.get(url)

    # Save the file to the current directory
    with open("ps2bios.bin", "wb") as f:
        f.write(response.content)

    # Print a message to confirm that the download was successful
    print("PS2 BIOS downloaded successfully!")

# Run the main function
if __name__ == "__main__":
    main()
