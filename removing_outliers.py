import os

def delete_files_with_numbers(path, path2, numbers):
    # Get a list of all files in the directory
    files = os.listdir(path)
    
    # Iterate over the files and delete the ones ending with the specified numbers
    for file in files:
        # Extract the last characters of the file name (assuming they are numbers)
        file_number = file.split('_')[-1].split('.')[0]
        
        # Check if the file number matches any of the specified numbers
        if file_number in numbers:
            # Construct the full file path
            file_path = os.path.join(path, file)
            file_path2 = os.path.join(path2, file)
            # Delete the file
            os.remove(file_path)
            os.remove(file_path2)
            print(f"Deleted file: {file_path}")

# Specify the directory path
directory_path = "/home/aranyaa/Project/dataset_not_normalized/val/images/"
directory_path2 = "/home/aranyaa/Project/dataset_not_normalized/val/ground_truths/"

# Specify the numbers to filter
numbers_to_filter = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41'}

# Call the function to delete the files
delete_files_with_numbers(directory_path, directory_path2, numbers_to_filter)
