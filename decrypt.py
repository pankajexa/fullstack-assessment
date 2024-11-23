"""
timer-assessment/
├── README.md                    # Public initial instructions
├── decrypt.py                   # Decryption script
├── encrypted/
│   └── INSTRUCTIONS.enc         # Encrypted detailed instructions
└── src/                        # Starter code structure
    ├── .gitkeep
    └── utils/
        └── github.js           # Sample GitHub API helper (optional)
"""

# decrypt.py
from cryptography.fernet import Fernet
import base64
import json
import os

def generate_key():
    """Generate a key based on git commit hash"""
    try:
        with os.popen('git rev-parse HEAD') as pipe:
            commit_hash = pipe.read().strip()
        
        if not commit_hash:
            return None
            
        key = base64.b64encode(commit_hash.encode()[:32].ljust(32, b'0'))
        return key
    except:
        return None

# def decrypt_instructions(encrypted_file='encrypted/INSTRUCTIONS.enc'):
#     """Decrypt the instructions and write them to markdown files"""
#     try:
#         key = generate_key()
#         if not key:
#             print("Error: This script must be run in a git repository after forking")
#             return None
            
#         with open(encrypted_file, 'r') as f:
#             encrypted_data = base64.b64decode(f.read())
            
#         cipher_suite = Fernet(key)
#         decrypted_data = cipher_suite.decrypt(encrypted_data)
#         instructions = json.loads(decrypted_data)
        
#         # Write detailed instructions to markdown files
#         for filename, content in instructions.items():
#             with open(filename, 'w') as f:
#                 f.write(content)
                
#         print("\n✨ Instructions decrypted successfully!")
#         print("\nCreated the following files:")
#         for filename in instructions.keys():
#             print(f"- {filename}")
            
#     except FileNotFoundError:
#         print(f"Error: Could not find {encrypted_file}")
#     except Exception as e:
#         print(f"Error decrypting instructions: {str(e)}")

def encrypt_instructions():
    """Utility function to encrypt the initial instructions"""
    try:
        initial_commit_hash = "aa09e60337f6eb7a36791ed40720d0edc1a56f36"
        key = base64.b64encode(initial_commit_hash.encode()[:32].ljust(32, b'0'))
        
        instructions = {
            "TASK.md": """# Build Your Own Timer Challenge 🕒

## Overview
This is a unique challenge where you'll build a timer that records how long it took you to build it! Your task is to create a full-stack application that tracks your build time from the moment you forked this repository until you complete the implementation.

## Core Requirements

### Backend Development
1. Create an API with the tech stack of your choice
2. Implement database schema with the following minimum fields:
   - assessment_start_time (get this from GitHub API fork time)
   - assessment_end_time (when user clicks complete)
   - any additional fields you find necessary

### Frontend Development
1. Build a digital stop clock display showing:
   - Time elapsed since you started (fork time)
   - Final build time (once completed)
2. Implement a "Complete" button that:
   - Records the end time in the database
   - Freezes the timer display
   - Shows total time taken

### Technical Requirements
1. Use any frontend framework/library of your choice
2. Use any backend framework of your choice
3. Use any database of your choice (SQL or NoSQL)
4. Host the application on Vercel or any equivalent platform
5. Ensure the application is responsive
6. Include proper error handling

### Bonus Points
- Clean, well-documented code
- Proper Git commit history
- Additional features (e.g., pause/resume, lap times)
- Creative UI/UX design
- Comprehensive testing

## Important Notes
- Start ONLY when you're ready - fork time is your start time
- Document any AI tools used in SUBMISSION.md
- Focus on code quality and user experience
""",
            "SETUP.md": """# Development Setup Guide

## Prerequisites
1. GitHub account
2. Node.js/Python/Any required runtime for your chosen stack
3. Database setup (local or cloud)
4. Vercel account (or equivalent)

## Getting Started
1. Fork this repository
2. Run `python decrypt.py` to view full instructions
3. Set up your development environment:
   - Initialize your project with your chosen framework
   - Set up version control
   - Configure your database
   - Set up deployment platform

## GitHub API Integration
To get your fork time:
1. Use GitHub's API: `GET /repos/{owner}/{repo}/forks`
2. Look for your fork's `created_at` timestamp
3. Store this as your start time

## Development Tips
1. Plan your database schema first
2. Build and test the timer logic separately
3. Integrate frontend and backend incrementally
4. Test deployment early
""",
            "SUBMISSION.md": """# Submission Template

## Project Information
- Name:
- Email:
- Repository URL:
- Deployed Application URL:

## Implementation Details
### Tech Stack Used
- Frontend:
- Backend:
- Database:
- Deployment Platform:

### Time Taken
- Start Time (Fork Time):
- End Time:
- Total Duration:

### Features Implemented
1.
2.
3.

### Database Schema
```sql
-- Include your schema here
```

### AI Tools Used
| Tool | Purpose | How it was used |
|------|----------|----------------|
|      |          |                |

### Challenges Faced
1.
2.

### Screenshots
- [Include screenshots of your application]

## Checklist
- [ ] Backend API implemented
- [ ] Frontend timer implemented
- [ ] Database integration complete
- [ ] Application deployed
- [ ] Code documented
- [ ] Screenshots attached
- [ ] All times recorded
- [ ] Email sent with submission
"""
        }
        
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(json.dumps(instructions).encode())
        
        os.makedirs('encrypted', exist_ok=True)
        with open('encrypted/INSTRUCTIONS.enc', 'wb') as f:
            f.write(base64.b64encode(encrypted_data))
            
        print("Instructions encrypted successfully!")
        
    except Exception as e:
        print(f"Error encrypting instructions: {str(e)}")

if __name__ == "__main__":
    # Comment out the decryption function
    # decrypt_instructions()
    
    # Uncomment the encryption function
    encrypt_instructions()