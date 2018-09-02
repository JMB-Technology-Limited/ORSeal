import os, sys

if __name__ == '__main__':
    # Setup environ
    sys.path.append(os.getcwd())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orseal.settings")

    # Setup django
    import django
    django.setup()

    # now you can import your ORM models
    import orseal_engine.import_hdsa

    importer = orseal_engine.import_hdsa.ImportHSDA()
    importer.go()
