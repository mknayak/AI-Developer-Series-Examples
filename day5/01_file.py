import os
from pathlib import Path

current_directory_using_os = os.path.dirname(os.path.abspath(__file__))
current_directory_using_pathlib = Path(__file__).parent

print(f"Current directory using os: {current_directory_using_os}")
print(f"Current directory using pathlib: {current_directory_using_pathlib}")

#old way
file_path= os.path.join(current_directory_using_os,"examples","csv","country.csv")
new_file_path= os.path.join(current_directory_using_os,"examples","csv","new_file2.csv")
print(file_path)
if os.path.exists(file_path):
    with open(file_path) as file:
        content= file.read()
        print(content)
    with open(new_file_path,"w") as file2:
        file2.write(content)
        
    
#new way
csv_path=Path(current_directory_using_pathlib)/"examples"/"csv"/"country.csv"
csv_write_path=csv_path.parent/"newfile.csv"
if csv_path.exists():
    content_csv= csv_path.read_text()
    print(content_csv)
    csv_write_path.write_text(content_csv)

sub_files= csv_path.parent.parent.rglob("*.csv")
for f in sub_files:
    print(f)