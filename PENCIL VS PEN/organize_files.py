import os
import shutil
import random

# --- CONFIGURATION ---
# Where your current images are (The folder containing 'pen' and 'pencil' subfolders)
# Example: r"C:\Users\evang\Downloads\Pen_vs_Pencil_Project\dataset"
ORIGINAL_DATASET_DIR = r"C:\Users\evang\Downloads\Pen_vs_Pencil_Project\dataset"

# Where you want the new organized folders to be created
BASE_DIR = r"C:\Users\evang\Downloads\Pen_vs_Pencil_Project\split_dataset"

# How much data goes to training? (0.8 = 80% Train, 20% Test)
SPLIT_SIZE = 0.8

# ---------------------

def split_data(source, training, testing, split_size):
    files = []
    # Get all files, ignore subdirectories
    for filename in os.listdir(source):
        file = os.path.join(source, filename)
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(f"{filename} is zero length, so ignoring.")

    training_length = int(len(files) * split_size)
    testing_length = int(len(files) - training_length)
    
    # Shuffle files to make it random
    random.shuffle(files)
    
    training_set = files[0:training_length]
    testing_set = files[-testing_length:]

    # Copy files
    for filename in training_set:
        this_file = os.path.join(source, filename)
        destination = os.path.join(training, filename)
        shutil.copyfile(this_file, destination)

    for filename in testing_set:
        this_file = os.path.join(source, filename)
        destination = os.path.join(testing, filename)
        shutil.copyfile(this_file, destination)

# Create the folders
train_dir = os.path.join(BASE_DIR, 'train')
test_dir = os.path.join(BASE_DIR, 'test')

# Make directories if they don't exist
os.makedirs(os.path.join(train_dir, 'pen'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'pencil'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'pen'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'pencil'), exist_ok=True)

# Run the split
print("Splitting PEN images...")
split_data(os.path.join(ORIGINAL_DATASET_DIR, 'pen'), 
           os.path.join(train_dir, 'pen'), 
           os.path.join(test_dir, 'pen'), 
           SPLIT_SIZE)

print("Splitting PENCIL images...")
split_data(os.path.join(ORIGINAL_DATASET_DIR, 'pencil'), 
           os.path.join(train_dir, 'pencil'), 
           os.path.join(test_dir, 'pencil'), 
           SPLIT_SIZE)

print(f"Done! Your new dataset is in: {BASE_DIR}")