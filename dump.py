# Import required libraries
import os
import ftputil
import shutil

# Declare URLs
gameurl = "/storage_mlc/usr/save/system/boss/"

# Declare FTP variables
address = input("Enter the Wii U's IP address. Do not include the port.\n -> ")

def file_check():

    if "output" not in os.listdir():
        os.mkdir("output")
    
    if ".gitkeep" in os.listdir('./output'):
        os.remove("./output/.gitkeep")

def transfer_data():

    with ftputil.FTPHost(address, "anonymous", "anonymous") as ftp_host:
        print("\nConnected to Wii U!")

        ftp_host.chdir(gameurl)
        names = ftp_host.listdir(ftp_host.curdir)

        names.remove("newsStorage.info")
        names.remove("afd.db")

        print(f"\nThere are {len(names)} BOSS save folders. They may take a while to download, so please be patient.\n")

        for user in names:
            if "task.db" in ftp_host.listdir(f"{gameurl}/{user}/"):   
                size = ftp_host.path.getsize(f"{gameurl}/{user}/task.db")
                print(f" -> BOSS database detected, downloading '{user}' ({size} bytes)...")
                ftp_host.download(f"{gameurl}/{user}/task.db", f"./output/task_{user}.db")

        print("\nAll save files have been downloaded.")

    print("\nDisconnected from Wii U!")

    shutil.make_archive("./output/output", "zip", "./output/")
    
    print("\nAll BOSS database files are accessible in the 'output' folder.")
    print("They have also been archived into a single ZIP file.")

if __name__ == '__main__':
    file_check()
    transfer_data()
