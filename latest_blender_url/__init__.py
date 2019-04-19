import os, re

# Python 2
try:  
    from urllib2 import urlopen
# Python 3
except ImportError:  
    from urllib.request import urlopen

class BlenderURLGetter:
    '''
    Defines the methods and properties of the URL getter
    '''

    def __init__(self):
        # The URL of the download page (that's where the links are scraped from)
        self.download_page_url = "https://www.blender.org/download/"

        # The pattern to use (default is Linux 64-bit. Look at the download page for patterns of other platforms)
        self.archive_pattern = '.+href="(.+?linux.+?x86_64.+?bz2)'

        # Whether to print the download URL on screen (useful when this script is used within the context of a shell script)
        self.print_url = True

    def get_html(self, url):
        '''Retrieves the HTML string of an URL'''

        return str(urlopen(url).read())

    def find_archive(self, html):
        '''Uses regular expressions to find the archive url'''

        return re.search(self.archive_pattern,html).group(1)

    def get_latest(self):
        '''Follows the download page links to get the final download URL'''

        # First, get the download page, which contains the pre-mirror url
        html = self.get_html(self.download_page_url)

        # Get the pre-mirror url
        latest_pre_mirror_url = self.find_archive(html)

        # Follow the pre-mirror url 
        html = self.get_html(latest_pre_mirror_url)

        # Get the actual download url
        latest_url = self.find_archive(html)
    
        if self.print_url:
            print(latest_url)

        return latest_url

def get_latest():
    '''A convenience method to get the default download url'''

    return BlenderURLGetter().get_latest()

