import os

def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"File Name {filename}: Created successfully!")
    except FileExistsError:
        print(f"file Name {filename} already exists!")

    except Exception as E:
        print("an error occurred!") 

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found!")
    else:
        print("files in directory!")
        for file in files:
            print(file) 
    
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("An error occurred!")

def read_file(filename):
    try:
        with open('sample.txt',"r") as f:
            Content = f.read() 
            print(f"content of '{filename}':\n{Content}")

    except FileNotFoundError:
        print(f"{filename}doesn't exist!")

    except Exception as e:
        print('An error occurred!')

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            Content = input('enter data to add=')
            f.write(Content + "\n")
            print('Content added to {filename} Successfully!')
    except FileNotFoundError:
        print(f"{filename} doesn't exixt!")

    except Exception as e:
        print('An error occurred!')

def main():
        while True:
            print("FILE MANAGEMANT APP")
            print('1: Create file')
            print('2: view all file')
            print('3: delete file')
            print('4: read file')
            print('5: edit file')
            print('6: Exit')

            choice = input("Enter your choice(1-6) = ")

            if choice == "1":
                filename = input("Enter the file-name to create =")
                create_file(filename)
            elif choice == "2":
                view_all_files()
            
            elif choice == '3':
                filename = input("Enter the name of file you want to delete =")
                delete_file(filename)

            elif choice == '4':
                filename = input("Enter the file name to Read =")
                read_file(filename)

            elif choice =='5':
                filename = input("Enter the file you want to edit =")
                edit_file(filename)

            elif choice =='6':
                filename = input("Closing the App....")
                break
            else:
                print('In-valid syntax')

if __name__ == "__main__":
 main()