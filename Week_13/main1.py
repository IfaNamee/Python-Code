from bs4 import BeautifulSoup as soup       # As soup so you don't have to keep typing BeautifulSoup
import requests


def main():
    # Set source URL where poem is located.
    str_url = "http://allpoetry.com/Do-Not-Go-Gentle-Into-That-Good-Night"
    # Set filename
    str_filename = "DoNotGoGentle.txt"                                  # set filename to save contents to

    try:
        # Display status messages
        print("\nDownloading poem from URL: ", str_url)
        print("Saving to                : ", str_filename)
        # Get specified webpage in soup html parsed format
        imported_webpage = GetWebpage(str_url)
        # Ask user if they'd like to see the source html
        while True:
            str_input = input("\nWould you like to see the unprocessed HTML? (y/n) : ")  # Get user input
            if str_input == "y" or str_input == "yes":    # If yes display source html /// for some reason if I use .lower, it does not work.
                print("\n### Displaying raw html ###")
                print("\n", imported_webpage)
                print("\n###   End of raw html   ###")
                break
            elif str_input == "n" or str_input == "no":   # If no, then display nothing and continue on..
                break
            else:
                print("Invalid input. Please try again.") # If no matching option detected, display error message and ask again.
        # Extract Poem
        str_poem = ExtractPoem(imported_webpage)
        # Export
        ExportFile(str_poem, str_filename)
        # Re-import file
        print("\nSave complete, re-importing file.")
        str_content = ImportFile(str_filename)
        # Display contents of file on screen
        print("\nFile read into memory, displaying contents:\n")
        Display(str_content)
    except Exception as err:  # generic exception handling, if something goes wrong display the error #
        print("\nCongratulations. You broke the time continuum. Internal error\n")
        print(err)


def GetWebpage(str_url):
    # Get web page
    page_html = requests.get(str_url)
    # Parse with BeautifulSoup's html parser
    page_soup = soup(page_html.text, "html.parser")
    # Return result in soup format
    return page_soup


def ExtractPoem(page_soup):
    # Locate div tag, class - 'poem_body'
    found = page_soup.find("div", {"class": "poem_body"})
    # This strips all the leading white space from each paragraph
    poem = "\n".join(line.strip() for line in found.p.text.split("\n"))
    # Return parsed poem as string
    return poem


def ExportFile(str_content, str_filename):
    # Open specified file in write mode  (not write - binary like the last one)
    export_file = open(str_filename, 'w')
    # Write contents out to file
    export_file.write(str_content)
    # Close file
    export_file.close()
    # In a more complex program I'd have it return a result such as success/fail


def ImportFile(str_filename):
    # Open specified file in read mode
    import_file = open(str_filename, 'r')
    # Read contents of file in variable
    str_content = import_file.read()                   # read file contents into variable
    # Close file
    # import_file.close   - not necessary to disabled
    return str_content


def Display(content):
    # Pretty simple, display contents of file. It's already formatted correctly
    print(content)


# Engage
main()