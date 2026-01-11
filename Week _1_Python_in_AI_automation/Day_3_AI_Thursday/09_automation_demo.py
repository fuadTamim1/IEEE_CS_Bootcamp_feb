"""
DAY 3 - LESSON 9: Real-World Automation Patterns
==============================================

Learning Objectives:
- Understand common automation patterns
- Learn scheduling and task automation
- Practice file automation
- Learn batch processing
- Understand workflow automation

Key Concepts:
- Automation: Automating repetitive tasks
- Scheduling: Running tasks at specific times
- Batch processing: Processing multiple items
- Workflow: Series of steps that happen together
"""

import os
import shutil
import datetime
import json

# ===== SECTION 1: File Organization Automation =====
print("=== FILE ORGANIZATION AUTOMATION ===\n")

print("""
Common automation task: Organize files by type

Use cases:
- Automatically sort Downloads folder
- Organize photos by date
- Archive old files
- Backup important documents
""")

def organize_files_by_extension(directory, dry_run=True):
    \"\"\"
    Organize files in a directory by their extension.
    dry_run=True shows what would happen without doing it.
    \"\"\"
    
    if not os.path.exists(directory):
        print(f"❌ Directory {directory} not found")
        return
    
    print(f"\nOrganizing files in: {directory}")
    if dry_run:
        print("(DRY RUN - No files will actually be moved)")
    
    file_count = 0
    folder_count = 0
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip if it's a directory
        if os.path.isdir(filepath):
            continue
        
        # Get file extension
        _, extension = os.path.splitext(filename)
        
        # Skip files without extension
        if not extension:
            continue
        
        # Create folder for this extension
        extension_folder = os.path.join(directory, extension.replace('.', ''))
        
        if dry_run:
            print(f"  Would move: {filename} -> {extension_folder}/")
        else:
            # Create folder if needed
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
                folder_count += 1
            
            # Move file
            shutil.move(filepath, os.path.join(extension_folder, filename))
        
        file_count += 1
    
    print(f"\nSummary:")
    print(f"  Files processed: {file_count}")
    print(f"  Folders created: {folder_count}")

# Example usage (dry_run=True so files aren't actually moved)
organize_files_by_extension(".", dry_run=True)


# ===== SECTION 2: Batch File Renaming =====
print("\n\n=== BATCH FILE RENAMING ===\n")

def rename_files_batch(directory, pattern, replacement):
    \"\"\"
    Rename all files matching a pattern.
    
    Example:
    rename_files_batch('.', 'old_', 'new_')
    \"\"\"
    
    if not os.path.exists(directory):
        print(f"❌ Directory {directory} not found")
        return
    
    renamed_count = 0
    
    for filename in os.listdir(directory):
        if pattern in filename:
            old_path = os.path.join(directory, filename)
            new_filename = filename.replace(pattern, replacement)
            new_path = os.path.join(directory, new_filename)
            
            # Only rename files, not directories
            if os.path.isfile(old_path):
                print(f"  {filename} -> {new_filename}")
                # os.rename(old_path, new_path)  # Uncomment to actually rename
                renamed_count += 1
    
    print(f"\nWould rename {renamed_count} files")

# Example
print("Example: Rename files starting with 'test_' to 'exam_':")
rename_files_batch(".", "test_", "exam_")


# ===== SECTION 3: Data Processing Pipeline =====
print("\n\n=== DATA PROCESSING PIPELINE ===\n")

def process_data_pipeline():
    \"\"\"
    Example of processing data through multiple stages.
    Stage 1: Collect
    Stage 2: Clean
    Stage 3: Transform
    Stage 4: Save
    \"\"\"
    
    # Stage 1: Collect (simulate reading from multiple sources)
    print("Stage 1: Collecting data...")
    raw_data = [
        {"name": "Ahmed", "score": 95, "status": " active"},
        {"name": " Sara", "score": 88, "status": "active "},
        {"name": "Ali", "score": 0, "status": "inactive"},
        {"name": "Fatima", "score": 92, "status": "active"},
    ]
    print(f"  Collected {len(raw_data)} records")
    
    # Stage 2: Clean (remove extra spaces, handle invalid data)
    print("\nStage 2: Cleaning data...")
    cleaned_data = []
    for record in raw_data:
        # Clean up whitespace
        record['name'] = record['name'].strip()
        record['status'] = record['status'].strip()
        
        # Skip invalid records
        if record['score'] == 0 or record['score'] < 0:
            print(f"  ⚠️  Skipping invalid record: {record['name']}")
            continue
        
        cleaned_data.append(record)
    
    print(f"  Cleaned: {len(cleaned_data)} valid records")
    
    # Stage 3: Transform (add derived data)
    print("\nStage 3: Transforming data...")
    transformed_data = []
    for record in cleaned_data:
        # Add grade based on score
        if record['score'] >= 90:
            grade = 'A'
        elif record['score'] >= 80:
            grade = 'B'
        else:
            grade = 'C'
        
        record['grade'] = grade
        transformed_data.append(record)
    
    print(f"  Added grade information to {len(transformed_data)} records")
    
    # Stage 4: Save
    print("\nStage 4: Saving data...")
    output_file = "processed_data.json"
    
    with open(output_file, 'w') as file:
        json.dump(transformed_data, file, indent=2)
    
    print(f"  Saved to {output_file}")
    
    # Show summary
    print("\nFinal Data:")
    for record in transformed_data:
        print(f"  {record['name']}: {record['score']} ({record['grade']})")
    
    return transformed_data

data = process_data_pipeline()


# ===== SECTION 4: Log Monitoring =====
print("\n\n=== LOG MONITORING ===\n")

def monitor_log_file(filename, error_level='ERROR'):
    \"\"\"
    Monitor a log file and alert on specific events.
    \"\"\"
    
    if not os.path.exists(filename):
        print(f"❌ Log file not found: {filename}")
        return
    
    errors = []
    warnings = []
    
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if 'ERROR' in line:
                errors.append((line_num, line.strip()))
            elif 'WARNING' in line:
                warnings.append((line_num, line.strip()))
    
    print(f"Log Analysis: {filename}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    
    if errors:
        print(f"\n⚠️  Errors found:")
        for line_num, error in errors[:5]:  # Show first 5
            print(f"  Line {line_num}: {error[:80]}...")
    
    return {'errors': len(errors), 'warnings': len(warnings)}

# Create sample log and monitor it
log_file = "app.log"
with open(log_file, 'w') as f:
    f.write("INFO: Application started\n")
    f.write("DEBUG: Initializing modules\n")
    f.write("WARNING: Deprecated function used\n")
    f.write("ERROR: Connection timeout\n")
    f.write("INFO: Retrying...\n")
    f.write("ERROR: Max retries exceeded\n")

monitor_log_file(log_file)


# ===== SECTION 5: Backup Automation =====
print("\n\n=== BACKUP AUTOMATION ===\n")

def backup_files(source_dir, backup_dir):
    \"\"\"
    Backup files from source to backup directory with timestamp.
    \"\"\"
    
    if not os.path.exists(source_dir):
        print(f"❌ Source directory not found: {source_dir}")
        return
    
    # Create backup directory with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    
    os.makedirs(backup_path, exist_ok=True)
    
    file_count = 0
    
    print(f"Backing up {source_dir} to {backup_path}")
    
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        
        # Only backup files, not directories
        if os.path.isfile(filepath):
            backup_file = os.path.join(backup_path, filename)
            # shutil.copy2(filepath, backup_file)  # Uncomment to actually backup
            print(f"  Backing up: {filename}")
            file_count += 1
    
    print(f"\n✓ Backup complete: {file_count} files")
    print(f"  Backup path: {backup_path}")
    
    return backup_path

# Example
backup_files(".", "./backups")


# ===== SECTION 6: Scheduled Tasks =====
print("\n\n=== SCHEDULED TASKS ===\n")

print("""
Ways to schedule Python scripts:

1. Task Scheduler (Windows)
   - Create task to run Python script at specific time
   - Can run daily, weekly, monthly, etc.

2. Cron (Linux/Mac)
   - Add to crontab: 0 9 * * * python /path/to/script.py
   - This runs script at 9 AM every day

3. Python's schedule library
   - pip install schedule
   - schedule.every().day.at("10:30").do(job)

4. APScheduler library
   - pip install APScheduler
   - scheduler.add_job(job, 'cron', hour=10, minute=30)

Example with schedule (pseudo-code):
\"\"\"
import schedule
import time

def backup_job():
    print("Running backup...")
    backup_files("./documents", "./backups")

# Schedule the job
schedule.every().day.at("10:30").do(backup_job)

# Keep scheduler running
while True:
    schedule.run_pending()
    time.sleep(60)
\"\"\"
)


# ===== SECTION 7: Email Notifications =====
print("\n=== EMAIL NOTIFICATIONS ===\n")

print("""
Sending email notifications from Python:

Use smtplib (built-in) or libraries like:
- python-dotenv (for API keys)
- email-validator (for validation)

Example:
\"\"\"
import smtplib
from email.mime.text import MIMEText

def send_notification(to_email, subject, message):
    sender_email = "bot@example.com"
    sender_password = "your_password"  # Use environment variable!
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

send_notification("user@example.com", 
                 "Backup Complete", 
                 "Your backup finished successfully")
\"\"\"
""")


# ===== SECTION 8: Practical Example - Download Monitor =====
print("\n=== PRACTICAL EXAMPLE: DOWNLOAD MONITOR ===\n")

def monitor_downloads(downloads_dir=".", max_days=30):
    \"\"\"
    Monitor downloads folder and report on old files.
    \"\"\"
    
    if not os.path.exists(downloads_dir):
        print(f"❌ Directory not found: {downloads_dir}")
        return
    
    now = datetime.datetime.now()
    max_days_delta = datetime.timedelta(days=max_days)
    
    old_files = []
    recent_files = []
    
    print(f"Scanning {downloads_dir}...")
    print(f"Looking for files older than {max_days} days\n")
    
    for filename in os.listdir(downloads_dir):
        filepath = os.path.join(downloads_dir, filename)
        
        if not os.path.isfile(filepath):
            continue
        
        # Get file modification time
        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
        age = now - mod_time
        
        if age > max_days_delta:
            old_files.append((filename, age.days))
        else:
            recent_files.append((filename, age.days))
    
    print(f"Recent files (< {max_days} days): {len(recent_files)}")
    print(f"Old files (>= {max_days} days): {len(old_files)}")
    
    if old_files:
        print(f"\nOld files that could be archived:")
        for filename, age in old_files[:5]:  # Show first 5
            print(f"  {filename} ({age} days old)")

monitor_downloads(".")


# ===== SECTION 9: Workflow Automation Example =====
print("\n\n=== WORKFLOW AUTOMATION EXAMPLE ===\n")

def content_workflow():
    \"\"\"
    Example workflow:
    1. Create content
    2. Format it
    3. Add metadata
    4. Save to structured directory
    5. Generate index
    \"\"\"
    
    print("Content Management Workflow\n")
    
    # Step 1: Create content
    print("Step 1: Creating content...")
    content = {
        "title": "Python Workshop",
        "author": "Fuad Al-Tamimi",
        "topic": "AI and Automation",
        "date": datetime.datetime.now().isoformat()
    }
    print(f"  Title: {content['title']}")
    
    # Step 2: Format
    print("\nStep 2: Formatting...")
    content['content'] = f\"\"\"
# {content['title']}

**Author:** {content['author']}
**Topic:** {content['topic']}
**Date:** {content['date']}

Content goes here...
\"\"\"
    print("  ✓ Formatted")
    
    # Step 3: Add metadata
    print("\nStep 3: Adding metadata...")
    content['tags'] = ['python', 'automation', 'ai', 'workshop']
    content['version'] = '1.0'
    print(f"  Tags: {', '.join(content['tags'])}")
    
    # Step 4: Save
    print("\nStep 4: Saving...")
    output_file = "content.json"
    with open(output_file, 'w') as f:
        json.dump(content, f, indent=2)
    print(f"  Saved to: {output_file}")
    
    # Step 5: Generate index
    print("\nStep 5: Generating index...")
    index = {
        "total_items": 1,
        "last_updated": datetime.datetime.now().isoformat(),
        "files": [output_file]
    }
    with open("index.json", 'w') as f:
        json.dump(index, f, indent=2)
    print(f"  Index created")
    
    print("\n✓ Workflow complete!")

content_workflow()


print("\n✅ Lesson 9 Complete!")
print("Next: Introduction to AI Libraries")
