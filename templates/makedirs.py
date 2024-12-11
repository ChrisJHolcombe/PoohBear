import os

# Base directory for the honeypot files
BASE_DIR = "honeypot_files"

# Structure to create
directory_structure = {
    "Documents": {
        "Passwords": {
            "password_list.txt": "admin:123456\nroot:password123\nuser:qwerty",
            "encrypted_passwords.csv": "username,password_hash\nadmin,e10adc3949ba59abbe56e057f20f883e\nroot,5f4dcc3b5aa765d61d8327deb882cf99",
        },
        "financial_report_2024.pdf": "This is a mock financial report for 2024. Nothing here is real.",
        "secret_meeting_notes.docx": "These are secret meeting notes for a project.",
    },
    "Photos": {
        "vacation_photos.zip": "Fake vacation photos archive.",
        "private_photos": {
            "photo001.jpg": "This is a fake photo file.",
        },
    },
    "Videos": {
        "confidential_interview.mp4": "Mock interview footage.",
        "surveillance_footage": {
            "footage_2024-12-01.mp4": "Fake surveillance footage.",
        },
    },
    "file1.txt": "This is a root-level text file.",
    "README.md": "Welcome to the honeypot! Nothing here is real.",
}

# Function to create the structure
def create_honeypot_files(base_dir, structure):
    for name, content in structure.items():
        path = os.path.join(base_dir, name)
        if isinstance(content, dict):
            # Create directory
            os.makedirs(path, exist_ok=True)
            # Recursively create subdirectories/files
            create_honeypot_files(path, content)
        else:
            # Create file with content
            with open(path, "w") as file:
                file.write(content)

# Create the honeypot directory and files
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
create_honeypot_files(BASE_DIR, directory_structure)

print(f"Honeypot files created in '{BASE_DIR}'.")
