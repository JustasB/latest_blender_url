[![PyPI version](https://badge.fury.io/py/latest_blender_url.svg)](https://badge.fury.io/py/latest_blender_url) [![Build Status](https://travis-ci.org/JustasB/latest_blender_url.svg?branch=master)](https://travis-ci.org/JustasB/latest_blender_url) [![codecov](https://codecov.io/gh/JustasB/latest_blender_url/branch/master/graph/badge.svg)](https://codecov.io/gh/JustasB/latest_blender_url)

# Get the latest Blender download URL and use it in a Travis CI scipt to download the archive

In travis.yml:

```
- pip install latest_blender_url
- url="$(python -c 'import latest_blender_url as lbu; lbu.get_latest()')"
- curl -L -o blender.tar.bz2 $url
```


