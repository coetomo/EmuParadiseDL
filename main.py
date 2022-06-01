import base64
import tkinter as tk
import webbrowser
from tkinter import messagebox as mb

import requests

VERSION = "1.0.1"
WIN_WIDTH, WIN_HEIGHT = 290, 255


def get_download_url(from_url):
    pageid = from_url.rsplit('/', 1)[-1]
    # pageid => 'id-download'
    if '-' in pageid:
        pageid = pageid.split('-', 1)[0]

    request_url = f"https://www.emuparadise.me/roms/get-download.php?gid={pageid}&test=true"

    response = requests.get(request_url, headers={"Referer": from_url}, allow_redirects=False)
    dl_link = response.headers.get('Location', None)
    return dl_link if dl_link else None
    len_link = len(dl_link)
    print("=" * (len_link + 4))
    print(f"| {dl_link} |");
    print("=" * (len_link + 4))


def test_print(entry):
    url = entry.get()
    print(f"Got URL: [{url}]")
    print(f"DL URL: [{get_download_url(url)}]")


def auto_download_browser(entry):
    url = entry.get()
    if not url:
        mb.showerror(title="Error",
                     message="URL field is empty. PLease enter the URL page before pressing this button!")
        return

    dlurl = get_download_url(url)
    if dlurl is None:
        mb.showerror(title="Error",
                     message="Invalid URL! Please ensure that it is a URL for the game page!")
        return
    webbrowser.open(dlurl)


def show_download_link(entry, text):
    url = entry.get()
    if not url:
        mb.showerror(title="Error",
                     message="URL field is empty. PLease enter the URL page before pressing the button!")
        return
    dlurl = get_download_url(url)
    if dlurl is None:
        mb.showerror(title="Error",
                     message="Invalid URL! Please ensure that it is a URL for the game page!")
        return
    text.configure(state='normal')
    text.delete('1.0', tk.END)
    text.insert('end', dlurl)
    text.configure(state='disabled')


def show_about():
    mb.showinfo(title="About",
                message=f"EmuParadiseDL v{VERSION}\nAuthor: Chris Oetomo (coetomo @ GitHub)\nMore features coming soon!")


if __name__ == '__main__':
    win = tk.Tk()
    icon = \
        """AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAD0//8B9P//AfT//wH0//8BPWAdT4GUAKmRpADLlKYA2ZSmANuUpQDPipoAsXuMAGP0//8B
9P//AfT//wH0//8B9P//AfT//wH0//8BztUATazGAP/d9wD/7P8A/+3/AP/t/wD/6/8A/+H8AP+/
2AD/prgAbfT//wH0//8B9P//AfT//wH0//8B9P//AazOALvj/gD/3/wA/5OpAP/+/wD///8A/5es
AP/b9gD/8v8A/7nOAN07Wx8F9P//AfT//wH0//8BM29THwA+CLGKrAD96v8A/9n2AP99kwD///8A
////AP9/lgD/zOkA//b/AP+bswD/AD0TwwBBFTH0//8BAGAAIQBjAN0AWQD/AF0A/3meAP+0xgD/
tsEA/9DjAP/Q5QD/sb0A/7DBAP+KpQD/FF4A/wBQAP8AXADvAEINNwB3AJcAdwD/AHgA/wBvAP8A
ZAD/AGkA/yN1AP86ewD/PHoA/yZxAP8FYgD/AFYA/wBgAP8AbAD/AG8A/wBuALOl1ADVYLoA/wCQ
AP8AkgD/AI8A/wCIAP8AgQD/AHwA/wB5AP8AdgD/AHcA/wB8AP8AfgD/AHwA/zWYAP+hyADh//8A
7y65AP8AoAD/AKMA/wCiAP8ArwD/JbsA/wCeAP8AmAD/AKUA/wSmAP8AkAD/AI4A/wCMAP8AmAD/
9fgA7f//AN8YvwD/AKoA/wCtAP8AqQD/NcwA////AP/R/wD/s/YA////AP+C3gD/AJ0A/wCdAP8A
mgD/AKIA//L/AOfm/wCxYtwA/wCtAP8AsQD/AK0A/wPIAP///wD///8A////AP///wD/UdQA/wCm
AP8ApwD/AKIA/yi6AP/0/wDLG74AWQC3AP8AsAD/ALAA/wC7AP/C/wD///8A////AP///wD///8A
/+H/AP8AuwD/AKwA/wCqAP8ArQD/DLUAgwC2HQkArwDTALEA/wCyAP+L9wD///8A////AP///wD/
//8A////AP///wD/tP8A/wCxAP8ArwD/AK4A7wC2ABv0//8BALgAPwC0AP8AsgD/ALwA/xjMAP+c
/QD///8A////AP/D/wD/PNYA/wDAAP8AsgD/ALEA/wC5AF/0//8B9P//AfT//wEArQB1ALQA/wCy
AP8AsAD/ALUA/9//AP///wD/ALoA/wCvAP8AsgD/ALQA/wCrAJP0//8B9P//AfT//wH0//8B9P//
AQC0AFUAtADjALQA/wCxAP8AxAD/AMgA/wCxAP8AswD/ALMA7QCyAGn0//8B9P//AfT//wH0//8B
9P//AfT//wH0//8BAKYAFwCzAG0AtACzALIA1QCyANkAtAC7ALgAfQCuAB/0//8B9P//AfT//wH0
//8BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAA=="""
    icondata = base64.b64decode(icon)
    tempFile = "icon.ico"
    iconfile = open(tempFile, "wb")
    iconfile.write(icondata)
    iconfile.close()
    win.iconbitmap("icon.ico")
    win.title('EmuParadiseDL')
    win.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
    win.minsize(width=WIN_WIDTH, height=WIN_HEIGHT)
    win.maxsize(width=WIN_WIDTH, height=WIN_HEIGHT)

    menubar = tk.Menu(win)
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=show_about)
    helpmenu.add_separator()
    helpmenu.add_command(label="Exit", command=win.quit)
    menubar.add_cascade(label="Help", menu=helpmenu)
    win.config(menu=menubar)

    row = tk.Frame(win)
    lab = tk.Label(row, text="Enter the Emuparadise game page URL", font=('Verdana', 10), anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, pady=15)
    lab.pack(side=tk.TOP)
    ent.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X, padx=10)

    win.bind('<Return>', lambda event, e=ent: show_download_link(e))
    auto_download_button = tk.Button(win, text='Download from Browser', font=('Verdana', 9, "bold"), height=3,
                                     borderwidth=2, command=lambda e=ent: auto_download_browser(e))
    auto_download_button.pack(fill=tk.X, pady=3, padx=10)
    show_textbox = tk.Text(win, state='disabled', height=3)
    show_link_button = tk.Button(win, text='Show Download Link', font=('Verdana', 9), height=3,
                                 borderwidth=2, command=lambda e=ent, text=show_textbox: show_download_link(e, text))
    show_link_button.pack(fill=tk.X, pady=3, padx=10)
    show_textbox.pack(fill=tk.X, padx=10)
    win.mainloop()
