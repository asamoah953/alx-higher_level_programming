import sys

def read_file(file_path):
    try:
        # Open the file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file
            content = file.read()
            # Print the content
            print(content)
    except Exception as e:
        # Print the error object if an exception occurs
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if a file path argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
    else:
        # Get the file path from the command-line arguments
        file_path = sys.argv[1]
        # Call the read_file function
        read_file(file_path)

