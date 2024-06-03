"""
Program: Lab12
Author: Ifa Namee
Date: 11/26/2023
purpose: This program is download file from online and display output on python Console.
"""
import requests


def download_txt(url):
    res = requests.get(url)
    if res.status_code == requests.codes.ok:  # checks if download is ok or allow.
        return res.text
    else:
        print(f"Failed to download file. Status code: {res.status_code}")  # display if download is not allowed.
        return None


def main():
    # Replace the URL with the link to the .txt file you want to download
    txt_file_url = "https://www.gutenberg.org/files/11/11-0.txt"

    # Download the .txt file
    file_content = download_txt(txt_file_url)

    if file_content:
        print(file_content[946:10000])  # Displaying the characters that between 946 and 10,000


main()
