# website-blocker-and-unblocker

Overview
This Python script provides a simple Graphical User Interface (GUI) for blocking and unblocking websites on a Windows system by manipulating the hosts file. The application is built using the Tkinter library, making it user-friendly and accessible.

Features
Block Website: Allows the user to input a website and block it by adding an entry to the system's hosts file.
Unblock Website: Permits the user to unblock a previously blocked website by removing its entry from the hosts file.
Informative Messages: Displays informative pop-up messages to notify the user about the success or failure of blocking/unblocking operations.

Requirements
Python: The script requires a Python interpreter to run. You can download Python from python.org.
Tkinter: Tkinter is included with most Python installations, but ensure it is available on your system.
How to Use
Run the Script: Execute the script by running it using a Python interpreter. The GUI window will appear.

Blocking a Website:

Enter the website's domain (e.g., example.com) in the provided entry field.
Click the "Block Website" button.

Unblocking a Website:

Enter the website's domain that you want to unblock.
Click the "Unblock Website" button.
Notifications:

Informative pop-up messages will appear, confirming the success or notifying about any errors.

Important Notes
Administrator Privileges: Ensure that the script is executed with administrative privileges to modify the hosts file.
Windows Only: This script is designed for Windows systems, as it manipulates the default hosts file location on Windows.

Customization
Hosts File Path: The script assumes the default hosts file path (C:\Windows\System32\drivers\etc\hosts). If your hosts file is located elsewhere, modify the hosts_file_path variable accordingly.

Disclaimer
Use this script responsibly, and be aware that modifying system files can have unintended consequences. Blocking critical websites may affect system functionality.
