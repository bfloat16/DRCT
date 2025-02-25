import os

def scan_directory(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.abspath(os.path.join(root, filename))
                file.write(file_path + '\n')

if __name__ == "__main__":
    folder_path = input("Enter the folder path to scan: ")
    output_txt = input("Enter the output text file path: ")
    
    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
    else:
        scan_directory(folder_path, output_txt)
        print(f"File paths have been written to {output_txt}")