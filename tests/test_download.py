def test_get_url():
    from latest_blender_url import get_latest
    latest_url = get_latest()
    print('Latest url is', latest_url)
    assert "blender-" in latest_url

def test_download():
    from latest_blender_url import get_latest
    latest_url = get_latest()

    print('Downloading Blender', latest_url)
    import os
    os.system('curl -L -o blender.tar.bz2 ' + latest_url)
    os.system('tar xvjf blender.tar.bz2')

    # rename dir to just blender
    d = '.'
    new_dir = os.path.join(d,'blender')
    print('Renaming dir to', new_dir)

    blender_dir = next(os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o)) and o.startswith('blender-'))
    os.renames(blender_dir,new_dir)

    os.system('./blender/blender --background')

    assert os.path.exists('blender/blender')

    os.system('rm -R blender')
    os.system('rm blender.tar.bz2')
