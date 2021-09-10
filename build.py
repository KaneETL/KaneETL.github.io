from staticjinja import Site
import os
import shutil

if __name__ == "__main__":
    prod = os.getenv("prod")
    site = Site.make_site(outpath="dist")
    # enable automatic reloading
    src = "static"
    dst = "dist/" + src
    dir_check = os.path.exists(dst)

    if dir_check == True:
        shutil.rmtree(dst)

    shutil.copytree(src, dst)
    if prod:
        site.render(use_reloader=False)
    else:
        site.render(use_reloader=True)
