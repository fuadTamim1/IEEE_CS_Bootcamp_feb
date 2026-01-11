"""
FINAL PROJECT: Option 1 - Smart File Organizer
==============================================

Project Description:
Automatically organize files in a directory by file extension (or other criteria).

Base Functionality:
- Read all files in a target directory
- Group files by extension (.txt, .jpg, .pdf, etc.)
- Create folders for each extension (if they don't exist)
- Move files to their corresponding folders
- Display a summary report

Skills Used:
- File I/O operations
- os and pathlib modules
- Loops and conditionals
- Functions for organization
- Error handling

Submission Requirements:
✓ Working Python file
✓ Output showing what was organized
✓ 100-200 word explanation of extensions implemented

==============================================

EXTENSIONS (Choose at least 2):

[ ] Time-Based Sorting
    Sort files by creation/modification date instead of extension
    Example: /2026-02-15/, /2026-02-16/

[ ] Auto-Renaming
    Rename files to a standard format
    Example: document.pdf -> doc_001.pdf, doc_002.pdf

[ ] Dynamic Folders
    Create folders dynamically if they don't exist
    (Already in base - but make it more robust)

[ ] System Safety
    Ignore system files (.DS_Store, Thumbs.db, etc.)
    Ignore hidden files

[ ] Reporting
    Generate a detailed report showing:
    - Total files processed
    - Files moved per category
    - Total storage saved/organized

[ ] Performance
    Measure and display execution time
    Show speed statistics (files/second)

[ ] Preview Mode
    Show what will be done without actually moving files
    \"Dry run\" option

[ ] Smart Categories
    Organize by document type (Images, Documents, Videos, Audio, Code, Other)
    Instead of just extension

==============================================
"""

import os
import shutil
from datetime import datetime
import time

# ============================================
# BASE FUNCTIONALITY - IMPLEMENT THESE FIRST
# ============================================

def get_file_extension(filename):
    """
    TODO: Extract file extension from filename.
    
    Examples:
    - 'document.pdf' -> '.pdf'
    - 'image.jpeg' -> '.jpeg'
    - 'no_extension' -> ''
    
    Args:
        filename (str): Name of the file
    
    Returns:
        str: File extension (including the dot)
    """
    pass


def create_category_folder(base_dir, category):
    """
    TODO: Create a folder for the category if it doesn't exist.
    
    Args:
        base_dir (str): Base directory path
        category (str): Category/extension name
    
    Returns:
        str: Path to the category folder
    """
    pass


def organize_files_by_extension(directory):
    """
    TODO: Main function to organize files by extension.
    
    Steps:
    1. List all files in directory
    2. For each file:
       a. Get its extension
       b. Skip if it's a directory or has no extension
       c. Create folder for this extension
       d. Move file to that folder
    3. Return statistics (files moved, folders created)
    
    Args:
        directory (str): Directory to organize
    
    Returns:
        dict: Statistics about the operation
            {
                'files_moved': int,
                'folders_created': int,
                'errors': list
            }
    """
    pass


def display_report(stats):
    """
    TODO: Display a summary report of the organization.
    
    Should show:
    - Files moved
    - Folders created
    - Any errors encountered
    
    Args:
        stats (dict): Statistics from organize_files_by_extension()
    """
    pass


# ============================================
# EXTENSION 1: SYSTEM SAFETY
# ============================================

def is_system_file(filename):
    """
    TODO (EXTENSION): Check if file is a system file that should be ignored.
    
    System files to ignore:
    - .DS_Store (Mac)
    - Thumbs.db (Windows)
    - .git* (Git)
    - Files starting with . (hidden files)
    
    Args:
        filename (str): Name of the file
    
    Returns:
        bool: True if file should be ignored
    """
    pass


# ============================================
# EXTENSION 2: TIME-BASED SORTING
# ============================================

def get_file_modification_date(filepath):
    """
    TODO (EXTENSION): Get the modification date of a file.
    
    Args:
        filepath (str): Full path to the file
    
    Returns:
        str: Date in format YYYY-MM-DD
    """
    pass


def organize_files_by_date(directory):
    """
    TODO (EXTENSION): Organize files by modification date instead of extension.
    
    Creates folders: /2026-02-15/, /2026-02-16/, etc.
    
    Args:
        directory (str): Directory to organize
    
    Returns:
        dict: Statistics about the operation
    """
    pass


# ============================================
# EXTENSION 3: AUTO-RENAMING
# ============================================

def rename_files_sequentially(directory):
    """
    TODO (EXTENSION): Rename files sequentially within their extension folders.
    
    Example:
    - image_01.jpg
    - image_02.jpg
    - document_01.pdf
    
    Args:
        directory (str): Directory to process
    
    Returns:
        dict: Statistics including files renamed
    """
    pass


# ============================================
# EXTENSION 4: PERFORMANCE TRACKING
# ============================================

def organize_with_performance(directory):
    """
    TODO (EXTENSION): Organize files and track performance metrics.
    
    Metrics to track:
    - Total time taken
    - Files processed per second
    - Average time per file
    
    Args:
        directory (str): Directory to organize
    
    Returns:
        dict: Statistics including performance metrics
    """
    pass


# ============================================
# EXTENSION 5: PREVIEW/DRY RUN MODE
# ============================================

def preview_organization(directory):
    """
    TODO (EXTENSION): Show what will be organized without actually doing it.
    
    Useful for:
    - Checking before committing changes
    - Verifying the logic is correct
    - Safe testing
    
    Args:
        directory (str): Directory to preview
    
    Returns:
        dict: What would be done (without doing it)
    """
    pass


# ============================================
# EXTENSION 6: SMART CATEGORIES
# ============================================

def get_smart_category(filename):
    """
    TODO (EXTENSION): Categorize files by type instead of just extension.
    
    Categories:
    - Images: .jpg, .png, .gif, .jpeg, .svg, .bmp
    - Documents: .pdf, .docx, .txt, .xlsx, .ppt
    - Videos: .mp4, .avi, .mov, .mkv
    - Audio: .mp3, .wav, .flac, .m4a
    - Code: .py, .js, .java, .cpp, .html
    - Compressed: .zip, .rar, .7z, .tar
    - Other: everything else
    
    Args:
        filename (str): Name of the file
    
    Returns:
        str: Category name
    """
    pass


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """
    Main function to run the file organizer.
    """
    
    print("=" * 50)
    print("SMART FILE ORGANIZER")
    print("=" * 50)
    
    # TODO: Ask user for directory to organize
    # directory = input("Enter directory path to organize: ")
    
    # For demo/testing, we'll use current directory
    directory = "."
    
    # TODO: Check if directory exists
    if not os.path.exists(directory):
        print(f"❌ Directory '{directory}' not found!")
        return
    
    print(f"\nTarget directory: {directory}")
    
    # TODO: Ask if user wants preview mode
    # preview_mode = input("Preview only? (y/n): ").lower() == 'y'
    
    # TODO: Call the appropriate function based on user choice
    # Options:
    # 1. organize_files_by_extension()
    # 2. organize_files_by_date()
    # 3. Other extensions
    
    print("\nStarting organization...")
    
    # TODO: This is where you call your function
    # stats = organize_files_by_extension(directory)
    
    print("\n(TODO: Implement and run the organizer)")
    
    # TODO: Display report
    # display_report(stats)
    
    print("\n" + "=" * 50)
    print("Done!")
    print("=" * 50)


# ============================================
# TESTING HELPERS
# ============================================

def create_test_files():
    """
    Create test files for development and testing.
    This helps you test without needing real files.
    """
    
    test_dir = "test_files"
    
    # Create test directory
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # Create sample files
    test_files = [
        "document1.pdf",
        "document2.pdf",
        "image1.jpg",
        "image2.png",
        "song1.mp3",
        "song2.mp3",
        "code.py",
        "archive.zip",
        "README.txt"
    ]
    
    for filename in test_files:
        filepath = os.path.join(test_dir, filename)
        with open(filepath, 'w') as f:
            f.write(f"This is {filename}")
    
    print(f"✓ Created {len(test_files)} test files in '{test_dir}/'")
    return test_dir


# ============================================
# GETTING STARTED
# ============================================

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════╗
║      SMART FILE ORGANIZER - STARTER CODE      ║
║                                                ║
║ Follow the TODO comments to implement the      ║
║ required functions. Then add your chosen       ║
║ extensions from the list above.                ║
║                                                ║
║ Steps:                                         ║
║ 1. Implement base functions (marked TODO)      ║
║ 2. Test with test_files (run create_test_files)║
║ 3. Add at least 2 extensions                   ║
║ 4. Create a README explaining your work        ║
╚════════════════════════════════════════════════╝
    """)
    
    # Uncomment to create test files
    # create_test_files()
    
    # TODO: Uncomment to run
    # main()
    
    print("\n📝 Next Steps:")
    print("1. Read through all the TODO comments")
    print("2. Implement the base functions")
    print("3. Test with test files")
    print("4. Add your extensions")
    print("5. Test thoroughly")
    print("\n💡 Tips:")
    print("- Start with just getting files and extensions")
    print("- Test moving one file first")
    print("- Add error handling for edge cases")
    print("- Use try-except blocks")
    print("- Print debug info to understand what's happening")
