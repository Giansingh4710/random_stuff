import webbrowser, sys, pyperclip
if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()

if "http" in address:       
    webbrowser.open(address)
else:
    a="https://www.google.com/search?q="
    for i in address.split(" "):
        a+=i
        a+="+"
    webbrowser.open(a)

