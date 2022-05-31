import tkinter as tk
import webbrowser
from tkinter import messagebox as mb

import requests

VERSION = "1.00"
WIN_WIDTH, WIN_HEIGHT = 290, 255


def get_download_url(from_url):
    pageid = from_url.rsplit('/', 1)[-1]
    request_url = f"https://www.emuparadise.me/roms/get-download.php?gid={pageid}&test=true"

    response = requests.get(request_url, headers={"Referer": from_url}, allow_redirects=False)
    dl_link = response.headers['Location']
    return dl_link
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
    webbrowser.open(dlurl)


def show_download_link(entry, text):
    url = entry.get()
    if not url:
        mb.showerror(title="Error",
                     message="URL field is empty. PLease enter the URL page before pressing the button!")
        return
    dlurl = get_download_url(url)
    text.configure(state='normal')
    text.delete('1.0', tk.END)
    text.insert('end', dlurl)
    text.configure(state='disabled')


def show_about():
    mb.showinfo(title="About",
                message=f"EmuParadiseDL v{VERSION}\nAuthor: Chris Oetomo\n(more features coming soon)")


if __name__ == '__main__':
    win = tk.Tk()
    win.iconbitmap("epdl.ico")
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
