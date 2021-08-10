import tkinter as tk
import tkinter.simpledialog
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        #setting title
        self.root = root

        self.path = 'Y:\\'

        self.limits = {
            'C': {
                'min': None,
                'max': 22
            },
            'P': {
                'min': None,
                'max': 55
            },
            'Cu': {
                'min': None,
                'max': 40
            },
        }

        root.title("")
        #setting window size
        width=600
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        root.lift()
        root.attributes("-topmost", True)
        root.attributes('-toolwindow', True)

        ft1 = tkFont.Font(family='Times',size=24)
        ft2 = tkFont.Font(family='Times',size=20)
        ft3 = tkFont.Font(family='Times',size=50)

        def getProperties(
                widget,
                text,
                font=ft1,
                bg="#ff0000",
                fg="#333333",
                justify="center"):

            widget["text"] = text
            widget["font"] = font
            widget["bg"] = bg
            widget['fg'] = fg
            widget["justify"] = justify
            widget["borderwidth"] = "1px"
            widget["relief"] = "solid"


        self.heatNumber = tk.Label(root)
        self.heatNumber.place(x=0,y=0,width=200,height=50)
        getProperties(self.heatNumber, "HEAT NUMBER", ft1)

        self.department = tk.Label(root)
        self.department.place(x=200,y=0,width=200,height=50)
        getProperties(self.department, "DEPARTMENT", ft1)

        self.heatTime = tk.Label(root)
        self.heatTime.place(x=400,y=0,width=150,height=50)
        getProperties(self.heatTime, "TIME", ft1)

        self.settings = tk.Button(root)
        self.settings.place(x=550,y=0,width=50,height=50)
        self.settings["text"] = ":\\\\"
        self.settings["font"] = tkFont.Font(family='Arial', size=14, weight='bold')
        self.settings["bg"] = "#fafafa"
        self.settings["fg"] = "#ff0033"
        self.settings["command"] = self.settings_command

        self.cText = tk.Label(root)
        self.cText.place(x=0,y=50,width=200,height=30)
        getProperties(self.cText,"Carbon (C)", font=ft2, bg="#1e90ff")

        self.cLabel = tk.Label(root)
        self.cLabel.place(x=0,y=80,width=200,height=140)
        getProperties(self.cLabel,"C", font=ft3, bg="#999999")

        self.siText = tk.Label(root)
        self.siText.place(x=200,y=50,width=200,height=30)
        getProperties(self.siText,"Silicon (Si)", font=ft2, bg="#1e90ff")

        self.siLabel = tk.Label(root)
        self.siLabel.place(x=200,y=80,width=200,height=140)
        getProperties(self.siLabel,"Si", font=ft3, bg="#999999")

        self.mnText = tk.Label(root)
        self.mnText.place(x=400,y=50,width=200,height=30)
        getProperties(self.mnText,"Manganese (Mn)", font=ft2, bg="#1e90ff")

        self.mnLabel = tk.Label(root)
        self.mnLabel.place(x=400,y=80,width=200,height=140)
        getProperties(self.mnLabel,"Mn", font=ft3, bg="#999999")

        self.pText = tk.Label(root)
        self.pText.place(x=0,y=220,width=200,height=30)
        getProperties(self.pText,"Phosphor (P)", font=ft2, bg="#1e90ff")

        self.pLabel = tk.Label(root)
        self.pLabel.place(x=0,y=250,width=200,height=140)
        getProperties(self.pLabel,"P", font=ft3, bg="#999999")

        self.cuText = tk.Label(root)
        self.cuText.place(x=200,y=220,width=200,height=30)
        getProperties(self.cuText,"Copper (Cu)", font=ft2, bg="#1e90ff")

        self.cuLabel = tk.Label(root)
        self.cuLabel.place(x=200,y=250,width=200,height=140)
        getProperties(self.cuLabel,"Cu", font=ft3, bg="#999999")

        self.pbText = tk.Label(root)
        self.pbText.place(x=400,y=220,width=200,height=30)
        getProperties(self.pbText,"Lead (Pb)", font=ft2, bg="#1e90ff")

        self.pbLabel = tk.Label(root)
        self.pbLabel.place(x=400,y=250,width=200,height=140)
        getProperties(self.pbLabel,"Pb", font=ft3, bg="#999999")

        self.listBox = tk.Listbox(root)
        self.listBox.place(x=0,y=390,width=600,height=110)
        self.listBox["font"] = tkFont.Font(family='Arial',size=16)
        self.listBox["bg"] = "#fad400"
        self.listBox["fg"] = "#333333"
        self.listBox["borderwidth"] = "1px"
        self.listBox["relief"] = "solid"
        self.listBox["justify"] = "left"
        self.listBox["exportselection"] = "1"

        self.hideButton = tk.Button(root)
        self.hideButton.place(x=450,y=500,width=150,height=150)
        self.hideButton["font"] = tkFont.Font(family='Arial',size=36)
        self.hideButton["bg"] = "#5fb878"
        self.hideButton["fg"] = "#000000"
        self.hideButton["borderwidth"] = "1px"
        self.hideButton["relief"] = "solid"
        self.hideButton["justify"] = "center"
        self.hideButton["text"] = "HIDE"
        self.hideButton["command"] = self.hideButton_command

        self.logviewer = tk.Listbox(root)
        self.logviewer.place(x=0,y=500,width=450,height=150)
        self.logviewer["font"] = tkFont.Font(family='Arial',size=12)
        self.logviewer["bg"] = "#E2DFDE"
        self.logviewer["fg"] = "#333333"
        self.logviewer["borderwidth"] = "1px"
        self.logviewer["relief"] = "solid"
        self.logviewer["justify"] = "left"
        self.logviewer["exportselection"] = "1"


    def hideButton_command(self):
        # self.root.withdraw()
        self.root.iconify()


    def settings_command(self):
        dl = tkinter.simpledialog.askstring(
            title="PATH:",
            prompt="Enter new folder path: ",
            initialvalue=self.path)
        if dl and isinstance(dl, str):
            self.path = dl


    def log(self, text):
        self.logviewer.insert(0, text)


    def warnColor(self, widget, controler, value, colorMin="#D8E300", colorMax="#ff0000"):
        if controler[0] is not None and round(value) <= controler[0]:
            widget["fg"] = colorMin
        if controler[1] is not None and round(value) >= controler[1]:
            widget["fg"] = colorMax


    def update(self, heat):
        lastHeat = heat[0]

        self.heatNumber.configure(text=lastHeat[2])
        self.department.configure(text=lastHeat[3])
        self.heatTime.configure(text=lastHeat[0].strftime('%H:%M'))
        self.cLabel.configure(text=f'{lastHeat[9] * 100:.0f}')
        self.warnColor(self.cLabel, (self.limits['C']['min'], self.limits['C']['max']), lastHeat[9] * 100)
        self.siLabel.configure(text=f'{lastHeat[12] * 100:.0f}')
        self.mnLabel.configure(text=f'{lastHeat[15] * 100:.0f}')
        self.pLabel.configure(text=f'{lastHeat[21] * 1000:.0f}')
        self.warnColor(self.pLabel, (self.limits['P']['min'], self.limits['P']['max']), lastHeat[21] * 1000)
        self.cuLabel.configure(text=f'{lastHeat[24] * 100:.0f}')
        self.warnColor(self.cuLabel, (self.limits['Cu']['min'], self.limits['Cu']['max']), lastHeat[24] * 100)
        self.pbLabel.configure(text=f'{lastHeat[69] * 100:.0f}')

        def lbline(x):
            return f'{x[2]} {x[0].strftime("%H:%M")} {x[3]}: C:{x[9] * 100:.0f} Si:{x[12] * 100:.0f} Mn:{x[15] * 100:.0f} P:{x[21] * 1000:.0f} Cu:{x[24] * 100:.0f} Pb:{x[69] * 100:.0f}'

        self.listBox.delete(0, tk.END)

        for c, i in enumerate(heat[1]):
            self.listBox.insert(c, lbline(i))

        self.root.title(f'{lastHeat[2]} - {lastHeat[3]}')
        self.root.deiconify()
