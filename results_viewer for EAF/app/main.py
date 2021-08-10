import csv
import os
from datetime import datetime
import time
import tkinter as tk

from gui import App


root = tk.Tk()
app = App(root)

LAST_HEAT = None


def checkHeats(path):
    # returns last heat and next 4 heats

    if not os.path.exists(app.path):
        return False

    heats = []
    # loop through last 20 csv file
    csv_files = sorted(os.listdir(path), reverse=True)[:20]
    counter = 0
    for csv_file in csv_files:
        # be sure that its a csv file
        if csv_file.split('.')[-1] == 'csv':
            file = os.path.abspath(os.path.join(path, csv_file))
            # open for read
            with open(file, 'r') as f:
                # prepare to read
                reader = list(csv.reader(f))[0]

                # check if EAF result
                if reader[3][:3] == "EAF":
                    reader = [int(i) if i.isdigit() else float(i) if i.replace('.','',1).isdigit() else i for i in reader]
                    reader[0] = datetime.strptime(reader[0], '%Y-%b-%d %X')
                    reader[69] = float(reader[69])
                    # add to heats
                    heats.append(reader)
                    # increase counter
                    counter += 1
        # exit after 5 heats
        if counter >= 5:
            break

    if len(heats) == 0:
        return None

    return (heats[0], heats[1:] if len(heats) > 1 else heats[0])


def checkCurrentHeat():

    global LAST_HEAT

    last5heats = checkHeats(app.path)

    if last5heats is False:
        app.log(f'Error: results folder path not found: {app.path}')
        return False

    if last5heats is None:
        app.log(f'No EAF results founded, skipping...')
        return False


    currentHeat = last5heats[0]
    otherHeats = last5heats[1]

    if currentHeat != LAST_HEAT:
        # updateAndShowTkWindow(last5heats)
        app.update(last5heats)
        LAST_HEAT = currentHeat
        app.log(f'Analyse result updated: heat {currentHeat[2]} {currentHeat[3]}')
    else:
        app.log(f'Results checked, no update required: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')



# create function to run every n secs
loop_secs = 3000
def task():
    checkCurrentHeat()
    root.after(loop_secs, task)

# show window
checkCurrentHeat()

# check update for every n secs
root.after(loop_secs, task)
