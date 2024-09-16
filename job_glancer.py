"""
Scan through the text of job applications quickly, and pick up signals that
might either appeal to me, or show that it's not worth my time.
"""

# Many websites may not be amenable to scraping, but at least I can use the
# text once it's in front of me!

from pandas.io import clipboard
from pprint import pprint

GOOD_LOCATIONS = ["edinburgh", "glasgow", "remote", "from home", "from-home",
                  "lothian", "falkirk"]

GREEN_FLAGS = ["responsibl", "climate", "gis",
               "math", #(sic)
               "entry", "graduate"]
RED_FLAGS = ["senior",
             "financ"]

def location_good(text):
    """Get whether an acceptable location is mentioned."""
    return any([location in text for location in GOOD_LOCATIONS])

def glance(text=None):
    """Look for green and red flags in the job advert"""
    if text is None:
        text = clipboard.paste().lower()

    # check location
    summary = {
        "location good": location_good(text),
        "red flags": [flag for flag in RED_FLAGS if flag in text],
        "green flags": [flag for flag in GREEN_FLAGS if flag in text]
        }
        
    return summary
