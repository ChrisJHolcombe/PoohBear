# PoohBear

PoohBear is a customizable honeypot designed to detect and log unauthorized access attempts. It simulates a realistic file directory structure to entice attackers and gather valuable insights into their behavior.

## Features

- **Realistic Directory Structure**: Mimics legitimate files and folders, including enticing file names like `password_list.txt` and `financial_report_2024.pdf`.
- **Logging**: Records all access attempts, including details about the accessed files or folders, and logs them to `PoohBear.log`.
- **Socket Listener**: Operates a separate socket-based honeypot to catch unauthorized connections.
- **Web Interface**: Built with Flask, providing a user-friendly interface to interact with the honeypot.
- **Dynamic Content**: Automatically generates a directory structure with nested folders and files.

## Installation

### Prerequisites

- Python 3.8+
- Flask

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ChrisJHolcombe/PoohBear-Honeypot.git
   cd PoohBear
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the honeypot:
   ```bash
   python poohbear.py
   ```

## Directory Structure

```
honeypot_files/
├── Documents/
│   ├── Passwords/
│   │   ├── password_list.txt
│   │   └── encrypted_passwords.csv
│   ├── financial_report_2024.pdf
│   └── secret_meeting_notes.docx
├── Photos/
│   ├── vacation_photos.zip
│   └── private_photos/
│       └── photo001.jpg
├── Videos/
│   ├── confidential_interview.mp4
│   └── surveillance_footage/
│       └── footage_2024-12-01.mp4
├── file1.txt
└── README.md
```

## How It Works

1. **Flask Application**:
   - Hosts a web-based interface showing the honeypot directory structure.
   - Users (or attackers) can click on files and folders to access them.
   - Logs all interactions in `access_log.txt`.

2. **Socket Listener**:
   - Runs a separate honeypot on a configurable port.
   - Captures unauthorized connection attempts and logs them to `PoohBear.log`.

## Customization

- Modify the `honeypot_files` directory to include your own custom structure and files.
- Update the Flask templates to change the look and feel of the web interface.

## Logging

- `access_log.txt`: Logs all file and folder access attempts.
- `PoohBear.log`: Logs socket-based connection attempts.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

## Disclaimer

This honeypot is for educational and research purposes only. Unauthorized use in a production environment or against unauthorized parties may violate applicable laws and regulations. Use responsibly.

