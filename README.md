[![PyPI version](https://badge.fury.io/py/latest_blender_url.svg)](https://badge.fury.io/py/latest_blender_url) [![Build Status](https://travis-ci.org/JustasB/latest_blender_url.svg?branch=master)](https://travis-ci.org/JustasB/latest_blender_url) [![codecov](https://codecov.io/gh/JustasB/latest_blender_url/branch/master/graph/badge.svg)](https://codecov.io/gh/JustasB/latest_blender_url)

# Get the latest Blender download URL and use it in a Travis CI scipt

Place the following lines in your travis.yml to download the latest Blender version (Linux 64-bit):

```
- pip install latest_blender_url
- url="$(python -c 'import latest_blender_url as lbu; lbu.get_latest()')"
- curl -L -o blender.tar.bz2 $url
```

# Customizing the distribution to get
[`BlenderURLGetter`](https://github.com/JustasB/latest_blender_url/blob/master/latest_blender_url/__init__.py#L10) class does all of the work. You can change the Blender download page and the archive to download by changing the class properties.

```
from latest_blender_url import BlenderURLGetter
getter = BlenderURLGetter()

# Set the download page
getter.download_page_url = "https://www.blender.org/download/" 

# Set the archive pattern (see Blender download page for URL formats)
#getter.archive_pattern = '.+href="(.+?linux.+?x86_64.+?bz2)' # Linux 64bit
#getter.archive_pattern = '.+href="(.+?macOS.+?dmg)'          # MacOS
#getter.archive_pattern = '.+href="(.+?windows64.zip)'        # Windows 64bit

# This will scrape the download page and get the matching url
url = getter.get_latest()
```

# Feel free to fork or submit a pull request with new features

