import sys,pyperclip
if len(sys.argv)>1:
    originialPath=sys.argv[-1]
else:
    originialPath=pyperclip.paste()
    if "\\" not in originialPath:
        originialPath=input("Enter a path: ")
ans=originialPath.replace("\\","\\\\")
print(ans)
pyperclip.copy(ans)