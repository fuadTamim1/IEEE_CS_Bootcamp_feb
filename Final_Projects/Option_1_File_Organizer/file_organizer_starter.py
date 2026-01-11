"""
WEEK 1 FINAL PROJECT - OPTION 1: Smart File Organizer
=======================================================

Base Functionality:
- Sort files by extension into organized folders

Extensions (choose at least 2):
✓ Sort by creation date
✓ Auto-rename files
✓ Create folders dynamically
✓ Ignore system files
✓ Display summary report
✓ Show execution time

Starter Code - Build upon this!
"""

import os
from pathlib import Path

def organize_files(directory):
    """
    Organize files in a directory by extension.
    
    Args:
        directory: Path to the directory to organize
    """
    
    # Get all files in the directory
    files = os.listdir(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        file_extension = os.path.splitext(file)[1]
        
        if not file_extension:
            folder_name = "No_Extension"
        else:
            folder_name = file_extension[1:].upper()  # Remove dot and uppercase
        
        # Create folder if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"📁 Created folder: {folder_name}")
        
        # Move file to the folder
        new_file_path = os.path.join(folder_path, file)
        os.rename(file_path, new_file_path)
        print(f"📄 Moved: {file} → {folder_name}/")


if __name__ == "__main__":
    # Example usage - change path as needed
    test_directory = "./test_files"
    
    # Create test files (optional)
    if not os.path.exists(test_directory):
        os.makedirs(test_directory)
        
        # Create sample files
        sample_files = ["doc1.txt", "image1.jpg", "report.pdf", "data.csv"]
        for file in sample_files:
            open(os.path.join(test_directory, file), "w").close()
        print("✅ Sample files created!\n")
    
    print("🚀 Starting file organization...\n")
    organize_files(test_directory)
    print("\n✅ File organization complete!")


# NEXT STEPS TO EXTEND THIS PROJECT:
# 1. Add date-based sorting
# 2. Add auto-renaming functionality
# 3. Add summary report
# 4. Add execution time tracking
# 5. Add error handling with try-except
# 6. Add logging to a file
# 7. Add command-line arguments
