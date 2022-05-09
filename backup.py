import os
import shutil
import time


def main() :
    deleted_folders_count = 0
    deleted_files_count=0

    path="/PATH_TO_DELETE"

    days = 30


    second= time.time() - (days*24*60*60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):

                remove_folder(root_folder)
                deleted_folders_count += 1

                break

            else:

                for folder in folders:

                    folder_path = os.path.join(root_folder,folder)

                    if seconds >= get_file_or_folder_age(folder_path):

                        remove_folder(root_folder)
                        deleted_folders_count += 1



                for file in files:

                    file_path = os.path.join(root_folder,folder)

                    if seconds >= get_file_or_folder_age(file_path):
                        remove_files(root_folder)
                        deleted_files_count += 1


        else:


                if seconds >= get_file_or_folder_age(file_path):
                        remove_files(root_folder)
                        deleted_files_count += 1


        else:

            print(f'"{path}" is not found')
            deleted_files_count += 1

        print(f"Total folders deleted: {deleted_folders_count}")
        print(f"Total files deleted: {deleted_files_count}")




def remove_folder(path):

    if not shutil.rmtree(path):

        print(f"{path} is removed succesfully")

    else:

        print("unable to delete the"+path)


def  get_file_or_folder_age(path):

    time.ctime=os.stat(path).st_ctime

    return ctime


if _name_ == '_main_':
    main()





                 



                
