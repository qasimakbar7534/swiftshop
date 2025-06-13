import zipfile
import os

def extract_war(war_file, output_dir):
    """
    Extracts the .war file into the specified output directory.
    """
    if not zipfile.is_zipfile(war_file):
        print(f"[-] Not a valid WAR/ZIP file: {war_file}")
        return
    
    with zipfile.ZipFile(war_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"[+] WAR file extracted to: {output_dir}")

def analyze_directory(directory):
    """
    Walks through the extracted WAR directory and prints information about relevant files.
    """
    print("\n[+] Starting analysis of extracted WAR content...\n")
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if file.endswith('.class'):
                print(f"[CLASS] {path}")
            elif file.endswith('.jsp'):
                print(f"[JSP]   {path}")
            elif file.endswith('.xml'):
                print(f"[XML]   {path}")
            elif file.endswith('.properties'):
                print(f"[CONFIG] {path}")
            elif file.endswith('.jar'):
                print(f"[LIB]   {path}")
    print("\n[+] Analysis completed.")

if __name__ == "__main__":
    war_file = "jenkins.war"  # Make sure this file is in the same folder
    output_dir = "jenkins_extracted"

    extract_war(war_file, output_dir)
    analyze_directory(output_dir)
