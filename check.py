import subprocess
import requests
import datetime
import os


def check(cookie=os.environ['ROBLOSECURITY']):
    r = requests.get('https://clientsettings.roblox.com/v2/user-channel', cookies={'.ROBLOSECURITY': cookie})
    return r.json()['channelName']


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('README.md', 'w') as f:
        r = check()
        d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        f.write('\r\n'.join([
            f"""<p align="center">As of {d}</p>""",
        ] + (r.lower() != 'zwinplayer64' and [
            f"""<h1 align="center">VisualPlugin is not yet in the Byfron experiment.</h1>""",
            f"""He is still enrolled in the *{check()}* channel, or Hyperion might've already seeped into other live channels."""
        ] or [
            f"""<h1 align="center">VisualPlugin has been enrolled into the hellscape that is Byfron and its trumper anti-tamper antics!</h1>""",
            f"""Congrats!  I am no longer able to run Rsexec, *but* there are tools out there which could help mitigate the problem until Hyperion is fully released.  I used Requestly to force me to remain on the *LIVE* channel (script is in this repository), so I should be safe for now, as of 2023-04-25.  There are other solutions which work for TamperMonkey."""
        ])))

    subprocess.call(f'git add .')
    subprocess.call(f'git commit -m "{d}"')
    subprocess.call('git push')
