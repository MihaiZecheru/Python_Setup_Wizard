from tkinter import *
from tkinter import ttk, messagebox
import os, sys
import requests, webbrowser
from time import sleep
from threading import Thread
from shutil import rmtree

'''
Application that sets up a coding environment for someone attempting to learn to code
'''

# constants
bg = '#8c8e8f'
fg = '#c8cbcc'
helv = ('Helvetica', 20, 'bold')
downloadLinks = {
    'python': "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe",
    'pycharm': "https://download.jetbrains.com/python/pycharm-community-2022.1.2.exe",
    'sublime': "https://download.sublimetext.com/sublime_text_build_4121_x64_setup.exe",
    'kite': "https://www.filehorse.com/download/file/GtpVx_9x3vTl9fe3WQa0sinj39Wzq859EiZ7Yw-haM-dEaXkk9mzaZqVYbeazdIV5801g-MtYWuKlbLxSHmPeX2bMutIml7It7kbPj9WhPE/",
    'grepper': "https://chrome.google.com/webstore/detail/grepper/amaaokahonnfjjemodnpmeenfpnnbkco",
    'vscode': "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
}
info = '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This program will install PyCharm (IDE), Sublime (IDE), and Python (programming language). 

Options for installing other useful addons such as Kite (AI), and Grepper (Google extension), and vscode (IDE)
will be presented after the main download
It is recommended to install these additional applications, as they are very useful

The video I used to learn will be presented at the end of all downloads, along with a discord invite link for people learning to code python

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

os.system('cls')


# for threads
def delayed_delete_function():
    sleep(6.5)  # time.sleep

    # remove the stdout texts
    app._temp0.destroy()
    app._temp1.destroy()
    app._temp2.destroy()

    app.update()


def finalChecker():
    while app._stopFinalChecker == False:
        sleep(1)
        if app._all_downloads_finished:
            app._stopFinalChecker = True
            app.videoAndDiscordInvite_screen()


def announceComplete():
    sleep(1)

    response = messagebox.askyesno('Install Kite',
                                   "Would you like to install Kite? It's an artificial intelligence client that will autocomplete your sentences as you code, which saves lots of time.")
    if response:
        for w in app.winfo_children():
            w.destroy()
        app.download_kite()
        sleep(5)
    else:
        app._isDownloading = False

    response = messagebox.askyesno('Install Grepper',
                                   "Would you like to install Grepper? It's a Google extension that will give user-added answers when you google a coding-related question, and it's surprisingly accurate. This is the top coding application someone could download, in my opinion.")
    if response:
        app.download_grepper()

    response = messagebox.askyesno('Install Visual Studio Code',
                                    "Would you like to install Visual Studio Code? This application is one of the best text editors you can find anywhere. It's great for intermediate developers, so it's great to have for when you get better!")
    if response:
        app.download_vscode()
    else:
        app._all_downloads_finished = True
        
    rmtree("C:/programming/exes")


def kiteDownloader():
    app._isDownloading = True
    path = "kite"
    app.label6 = Label(app, bg=bg, font=helv, text="Downloading Kite...")
    app.label6.pack(pady=200)
    app.update()
    app.label24 = Label(app, bg=bg, font=helv, text="This might take a while...")
    app.label24.pack()
    app.update()
    link = downloadLinks.get('kite')
    req = requests.get(link, allow_redirects=True)
    try:
        os.mkdir("C:/programming/TEMP")
    except FileExistsError:
        pass
    app.label13 = Label(app, bg=bg, font=helv, text="Almost done!")
    app.label13.pack(pady=50)
    app.update()
    open("C:/programming/TEMP/kite.exe", "wb").write(req.content)
    os.system("C:/programming/TEMP/%s.exe" % path)
    app.label6.destroy()
    app.label6 = Label(app, bg=bg, font=helv, text="Kite finished downloading")
    rmtree("C:/programming/TEMP")
    app._isDownloading = False
    sleep(4)
    app.label6.destroy()


def pythonDownloader():
    path = "python"

    # start download
    link = downloadLinks.get('python')
    req = requests.get(link, allow_redirects=True)
    app.update_progressBar(5, mode='add')
    open("C:/programming/exes/python.exe", "wb").write(req.content)
    app.update_progressBar(5, mode='add')
    os.system("C:/programming/exes/%s.exe" % path)

    # update bar
    app.update_progressBar(25, mode='add')

    # check if all are done
    if os.path.exists("C:/programming/exes/%s.exe" % path) and os.path.exists(
            "C:/programming/exes/%s.exe" % 'pycharm') and os.path.exists("C:/programming/exes/%s.exe" % 'sublime'):
        app._isDownloading = False
        app.mainDownloadFinished()


def pycharmDownloader():
    path = 'pycharm'

    # start download
    link = downloadLinks.get('pycharm')
    req = requests.get(link, allow_redirects=True)
    app.update_progressBar(5, mode='add')
    open("C:/programming/exes/pycharm.exe", "wb").write(req.content)
    app.update_progressBar(5, mode='add')
    os.system("C:/programming/exes/%s.exe" % path)

    # update bar
    app.update_progressBar(15, mode='add')

    # check if all are done
    if os.path.exists("C:/programming/exes/%s.exe" % path) and os.path.exists(
            "C:/programming/exes/%s.exe" % 'pycharm') and os.path.exists("C:/programming/exes/%s.exe" % 'sublime'):
        app._isDownloading = False
        app.mainDownloadFinished()


def sublimeDownloader():
    path = "sublime"

    # start download
    link = downloadLinks.get('sublime')
    req = requests.get(link, allow_redirects=True)
    app.update_progressBar(5, mode='add')
    open("C:/programming/exes/sublime.exe", "wb").write(req.content)
    app.update_progressBar(5, mode='add')
    os.system("C:/programming/exes/%s.exe" % path)

    # update bar
    app.update_progressBar(15, mode='add')

    # check if all are done
    if os.path.exists("C:/programming/exes/%s.exe" % path) and os.path.exists(
            "C:/programming/exes/%s.exe" % 'pycharm') and os.path.exists("C:/programming/exes/%s.exe" % 'sublime'):
        app._isDownloading = False
        app.mainDownloadFinished()

def vscodeDownloader():
    app._isDownloading = True
    path = "vscode"
    app.label17 = Label(app, bg=bg, font=helv, text="Downloading Visual Studio Code...")
    app.label17.pack(pady=200)
    app.update()
    app.label24 = Label(app, bg=bg, font=helv, text="This might take a while...")
    app.label24.pack()
    app.update()
    link = downloadLinks.get(path)
    req = requests.get(link, allow_redirects=True)
    try:
        os.mkdir("C:/programming/TEMP")
    except FileExistsError:
        pass
    app.label13 = Label(app, bg=bg, font=helv, text="Almost done!")
    app.label13.pack(pady=50)
    app.update()
    open("C:/programming/TEMP/vscode.exe", "wb").write(req.content)
    os.system("C:/programming/TEMP/%s.exe" % path)
    app.label6.destroy()
    app.label6 = Label(app, bg=bg, font=helv, text="Visual Studio Code finished downloading")
    rmtree("C:/programming/TEMP")
    app._isDownloading = False
    app._all_downloads_finished = True
    sleep(4)
    app.label6.destroy()



# create tk app
class App(Tk):
    def __init__(self, infoMessage):
        super().__init__()
        self.style = ttk.Style(self)
        self.style.theme_use('vista')
        self.title("Python Setup")
        self.iconbitmap('icon.ico')
        self.configure(bg=bg)

        # setup screen
        self.resizable(False, False)
        self.state('zoomed')
        self.attributes('-topmost', 1)
        self.update()
        self.attributes('-topmost', 0)

        # setup protocol and settings keybind
        self.protocol("WM_DELETE_WINDOW", self._close_app)

        # app constants
        self._isDownloading = False
        self._stopFinalChecker = False
        self._all_downloads_finished = False
        self.infoMessage = infoMessage

        # setup dirs
        self.setupDirs()

        # start app
        self.main_screen()

    def setupDirs(self):
        if not os.path.isdir('C:/programming'):
            os.mkdir('C:/programming')
        if not os.path.isdir('C:/programming/exes'):
            os.mkdir('C:/programming/exes')
        if not os.path.isdir('C:/programming/projects'):
            os.mkdir('C:/programming/projects')
        if not os.path.isdir('C:/programming/video_notes'):
            os.mkdir('C:/programming/video_notes')
        if not os.path.exists('C:/programming/video_link.txt'):
            with open('C:/programming/video_link.txt', 'w') as f:
                f.write("https://youtu.be/rfscVS0vtbw")
        if not os.path.exists('C:/programming/discord_link.txt'):
            with open('C:/programming/discord_link.txt', 'w') as f:
                f.write("https://discord.gg/A9d3TRK8kp")

    def _close_app(self):
        if self._isDownloading:
            allowProceed = messagebox.askokcancel('Download Interrupted',
                                                  'The installation is still running. If you quit now, the currently installing applications will self-delete in order to prevent file corruption.\n\nYou will have to run this program again to install these applications.')
            if allowProceed:
                # user pressed 'ok'

                # delete what has been installed so far to prevent corruption
                try:
                    rmtree("C:/programming/exes")
                except:
                    pass
                try:
                    rmtree("C:/programming/TEMP")
                except:
                    pass
                
                sys.exit()
        else:
            sys.exit()

    def main_screen(self):
        self.infoLabel = Label(self, text=self.infoMessage, font=helv, bg=bg)
        self.infoLabel.pack()

        self.frame_buttons = Frame(self, bg=bg)
        self.frame_buttons.pack(pady=10)

        self.button_proceed = Button(self.frame_buttons, text='Start Download', font=helv, padx=100, bg=fg,
                                     command=lambda: [self.main_download(), self.frame_buttons.destroy()])
        self.button_proceed.grid(row=0, column=0, padx=(0, 100))
        self.button_exit = Button(self.frame_buttons, text="I don't want to download this", font=helv, bg=fg,
                                  command=sys.exit)
        self.button_exit.grid(row=0, column=1)

        # for the progress bar
        self.frame_progressBar = Frame(self, bg=bg)
        self.frame_progressBar.pack()

        # 'console'; updates users on the download progress
        self.stdout = Frame(self, bg=bg)
        self.stdout.pack()

    def main_download(self):
        messagebox.showinfo('Notice',
                            "If it feels like a part of the download is taking a long time, check your taskbar at the bottom of your screen, as there may be an application prompt for you to accept!")
        self._isDownloading = True

        # setup progress bar
        self.progress_bar(mode='main')

        # begin downloads
        self.download_python()
        self._temp0 = Label(self.stdout, bg=bg, font=helv, text='Downloading Python...')
        self._temp0.pack(pady=(50, 0))
        self.download_pycharm()
        self._temp1 = Label(self.stdout, bg=bg, font=helv, text='Downloading PyCharm...')
        self._temp1.pack()
        self.download_sublime()
        self._temp2 = Label(self.stdout, bg=bg, font=helv, text='Downloading Sublime...')
        self._temp2.pack()

        delayed_delete = Thread(daemon=True, target=delayed_delete_function)
        delayed_delete.start()

    def mainDownloadFinished(self):
        for w in self.winfo_children():
            w.destroy()
        announceCompleteThread = Thread(daemon=True, target=announceComplete)
        announceCompleteThread.start()

        finalCheckerThread = Thread(daemon=True, target=finalChecker)
        finalCheckerThread.start()

    def videoAndDiscordInvite_screen(self):
        self._isDownloading = False
        for w in self.winfo_children():
            w.destroy()
        TEXTBOX_INFO = """  (Scroll)
          The downloading is over! All applications have been successfully downloaded to your computer.
        
        \tA new directory has been created for you while you were waiting. Take a look at C:/programming/
        
        \tJoin this discord to make learning to code easier: https://discord.gg/A9d3TRK8kp
        
        \tWatch this video to start learning: https://youtu.be/rfscVS0vtbw
        
        \tWhile watching the video, you should take notes on what he's teaching you,
        \tso that you can remember it better, and have the notes as a reference for later
        
        \tYou can put your finished notes ion C:/programming/video_notes/
        
        \tThe video and discord link are in your C:/programming/ directory, so don't worry about losing the links.
          
          Good Luck!"""

        self.textbox = Text(self, bg=fg, font=helv, width=100, height=18, borderwidth=0)
        self.textbox.pack(pady=400)
        self.textbox.insert(END, TEXTBOX_INFO)

    def progress_bar(self, downloadName=None, mode=None):
        if mode == None and downloadName is not None:
            self.downloadName = Label(self.frame_progressBar, bg=bg, text='Downloading {}...'.format(downloadName),
                                      font=helv)
            self.downloadName.pack()
            self.progress = ttk.Progressbar(self.frame_progressBar, orient=HORIZONTAL, length=1000, mode="determinate")
            self.progress.pack(pady=10)
            self.update_progressBar(0)
        elif mode == 'main' and downloadName == None:
            self.downloadName = Label(self.frame_progressBar, bg=bg, text='Downloading main applications...', font=helv)
            self.downloadName.pack()
            self.progress = ttk.Progressbar(self.frame_progressBar, orient=HORIZONTAL, length=1000, mode="determinate")
            self.progress.pack(pady=10)
            self.update_progressBar(0)

    def update_progressBar(self, x, mode='set'):
        if mode == 'set':
            self.progress['value'] = x
        elif mode == 'add':
            self.progress['value'] = self.progress['value'] + x

        self.update_idletasks()
        os.system('cls')

    # main download
    def download_python(self):
        self.update_progressBar(5, mode='add')
        pythonDownload = Thread(daemon=True, target=pythonDownloader)
        pythonDownload.start()

    def download_pycharm(self):
        self.update_progressBar(5, mode='add')
        pycharmDownload = Thread(daemon=True, target=pycharmDownloader)
        pycharmDownload.start()

    def download_sublime(self):
        self.update_progressBar(5, mode='add')
        sublimeDownload = Thread(daemon=True, target=sublimeDownloader)
        sublimeDownload.start()

    # extra downloads
    def download_kite(self):
        kiteDownload = Thread(daemon=True, target=kiteDownloader)
        kiteDownload.start()

    def download_grepper(self):
        link = downloadLinks.get('grepper')
        webbrowser.open(link)

    def download_vscode(self):
        vscodeDownload = Thread(daemon=True, target=vscodeDownloader)
        vscodeDownload.start()


if __name__ == '__main__':
    app = App(info)
    app.mainloop()