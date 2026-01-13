# also install types-* [replace "*"  with package name you want to install]
# eg: types-requests

import requests

resp = requests.get("https://www.rohilprajapati.com.np/#/home", timeout=5)
status = resp.status_code
status = 200

"""
    Notes:
        Input should be Generic
        Output should be Specific
"""
