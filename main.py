# pretty sure this needs no explanation. Just an extremely simple but useful program I made for myself

import webbrowser
import os
import PySimpleGUI as pg

pg.theme("DarkBlue14")

layout = [
    [pg.VPush()],
    [pg.Text("What do you wanna do today?")],
    [pg.Button("school things")],
    [pg.Button("work on my programming project")],
    [pg.Button("talk with my friends")],
    [pg.Button("just chill")],
    [pg.Button("play video games(imagine)")],
    [pg.Button("do some things to help my dad")],
    [pg.Button("nothing")],
    [pg.VPush()]
]

window = pg.Window("startup manager", layout, size=(1920, 1200), element_justification="c", font="Any 20").Finalize()
window.Maximize()
event= window.read()[0]
match event:
    case "school things":
        webbrowser.open_new("https://www.htl-klu.at/intern/quick-links")
        webbrowser.open_new_tab("https://klio.webuntis.com/timetable-students-my/2022-11-02")
    case "work on my programming project":
        os.system("D:/VSC/code.exe")
    case "talk with my friends":
        os.system("C:/Users/jonas/AppData/Local/Discord/app-1.0.9007/discord.exe")
    case "just chill":
        webbrowser.open_new("https://www.youtube.com/playlist?list=WL")
    case "play video games(imagine)":
        os.system("C:/Users/jonas/Desktop/steam.lnk")
    case "do some things to help my dad":
        window.close()
        os.system("node-red")
    case "nothing":
        os.system("shutdown /p")