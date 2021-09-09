from staticjinja import Site
import os

if __name__ == "__main__":
    prod = os.getenv("prod")
    site = Site.make_site(outpath="dist")
    # enable automatic reloading
    if prod:
        site.render(use_reloader=False)
    else:
        site.render(use_reloader=True)
