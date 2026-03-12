# Massachusetts FOIA Campaign

FOIA requests targeting ALPR surveillance and fusion center data sharing 
across all 351 Massachusetts municipalities.

## Files

- `contacts.pdf` — official Mass.gov contact list for all 351 cities and towns
- `parse_contacts.py` — parses contacts.pdf and merges with town websites into targets.json
- `targets.json` — master target list with name, website, and email for each town
- `sender.py` — sends FOIA request emails to targets with dry run mode

## Workflow
```
contacts.pdf → parse_contacts.py → targets.json → sender.py
```

## Usage
```bash
# Parse contacts and build target list
python3 parse_contacts.py

# Dry run - preview without sending
python3 sender.py

# To send for real, change dry_run=False in sender.py
```

## Known Issues

8 towns are missing emails from the Mass.gov PDF and need to be filled 
in manually in targets.json:

- Chesterfield
- Easthampton
- Lynnfield
- Manchester-by-the-Sea
- Mount Washington
- Newburyport
- Wareham
- Westhampton

## Status

- Targets built: 343/351
- Requests sent: 0
- Responses received: 0
![eyecon](https://github.com/user-attachments/assets/f537ccce-10f8-43d6-b868-664c4dc658c5)
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>Redirect Notice</title><style>body,div,a{font-family:Arial,sans-serif}body{background-color:var(--xhUGwc);margin-top:3px}div{color:var(--YLNNHc)}a:link{color:#681da8}a:visited{color:#681da8}a:active{color:#ea4335}div.mymGo{border-top:1px solid var(--gS5jXb);border-bottom:1px solid var(--gS5jXb);background:var(--aYn2S);margin-top:1em;width:100%}div.aXgaGb{padding:0.5em 0;margin-left:10px}div.fTk7vd{margin-left:35px;margin-top:35px}</style></head><body><div class="mymGo"><div class="aXgaGb"><font style="font-size:larger"><b>Redirect Notice</b></font></div></div><div class="fTk7vd">&nbsp;The previous page is sending you to <a href="https://www.freeiconspng.com/images/eye-icon">https://www.freeiconspng.com/images/eye-icon</a>.<br><br>&nbsp;If you do not want to visit that page, you can <a href="#" id="tsuid_RzOyaYyrG6mt5NoPuZiycA_1">return to the previous page</a>.<script nonce="HeGwv864d1hAD_t7Xbriyw">(function(){var id='tsuid_RzOyaYyrG6mt5NoPuZiycA_1';(function(){document.getElementById(id).onclick=function(){window.history.back();return!1};}).call(this);})();(function(){var id='tsuid_RzOyaYyrG6mt5NoPuZiycA_1';var ct='originlink';var oi='unauthorizedredirect';(function(){document.getElementById(id).onmousedown=function(){var b=document&&document.referrer,a="encodeURIComponent"in window?encodeURIComponent:escape,c="";b&&(c=a(b));(new Image).src="/url?sa=T&url="+c+"&oi="+a(oi)+"&ct="+a(ct);return!1};}).call(this);})();</script><br><br><br></div></body></html>
