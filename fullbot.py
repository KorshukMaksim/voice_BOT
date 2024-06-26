# Read the content of file1.py
with open("file1.py", "r") as file1:
    content1 = file1.read()

# Read the content of file2.py
with open("file2.py", "r") as file2:
    content2 = file2.read()

# Combine the contents with a newline separator
combined_content = content1 + "\n" + content2

# Write the combined content to a new file (file3.py)
with open("file3.py", "w") as file3:
    file3.write(combined_content)

# Execute the combined file (file3.py)
import subprocess
subprocess.run(["python", "file3.py"])
