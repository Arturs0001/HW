FILE_NAME = "music_collection.txt"






def copy_file():
    with open("data.txt", "r", encoding="utf-8") as source:
        content = source.read()

    with open("backup.txt", "w", encoding="utf-8") as backup:
        backup.write(content)

    print("File copied successfully.")





def shift_char(c):
    if 'a' <= c <= 'z':
        return 'a' if c == 'z' else chr(ord(c) + 1)
    elif 'A' <= c <= 'Z':
        return 'A' if c == 'Z' else chr(ord(c) + 1)
    else:
        return c


def encrypt_file():
    with open("data.txt", "r", encoding="utf-8") as file:
        text = file.read()

    encrypted = "".join(shift_char(c) for c in text)

    with open("encrypted.txt", "w", encoding="utf-8") as file:
        file.write(encrypted)

    print("Encryption completed.")






def add_album():
    title = input("Album title: ")
    artist = input("Artist: ")
    year = input("Year: ")

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{title}|{artist}|{year}\n")

    print("Album added.")


def view_collection():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            print("Collection is empty.")
            return

        for line in lines:
            title, artist, year = line.strip().split("|")
            print(f"Title: {title}, Artist: {artist}, Year: {year}")

    except FileNotFoundError:
        print("No collection found.")


def search_by_artist():
    artist_search = input("Enter artist: ").lower()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            found = False

            for line in file:
                title, artist, year = line.strip().split("|")

                if artist.lower() == artist_search:
                    print(f"{title} ({year})")
                    found = True

            if not found:
                print("No albums found.")

    except FileNotFoundError:
        print("No collection found.")


def delete_album():
    title_delete = input("Enter album title to delete: ").lower()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            found = False

            for line in lines:
                title, artist, year = line.strip().split("|")

                if title.lower() != title_delete:
                    file.write(line)
                else:
                    found = True

        if found:
            print("Album deleted.")
        else:
            print("Album not found.")

    except FileNotFoundError:
        print("No collection found.")


def music_menu():
    while True:
        print("--- MUSIC MENU ---")
        print("1. Add album")
        print("2. View collection")
        print("3. Search by artist")
        print("4. Delete album")
        print("5. Back to main menu")

        choice = input("Choose: ")

        if choice == "1":
            add_album()
        elif choice == "2":
            view_collection()
        elif choice == "3":
            search_by_artist()
        elif choice == "4":
            delete_album()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def main():
    while True:
        print("=== MAIN MENU ===")
        print("1. Copy file")
        print("2. Encrypt file")
        print("3. Music collection")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            copy_file()
        elif choice == "2":
            encrypt_file()
        elif choice == "3":
            music_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()