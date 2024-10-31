import webbrowser as wb
import time
import pyautogui as pu
v = ['ABACK', 'ABASE', 'ABATE', 'ABBEY', 'ABBOT', 'ABHOR', 'ABIDE', 'ABLED', 'ABODE', 'ABORT', 'ABOUT', 'ABOVE', 'ABUSE', 'ABYSS', 'ACORN', 'ACRID', 'ACTOR', 'ACUTE', 'ADAGE', 'ADAPT', 'ADEPT', 'ADMIN', 'ADMIT', 'ADOBE', 'ADOPT', 'ADORE', 'ADORN', 'ADULT', 'AFFIX', 'AFIRE']
for elem in v:
    q = elem.replace(" ", "+")
    wb.open(f"https://www.bing.com/search?q={q}")
    time.sleep(2)
    pu.hotkey("ctrl","w")


