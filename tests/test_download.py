def test_get_default_url():
    from latest_blender_url import get_latest
    latest_url = get_latest()
    print('Latest url is', latest_url)
    assert "blender-" in latest_url

def test_win_url():
    from latest_blender_url import BlenderURLGetter
    getter = BlenderURLGetter()
    getter.archive_pattern = 'windows64.zip'        # Windows 64bit
    url = getter.get_latest()
    assert url.endswith(getter.archive_pattern)

def test_mac_url():
    from latest_blender_url import BlenderURLGetter
    getter = BlenderURLGetter()
    getter.archive_pattern = 'macOS.dmg'          # MacOS
    url = getter.get_latest()
    assert url.endswith(getter.archive_pattern)

def test_linux_url():
    from latest_blender_url import BlenderURLGetter
    getter = BlenderURLGetter()
    getter.archive_pattern = 'linux64.tar.xz' # Linux 64bit
    url = getter.get_latest()
    assert url.endswith(getter.archive_pattern)

def test_download():
    from latest_blender_url import get_latest
    latest_url = get_latest()

    print('Downloading Blender', latest_url)
    import os
    os.system('curl -L -o blender.tar.xz ' + latest_url)
    os.system('tar xvJf blender.tar.xz')

    # rename dir to just blender
    d = '.'
    new_dir = os.path.join(d,'blender')
    print('Renaming dir to', new_dir)

    blender_dir = next(os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o)) and o.startswith('blender-'))
    os.renames(blender_dir,new_dir)

    os.system('./blender/blender --background')

    assert os.path.exists('blender/blender')

    os.system('rm -R blender')
    os.system('rm blender.tar.xz')


if __name__ == "__main__":
    test_get_default_url()