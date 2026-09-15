import re
import sys

def extract_strings(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    # Find sequences of printable characters
    strings = re.findall(b'[a-zA-Z0-9\s.,;:\(\)\-]{4,}', content)
    for s in strings:
        try:
            decoded = s.decode('ascii').strip()
            if len(decoded) > 10: # Filter out short noise
                print(decoded)
        except:
            continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_text.py <file_path>")
        sys.exit(1)
    print(f"--- Extracting from {sys.argv[1]} ---")
    extract_strings(sys.argv[1])
