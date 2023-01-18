#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
     """fetches https://alx-ntranet.hbtn.io/status"""
   
     
     import urllib.request as request
   
     
     with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        html = r.read()
      html_str = html.decode("utf-8")
        
     
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html_str))
