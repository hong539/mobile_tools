import zipfile
import shutil
import os

def extract_apk_from_xapk(xapk_file, output_folder):
    # Open the XAPK file
    with zipfile.ZipFile(xapk_file, 'r') as xapk_zip:
        # Extract all contents to the output folder
        xapk_zip.extractall(output_folder)

        # Look for the APK file within the extracted contents
        apk_file = None
        for filename in xapk_zip.namelist():
            if filename.endswith('.apk'):
                apk_file = filename
                break
        
        if apk_file:
            # Rename the APK file
            extracted_apk_path = os.path.join(output_folder, apk_file)
            renamed_apk_path = os.path.join(output_folder, 'extracted.apk')
            os.rename(extracted_apk_path, renamed_apk_path)
            return renamed_apk_path
        else:
            return None

# Provide the path to your XAPK file
xapk_path = 'path/to/your/file.xapk'

# Provide the output folder where you want to extract the APK
output_folder = 'output/folder/path'

# Extract the APK from the XAPK
result = extract_apk_from_xapk(xapk_path, output_folder)

if result:
    print(f"APK extracted successfully to: {result}")
else:
    print("No APK file found in the XAPK.")