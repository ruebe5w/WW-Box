try:
    from pip._internal import main as pip
except:
    try:
        from pip import main as pip
    except:
        print('ERROR importing pip.')

pip(['install', '-r' 'requirements.txt'])
