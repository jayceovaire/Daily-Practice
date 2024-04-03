import os
import requests
from bs4 import BeautifulSoup
import string

def download_image(url, folder):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:  # success
            # Extract the base name (part before '?') and replace problematic characters
            filename = url.split("/")[-1].split("?")[0]
            valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
            filename = ''.join(c for c in filename if c in valid_chars)

            filepath = os.path.join(folder, filename)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded {url} to {filepath}")
        else:
            print(f"Failed to download {url}. Status Code: {response.status_code}. Content Type: {response.headers['content-type']}")
    except Exception as e:
        print(f"An error occurred while downloading {url}. Error: {e}")


def extract_images_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        # Extracting the URLs of the images
        img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

        # Resolving relative URLs
        img_urls = [requests.compat.urljoin(url, img_url) for img_url in img_urls]
        return img_urls
    except Exception as e:
        print(f"An error occurred while processing {url}. Error: {e}")
        return []


def main():
    urls = [
        "",
        # ... add more URLs as needed
    ]
    folder = "downloaded_images"
    os.makedirs(folder, exist_ok=True)

    for url in urls:
        image_urls = extract_images_from_url(url)
        for img_url in image_urls:
            download_image(img_url, folder)

if __name__ == "__main__":
    main()

