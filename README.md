# Get the latest Blender download URL and use it in a Travis CI scipt to download the archive

In travis.yml:

```
- pip install latest_blender_url
- url="$(python -c 'import latest_blender_url as lbu; lbu.get_latest()')"
- curl -L -o blender.tar.bz2 $url
```

