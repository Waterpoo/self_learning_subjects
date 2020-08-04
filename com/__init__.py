老师您好 我根据您的算法已经完成了界面和操作 但是目前遇到的情况是根据这个算法计算出的结果导致游戏在早期就超过三次的爆牌(超过21点)以至于后续的游戏其实是无法进行的 之前和您联系也没有收到您的答复 
还请您尽快给予答复 我昨天一天一夜没睡都是在自己写代码    拜托了     我的代码已经付在了下面

import random
from tkinter import *

# ====================================================================================================================

fullDeck = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5",
            "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9",
            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", ".", ".", "1", "1", "1", "1"]
tempDeck = list(fullDeck)
col0 = ["", "", "", "", ""]
col1 = ["", "", "", "", ""]
col2 = ["", "", "", "", ""]
col3 = ["", "", "", "", ""]


def purge_cols():
    global col0, col1, col2, col3
    sum0, sum1, sum2, sum3 = 0, 0, 0, 0
    for i in range(len(col0)):
        if col0[i] != "":
            sum0 += int(col0[i])
        if col1[i] != "":
            sum1 += int(col1[i])
        if col2[i] != "":
            sum2 += int(col2[i])
        if col3[i] != "":
            sum3 += int(col3[i])
    if sum0 >= 21 or col0[4] != "":
        for j1 in range(1, 6):
            exec(f'label_0_{j1}.config(text="")')
            col0 = ["", "", "", "", ""]
    if sum1 >= 21 or col1[4] != "":
        for j2 in range(1, 6):
            exec(f'label_1_{j2}.config(text="")')
            col1 = ["", "", "", "", ""]
    if sum2 >= 21 or col2[4] != "":
        for j3 in range(1, 6):
            exec(f'label_2_{j3}.config(text="")')
            col2 = ["", "", "", "", ""]
    if sum3 >= 21 or col3[4] != "":
        for j4 in range(1, 6):
            exec(f'label_3_{j4}.config(text="")')
            col3 = ["", "", "", "", ""]

def update_remains():
    global v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11
    if e.get() == list_deck_detail[0]:
        v_1 -= 1
        label_remain_1n.config(text=v_1)
    if e.get() == list_deck_detail[1]:
        v_2 -= 1
        label_remain_2n.config(text=v_2)
    if e.get() == list_deck_detail[2]:
        v_3 -= 1
        label_remain_3n.config(text=v_3)
    if e.get() == list_deck_detail[3]:
        v_4 -= 1
        label_remain_4n.config(text=v_4)
    if e.get() == list_deck_detail[4]:
        v_5 -= 1
        label_remain_5n.config(text=v_5)
    if e.get() == list_deck_detail[5]:
        v_6 -= 1
        label_remain_6n.config(text=v_6)
    if e.get() == list_deck_detail[6]:
        v_7 -= 1
        label_remain_7n.config(text=v_7)
    if e.get() == list_deck_detail[7]:
        v_8 -= 1
        label_remain_8n.config(text=v_8)
    if e.get() == list_deck_detail[8]:
        v_9 -= 1
        label_remain_9n.config(text=v_9)
    if e.get() == list_deck_detail[9]:
        v_10 -= 1
        label_remain_10n.config(text=v_10)
    if e.get() == list_deck_detail[10]:
        v_11 -= 1
        label_remain_11n.config(text=v_11)


def choose_location():
    card = e.get()
    global col0, col1, col2, col3
    sum0, sum1, sum2, sum3 = 0, 0, 0, 0

    if card != '1' and card != '0' and card != '.':
        card = int(card)
    elif card == '0':
        card = 10
    elif card == '.':
        card = 21
    elif card == '1':
        card_1 = [1, 11]
        for k in range(0, 4):
            if eval(f'21 - sum{k} == 11'):
                card = card_1[1]
                return int(f'{k}')
            else:
                card = card_1[0]
                return int(f'{k}')
    if sum0 + card == 21:
        return 0
    if sum1 + card == 21:
        return 1
    if sum2 + card == 21:
        return 2
    if sum3 + card == 21:
        return 3
    else:
        return random.randint(0, 3)


def positioning_card(c):
    for i in range(1, 6):
        if eval(f'label_{c}_{i}["text"] == ""'):
            if e.get() != '1' and e.get() != '0' and e.get() != '.':
                exec(f'col{c}[{i - 1}] = {e.get()}')
            elif e.get() == '0':
                exec(f'col{c}[{i-1}] = "10"')
            elif e.get() == '.':
                exec(f'col{c}[{i-1}] = "21"')
            elif e.get() == '1':
                temp_sum = 0
                for j1 in range(0, 4):
                    if eval(f'col{c}[{j1}] != ""'):
                        temp_sum += int(eval(f'col{c}[{j1}]'))
                if (temp_sum + 11) <= 21:
                    exec(f'col{c}[{i-1}] = "11"')
                else:
                    exec(f'col{c}[{i-1}] = "1"')

            exec(f'label_{c}_{i}.config(text=e.get())')
            break


def verifycard(cardinput):
    if cardinput not in tempDeck:
        label_alert.config(bg="red", text="Wrong entry")
        return False
    else:
        label_alert.config(bg='SystemButtonFace', text="")
        return True


def submit(event):
    global cardRemainder
    if verifycard(e.get()):
        positioning_card(choose_location())
        purge_cols()
        tempDeck.remove(e.get())
        cardRemainder -= 1
        label_cardsleft.config(text=cardRemainder)
        update_remains()
        print(f'{col0}\n{col1}\n{col2}\n{col3}\n')
    e.delete(0, END)


def reset_labels():
    global tempDeck, cardRemainder, col0, col1, col2, col3
    col0 = ["", "", "", "", ""]
    col1 = ["", "", "", "", ""]
    col2 = ["", "", "", "", ""]
    col3 = ["", "", "", "", ""]
    tempDeck = list(fullDeck)
    for i in range(1, 10):
        exec("label_remain_%dn.config(text='4')" % i)
    label_remain_11n.config(text="2")
    label_remain_10n.config(text="14")
    for temp_row in range(1, 6):
        for temp_col in range(0, 4):
            exec("label_%d_%d.config(text='')" % (temp_col, temp_row))
    e.delete(0, END)
    label_alert.config(bg='SystemButtonFace', text="")
    cardRemainder = len(fullDeck)
    label_cardsleft.config(text=cardRemainder)


root = Tk()
w = 600  # width for the Tk root
h = 420  # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the scedreen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("21 Blitz")

frame1 = Frame(root, borderwidth=2, relief="sunken")
frame2 = Frame(root, relief="sunken", padx=3, pady=10)
frame3 = Frame(root, relief="sunken", padx=3)
label_column1 = Label(frame1, text='col1', borderwidth=1, relief="groove", width=15, height=2).grid(column=0, row=0)
label_column2 = Label(frame1, text='col2', borderwidth=1, relief="groove", width=15, height=2).grid(column=1, row=0)
label_column3 = Label(frame1, text='col3', borderwidth=1, relief="groove", width=15, height=2).grid(column=2, row=0)
label_column4 = Label(frame1, text='col4', borderwidth=1, relief="groove", width=15, height=2).grid(column=3, row=0)

label_empty2 = Label(frame1, text='', width=5, height=2).grid(column=4, row=1)
label_empty3 = Label(frame1, text='', width=5, height=2).grid(column=4, row=3)
label_empty4 = Label(frame1, text='', width=5, height=2).grid(column=4, row=5)
label_alert = Label(frame1, text='', width=13, height=2, padx=4, borderwidth=1, relief="sunken")
label_alert.grid(column=5, row=0, columnspan=2)

label_0_1 = Label(frame1, text=col0[0], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_0_1.grid(column=0, row=1)
label_0_2 = Label(frame1, text=col0[1], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_0_2.grid(column=0, row=2)
label_0_3 = Label(frame1, text=col0[2], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_0_3.grid(column=0, row=3)
label_0_4 = Label(frame1, text=col0[3], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_0_4.grid(column=0, row=4)
label_0_5 = Label(frame1, text=col0[4], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_0_5.grid(column=0, row=5)

label_1_1 = Label(frame1, text=col1[0], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_1_1.grid(column=1, row=1)
label_1_2 = Label(frame1, text=col1[1], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_1_2.grid(column=1, row=2)
label_1_3 = Label(frame1, text=col1[2], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_1_3.grid(column=1, row=3)
label_1_4 = Label(frame1, text=col1[3], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_1_4.grid(column=1, row=4)
label_1_5 = Label(frame1, text=col1[4], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_1_5.grid(column=1, row=5)

label_2_1 = Label(frame1, text=col2[0], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_2_1.grid(column=2, row=1)
label_2_2 = Label(frame1, text=col2[1], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_2_2.grid(column=2, row=2)
label_2_3 = Label(frame1, text=col2[2], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_2_3.grid(column=2, row=3)
label_2_4 = Label(frame1, text=col2[3], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_2_4.grid(column=2, row=4)
label_2_5 = Label(frame1, text=col2[4], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_2_5.grid(column=2, row=5)

label_3_1 = Label(frame1, text=col3[0], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_3_1.grid(column=3, row=1)
label_3_2 = Label(frame1, text=col3[1], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_3_2.grid(column=3, row=2)
label_3_3 = Label(frame1, text=col3[2], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_3_3.grid(column=3, row=3)
label_3_4 = Label(frame1, text=col3[3], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_3_4.grid(column=3, row=4)
label_3_5 = Label(frame1, text=col3[4], width=10, height=3, bg="white", borderwidth=1, relief="solid")
label_3_5.grid(column=3, row=5)

v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11 = 4, 4, 4, 4, 4, 4, 4, 4, 4, 14, 2

label_remain_1 = Label(frame2, text='A', font="7", relief="groove", width=4).grid(column=0, row=0)
label_remain_1n = Label(frame2, text=v_1, relief="groove", width=5, padx=4)
label_remain_1n.grid(column=0, row=1)

label_remain_2 = Label(frame2, text='2', font="7", relief="groove", width=4).grid(column=1, row=0)
label_remain_2n = Label(frame2, text=v_2, relief="groove", width=5, padx=4)
label_remain_2n.grid(column=1, row=1)

label_remain_3 = Label(frame2, text='3', font="7", relief="groove", width=4).grid(column=2, row=0)
label_remain_3n = Label(frame2, text=v_3, relief="groove", width=5, padx=4)
label_remain_3n.grid(column=2, row=1)

label_remain_4 = Label(frame2, text='4', font="7", relief="groove", width=4).grid(column=3, row=0)
label_remain_4n = Label(frame2, text=v_4, relief="groove", width=5, padx=4)
label_remain_4n.grid(column=3, row=1)

label_remain_5 = Label(frame2, text='5', font="7", relief="groove", width=4).grid(column=4, row=0)
label_remain_5n = Label(frame2, text=v_5, relief="groove", width=5, padx=4)
label_remain_5n.grid(column=4, row=1)

label_remain_6 = Label(frame2, text='6', font="7", relief="groove", width=4).grid(column=5, row=0)
label_remain_6n = Label(frame2, text=v_6, relief="groove", width=5, padx=4)
label_remain_6n.grid(column=5, row=1)

label_remain_7 = Label(frame2, text='7', font="7", relief="groove", width=4).grid(column=6, row=0)
label_remain_7n = Label(frame2, text=v_7, relief="groove", width=5, padx=4)
label_remain_7n.grid(column=6, row=1)

label_remain_8 = Label(frame2, text='8', font="7", relief="groove", width=4).grid(column=7, row=0)
label_remain_8n = Label(frame2, text=v_8, relief="groove", width=5, padx=4)
label_remain_8n.grid(column=7, row=1)

label_remain_9 = Label(frame2, text='9', font="7", relief="groove", width=4).grid(column=8, row=0)
label_remain_9n = Label(frame2, text=v_9, relief="groove", width=5, padx=4)
label_remain_9n.grid(column=8, row=1)

label_remain_10 = Label(frame2, text='10', font="7", relief="groove", width=4).grid(column=9, row=0)
label_remain_10n = Label(frame2, text=v_10, relief="groove", width=5, padx=4)
label_remain_10n.grid(column=9, row=1)

label_remain_11 = Label(frame2, text='B', font="7", relief="groove", width=4).grid(column=10, row=0)
label_remain_11n = Label(frame2, text=v_11, relief="groove", width=5, padx=4)
label_remain_11n.grid(column=10, row=1)

list_deck_detail = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

button_reset = Button(frame1, text='Reset', width=13, height=2, padx=4, command=reset_labels)
button_reset.grid(column=5, row=2, columnspan=2)

e = Entry(frame1, width=8, relief="solid", borderwidth=1, font=("", 14))
e.grid(column=5, row=4, columnspan=2)
e.bind("<Return>", submit)



cardRemainder = StringVar()
cardRemainder = len(fullDeck)

label_cardsleft = Label(frame1, text=cardRemainder, width=13, height=2, padx=4, borderwidth=1, relief="sunken")
label_cardsleft.grid(column=5, row=6, columnspan=2)

frame1.pack(fill="both", expand=True)
frame2.pack(fill=None, expand=False)

root.mainloop()
