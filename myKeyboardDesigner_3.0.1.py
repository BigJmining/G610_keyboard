#!/usr/bin/env python3
from time import sleep
import subprocess as sub
import os, sys, random

from tkinter import *

root = Tk()
root.title('My Keyboard')
root.configure(bg='grey8')
root.resizable(False,False)

bg_color = 'black'
fg_keys = 'white'
bg_hotkey = 'red3'
fg_hotkey = 'snow'

def quitapp():
    if len(user_settings) != len():
        print('changes')
    else:
        root.destroy()

## used to change a key or csv set of keys
def change():
    a_key.set(key_to_change.get())
    invalid.grid_forget()

    # print(brightness.get(), a_key.get())
    if len(a_key.get()) > 1:
        if a_key.get()[1] in (','):
            alpha = a_key.get().split(',')
            for x in range(len(alpha)):
                sub.check_output(f'g610-led -k {str(alpha[x])} {str(brightness.get()).zfill(2)}',shell=True)
                with open('g610/current_session_keyboard_lights.txt','a') as f:
                    command = f'g610-led -k {str(alpha)} {str(brightness.get()).zfill(2)};'
                    f.write(command)
                    f.close()
        elif a_key.get()[0] == ('f'):
            alpha = a_key.get()#.split(',')
            sub.check_output(f'g610-led -k {str(alpha)} {str(brightness.get()).zfill(2)}',shell=True)
            with open('g610/current_session_keyboard_lights.txt','a') as f:
                    command = f'g610-led -k {str(alpha)} {str(brightness.get()).zfill(2)};'
                    f.write(command)
                    f.close()
        
    
    elif len(a_key.get()) == 0:
        invalid.grid(row=3, column=0, pady=5, columnspan=3)
            
    else:
        try:
            sub.check_output(f'g610-led -k {str(a_key.get())} {str(brightness.get()).zfill(2)}',shell=True)
            with open('g610/current_session_keyboard_lights.txt','a') as f:
                command = f'g610-led -k {str(a_key.get())} {str(brightness.get()).zfill(2)};'
                f.write(command)
                f.close()
        except sub.CalledProcessError as e:
            print(e)
    

    key_to_change.delete(0,END)




## Keybaord image
keyboard_window = LabelFrame(root, bg='grey10', bd=4)
keyboard_window.grid(row=4, column=0, columnspan=4, padx=20, pady=20)

k_blank1 = Button(keyboard_window,text='   \n  ',bg=bg_color, fg=bg_color, )


profile_of_keyboard = []

record_session = []

command_var = StringVar()  # used??

def key_click(b,t):
    b.configure(fg=f'grey{int(brightness.get())}',)
    profile_of_keyboard.append((t,brightness.get()))
    
    sub.check_output(f'g610-led -k {t} {brightness.get().zfill(2)}',shell=True)
    with open('g610/current_session_keyboard_lights.txt','a') as f:
        command = f'g610-led -k {t} {brightness.get().zfill(2)};'
        f.write(command)
        f.close()

k_logo = Button(keyboard_window, text='G\nlogo', bg=bg_color, fg=fg_keys, font='system 16',
    command=lambda: key_click(b=k_logo,t='logo'),)
k_logo.grid(columnspan=2, rowspan=2, sticky=NW)
k_num_indicator = Button(keyboard_window,text='-#-\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num_indicator,t='num_indicator'),)
k_caps_indicator = Button(keyboard_window,text='-X-\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_caps_indicator,t='caps_indicator'),)
k_scroll_indicator = Button(keyboard_window,text='-^-\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_scroll_indicator,t='scroll_indicator'),)
k_game = Button(keyboard_window,text='-&-\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_game,t='gamemode'),)
k_backlight = Button(keyboard_window,text='-!-\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_backlight,t='backlight'),)
k_mute = Button(keyboard_window,text='Sss\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_mute,t='mute'),)   

row0_key_layout = [k_logo,k_blank1,k_blank1,k_blank1,k_blank1,k_blank1,k_blank1,
k_blank1,k_blank1,k_blank1,k_blank1,k_blank1,k_num_indicator,k_caps_indicator,k_scroll_indicator,
                    k_blank1,k_blank1,k_game,k_blank1,k_backlight,k_mute,]

for x in range(len(row0_key_layout)):    
    for btn in row0_key_layout:
        row0_key_layout[x].grid(row=0, column=x, padx=3, pady=35)


## build row 1 of keyboard (top)
k_esc= Button(keyboard_window, text='esc\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_esc,t='esc'),)

k_f1= Button(keyboard_window,text='F1\n', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f1,t='f1'),)
k_f2= Button(keyboard_window,text='F2\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f2,t='f2'),)
k_f3= Button(keyboard_window,text='F3\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f3,t='f3'),)
k_f4= Button(keyboard_window,text='F4\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f4,t='f4'),)
k_f5= Button(keyboard_window,text='F5\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f5,t='f5'),)
k_f6= Button(keyboard_window,text='F6\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f6,t='f6'),)
k_f7= Button(keyboard_window,text='F7\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f7,t='f7'),)
k_f8= Button(keyboard_window,text='F8\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f8,t='f8'),)
k_f9= Button(keyboard_window,text='F9\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f9,t='f9'),)
k_f10= Button(keyboard_window,text='F10\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f10,t='f10'),)
k_f11= Button(keyboard_window,text='F11\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f11,t='f11'),)
k_f12= Button(keyboard_window,text='F12\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f12,t='f12'),)
k_print= Button(keyboard_window,text='prnt\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_print,t='print'),)
k_scrolllock= Button(keyboard_window,text='scrl\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_scrolllock,t='scrolllock'),)
k_break= Button(keyboard_window,text='brak\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_break,t='break'),)
k_play= Button(keyboard_window,text='play\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_play,t='play'),)
k_stop= Button(keyboard_window,text='stop\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_stop,t ='stop'),)
k_prev= Button(keyboard_window,text='prev\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_prev,t='prev'),)
k_next= Button(keyboard_window,text='next\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_next,t='next'),)

# set row 1 to board
row1_key_layout = [
    k_esc, k_blank1, k_f1,k_f2,k_f3,k_f4, k_blank1, k_f5,k_f6,
    k_f7,k_f8, k_blank1 ,k_f9,k_f10,k_f11,k_f12,k_blank1,k_print,
    k_scrolllock, k_break , k_blank1,k_play,k_stop,k_prev,k_next,
]

for x in range(len(row1_key_layout)):
    
    for btn in row1_key_layout:
        row1_key_layout[x].grid(row=1, column=x, padx=3, pady=5)

# build row 2 of keyboard 
k_tilde= Button(keyboard_window, text=' `\n~  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_tilde,t='tilde'),)
k_1= Button(keyboard_window,text=' 1\n!  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_1,t='1'),)
k_2= Button(keyboard_window,text=' 2\n@  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_2,t='2'),)
k_3= Button(keyboard_window,text=' 3\n#  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_3,t='3'),)
k_4= Button(keyboard_window,text=' 4\n$  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_4,t='4'),)
k_5= Button(keyboard_window,text=' 5\n%',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_5,t='5'),)
k_6= Button(keyboard_window,text=' 6\n^',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_6,t='6'),)
k_7= Button(keyboard_window,text=' 7\n&',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_7,t='7'),)
k_8= Button(keyboard_window,text=' 8\n*',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_8,t='8'),)
k_9= Button(keyboard_window,text=' 9\n(',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_9,t='9'),)
k_0= Button(keyboard_window,text=' 0\n)',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_0,t='0'),)

k_minus= Button(keyboard_window,text=' -\n_ ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_minus,t='minus'),)
k_equal= Button(keyboard_window,text=' =\n+  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_equal,t='equal'),)
k_backspace= Button(keyboard_window,text=' back\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_backspace,t='back'),)
k_backspace.grid(columnspan=2, sticky=W)
k_insert= Button(keyboard_window,text='inrt\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_insert,t='insert'),)
k_home= Button(keyboard_window,text='home\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_home,t='home'),)
k_pageup= Button(keyboard_window,text='pgup\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_pageup,t='pageup'),)
k_numlock= Button(keyboard_window,text='num\nlock',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numlock,t='numlock'),)
k_numslash= Button(keyboard_window,text=' /\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numslash,t='numslash'),)
k_numastrisk= Button(keyboard_window,text=' *\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numastrisk,t='numasterisk'),)
k_numminus= Button(keyboard_window,text=' -\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numminus,t='numminus'),)
# set row 2 to board
row2_key_layout = [
    k_tilde, k_1, k_2, k_3, k_4, k_5, k_6,
    k_7, k_8, k_9, k_0, k_minus, k_equal, k_backspace, k_blank1, k_insert, k_home, k_pageup,
    k_blank1, k_blank1,k_blank1,k_numlock, k_numslash, k_numastrisk, k_numminus,
]
for x in range(len(row2_key_layout)):
    for btn in row2_key_layout:
        row2_key_layout[x].grid(row=2,column=x, padx=5, pady=10, ipadx=6)

# build row 3 of keyboard 
k_tab= Button(keyboard_window, text='TAB\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_tab,t='tab'),)
k_tab.grid(columnspan=2, sticky=W, ipadx=12,)
k_q= Button(keyboard_window,text=' Q\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_q,t='q'),)
k_w= Button(keyboard_window,text=' W\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_w,t='w'),)
k_e= Button(keyboard_window,text=' E\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_e,t='e'),)
k_r= Button(keyboard_window,text=' R\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_r,t='r'),)
k_t= Button(keyboard_window,text=' T\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_t,t='t'),)
k_y= Button(keyboard_window,text=' Y\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_y,t='y'),)
k_u= Button(keyboard_window,text=' U\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_u,t='u'),)
k_i= Button(keyboard_window,text=' I\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_i,t='i'),)
k_o= Button(keyboard_window,text=' O\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_o,t='o'),)
k_p= Button(keyboard_window,text=' P\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_p,t='p'),)

k_open_bracket= Button(keyboard_window,text=' [\n{ ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_open_bracket,t='open_bracket'),)
k_close_bracket= Button(keyboard_window,text=' ]\n}  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_close_bracket,t='close_bracket'),)
k_backslash= Button(keyboard_window,text=' | \n |',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_backslash,t='backslash'),)
k_delete= Button(keyboard_window,text='del\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_delete,t='delete'),)
k_end= Button(keyboard_window,text='end\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_end,t='end'),)
k_pagedown= Button(keyboard_window,text='pgdwn\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_pagedown,t='pagedown'),)
k_num7= Button(keyboard_window,text=' 7\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num7,t='num7'),)
k_num8= Button(keyboard_window,text=' 8\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num8,t='num8'),)
k_num9= Button(keyboard_window,text=' 9\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num9,t='num9'),)
k_numplus= Button(keyboard_window,text=' +\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numplus,t='numplus'),)

row3_key_layout = [
    k_tab,k_q,k_w,k_e,k_r,k_t,k_y,
    k_u,k_i,k_o,k_p, k_open_bracket,k_close_bracket,k_backslash,k_blank1,k_delete,k_end,k_pagedown,
    k_blank1,k_blank1,k_blank1,k_num7,k_num8,k_num9,k_numplus,
]
for x in range(len(row3_key_layout)):
    for btn in row3_key_layout:
        row3_key_layout[x].grid(row=3,column=x, padx=3, pady=5,ipadx=10)

# build 3rd row of keyboard
k_cap= Button(keyboard_window, text=' CAP\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_cap,t='caps_lock'),)
k_cap.grid(columnspan=2, sticky=W, ipadx=8)
k_a= Button(keyboard_window,text=' A\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_a,t='a'),)
k_s= Button(keyboard_window,text=' S\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_s,t='s'),)
k_d= Button(keyboard_window,text=' D\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_d,t='d'),)
k_f= Button(keyboard_window,text=' F\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_f,t='f'),)
k_g= Button(keyboard_window,text=' G\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_g,t='g'),)
k_h= Button(keyboard_window,text=' H\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_h,t='h'),)
k_j= Button(keyboard_window,text=' J\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_j,t='j'),)
k_k= Button(keyboard_window,text=' K\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_k,t='k'),)
k_l= Button(keyboard_window,text=' L\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_l,t='l'),)
k_semicolon= Button(keyboard_window,text=' ;\n:',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_semicolon,t='semicolon'),)

k_quote= Button(keyboard_window,text=' "\n" ' ,bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_quote,t='quote'),)
k_enter= Button(keyboard_window,text='  ENTER  \n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_enter,t='enter'),)
k_enter.grid(columnspan=3, ipadx=80, sticky=SW)
k_num4= Button(keyboard_window,text=' 4\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num4,t='num4'),)
k_num5= Button(keyboard_window,text='5\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num5,t='num5'),)
k_num6= Button(keyboard_window,text='6\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num6,t='num6'),)
k_numplus= Button(keyboard_window,text='entr\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numplus,t='numplus'),)

row4_key_layout = [
    k_cap,k_a,k_s,k_d,k_f,k_g,k_h,
    k_j,k_k,k_l,k_semicolon, k_quote,k_enter,k_blank1,k_blank1,k_blank1,k_blank1,k_blank1, k_blank1,k_blank1,k_blank1,k_num4,
    k_num5,k_num6,#k_numplus,
]
for x in range(len(row4_key_layout)):
    for btn in row4_key_layout:
        row4_key_layout[x].grid(row=4,column=x, padx=3, pady=5, ipadx=8)


# build 3rd row of keyboard
k_shiftleft= Button(keyboard_window, text='SHIFT\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_shiftleft,t='shiftleft'),)
k_shiftleft.grid(columnspan=2, sticky=SE,padx=1  ) 
k_z= Button(keyboard_window,text=' Z\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_z,t='z'),)
k_x= Button(keyboard_window,text=' X\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_x,t='x'),)
k_c= Button(keyboard_window,text=' C\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_c,t='c'),)
k_v= Button(keyboard_window,text=' V\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_v,t='v'),)
k_b= Button(keyboard_window,text=' B\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_b,t='b'),)
k_n= Button(keyboard_window,text=' N\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_n,t='n'),)
k_m= Button(keyboard_window,text=' M\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_m,t='m'),)
k_comma= Button(keyboard_window,text=' ,\n<',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_comma,t='comma'),)
k_period= Button(keyboard_window,text=' .\n>',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_period,t='period'),)
k_backslash= Button(keyboard_window,text=' /\n?',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_backslash,t='slash'),)

k_shiftright= Button(keyboard_window,text=' SHIFT \n ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_shiftright,t='shiftright'),)
k_shiftright.grid(columnspan=2, sticky=SW, ipadx=80 )
k_arrow_top= Button(keyboard_window,text=' up\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_arrow_top,t='arrow_top'),)
k_num1= Button(keyboard_window,text=' 1 \n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num1,t='num1'),)
k_num2= Button(keyboard_window,text='2\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num2,t='num2'),)
k_num3= Button(keyboard_window,text='3\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num3,t='num3'),)
k_numenter= Button(keyboard_window,text='entr\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numenter,t='numenter'),)

row5_key_layout = [
    k_shiftleft,k_blank1,k_z,k_x,k_c,k_v,k_b,k_n,
    k_m,k_comma,k_period,k_backslash, k_shiftright,k_blank1,k_blank1,k_blank1,k_arrow_top,k_blank1,k_blank1, k_blank1,k_blank1,k_num1,
    k_num2,k_num3,k_numenter,
]
for x in range(len(row5_key_layout)):
    for btn in row5_key_layout:
        row5_key_layout[x].grid(row=5,column=x, padx=3, pady=5, ipadx=8 )

# build 3rd row of keyboard
k_ctrlleft= Button(keyboard_window, text=' ctrl\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_ctrlleft,t='ctrlleft'),)
k_win_left= Button(keyboard_window,text=' win\n  ', bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_win_left,t='win_left'),)
k_alt_left= Button(keyboard_window,text=' alt\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_alt_left,t='alt_left'),)
k_space= Button(keyboard_window,text=' space\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_space,t='space'),)
k_space.grid(columnspan=5, sticky=W, ipadx=130)
k_alt_right= Button(keyboard_window,text=' alt\n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_alt_right,t='alt_right'),)
k_win_right= Button(keyboard_window,text=' win\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_win_right,t='win_right'),)
k_menu= Button(keyboard_window,text=' [=] \n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_menu,t='menu'),)
k_ctrlright= Button(keyboard_window,text=' ctrl\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_ctrlright,t='ctrlright'),)
k_arrow_left= Button(keyboard_window,text=' left\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_arrow_left,t='arrow_left'),)
k_arrow_bottom= Button(keyboard_window,text=' down\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_arrow_bottom,t='arrow_bottom'),)
k_arrow_right= Button(keyboard_window,text=' right\n',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_arrow_right,t='arrow_right'),)

k_num0= Button(keyboard_window,text='  0  \n ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_num0,t='num0'),)
k_num0.grid(columnspan=3, padx=5, sticky=NW, ipadx=15)
k_numdot= Button(keyboard_window,text='  .  \n  ',bg=bg_color, fg=fg_keys, 
    command=lambda: key_click(b=k_numdot,t='num.'),)
# k_numenter= Button(keyboard_window,text=' enter \n  ',bg=bg_color, fg=fg_keys, 
#     command=lambda: key_click(b=k_numenter,t='numenter'),)
# k_enter.grid(columnspan=3, padx=5, sticky=N, ipadx=25)

row6_key_layout = [
    k_blank1,k_ctrlleft,k_win_left,k_alt_left,k_space,k_blank1,k_blank1,k_blank1,k_blank1,k_alt_right,k_win_right,k_menu,
    k_ctrlright,k_blank1,k_blank1,k_arrow_left,k_arrow_bottom,k_arrow_right,k_blank1,k_blank1,k_blank1,k_num0,
    k_numdot,#k_numenter,
]

for x in range(len(row6_key_layout)):
    
    for btn in row6_key_layout:
        row6_key_layout[x].grid(row=6,column=x, padx=5,pady=10 )



#### end of keyboard layouts
whole_damn_keyboard = [
    row0_key_layout,
    row1_key_layout,
    row2_key_layout,
    row3_key_layout,
    row4_key_layout,
    row5_key_layout,
    row6_key_layout,
    ]



#############################################################################################


def load_profile():
    global user_settings
    with open('g610/current_session_keyboard_lights.txt','r') as f:
        user_settings = f.read()
        f.close()
    print(user_settings)

    gb = Label(root, text='Got them', font='ariel 20 bold', bg='grey10', fg='snow')
    gb.grid(row=0, column=0, columnspan=4, rowspan=4)
    # sleep(2)
    # root.destroy()


def all_keys_off():
    sub.check_output(f'g610-led -a 00', shell=True)
    
def all_keys_on():
    sub.check_output('g610-led -a 99',shell=True)  

def set_to_profile():
    sub.check_output(f'{user_settings}', shell=True)
    print('done')

def all_blink():
    blink_rate = .081 #blink_rate_var.get() 
    try:
        for _ in range(10):

            sleep(blink_rate)
            all_keys_off()
            sleep(blink_rate)
            all_keys_on()
    except KeyboardInterrupt:
        root.destroy()


def random_blink():
    pass
    


def scroll_blink():
    blink_rate =.0915 #blink_rate_var.get() 
    scroll_rate = 0.025
    for key_row in whole_damn_keyboard:
        for key in key_row:
                
                try:
                    brightness.set('00')
                    key.invoke()
                    sleep(blink_rate)
                    brightness.set('99')
                    key.invoke()
                    sleep(scroll_rate)
                except AttributeError:
                    pass



preset_window = LabelFrame(root, fg='snow', bg='grey8', bd=0,)
preset_window.grid(row=0,column=2, rowspan=4)
all_on_key = Button(preset_window, text='All On ', fg='snow',bg=bg_color, bd=0, command=all_keys_on,)
all_on_key.grid(row=0, column=0,padx=5, ipadx=10,pady=5,sticky=W)
# all_on_key.deselect()
all_off_key = Button(preset_window, text='All Off ',fg='snow',bg=bg_color, bd=0, command=all_keys_off, )
all_off_key.grid(row=1, column=0,padx=5, ipadx=10,pady=5,sticky=W)
# all_off_key.deselect()
all_blink_key = Button(preset_window, text='All Blink ',fg='snow',bg=bg_color, bd=0, command=all_blink, )
all_blink_key.grid(row=2, column=0,padx=5, ipadx=10,pady=5,sticky=W)
def night(t):
    # print(night_scale.get())
    # print(night_var.get())
    if night_var.get() == 1:
        root.configure(bg='grey8')
        brightness_lbl.configure(bg='grey8', fg='snow')
        on_off_label.configure(bg='grey8', fg='snow')
        preset_window.configure(bg='grey8', fg='snow')
        keyboard_info_label.configure(bg='grey8', fg='snow')
        night_scale.configure(label='Day:', troughcolor='green3')
    if night_scale.get() == 0:
        root.configure(bg='grey70',)
        keyboard_info_label.configure(bg='grey70', fg='black')
        preset_window.configure(bg='grey70', fg='black')
        brightness_lbl.configure(bg='grey70', fg='black')
        on_off_label.configure(bg='grey70', fg='black')
        night_scale.configure(label='Night:', troughcolor='grey30')


night_var = IntVar()
night_scale = Scale(root, variable=night_var, from_=0, to_=1, bd=0, orient=HORIZONTAL,
        resolution=1, fg='snow', bg='black', showvalue=0, label='Day:', troughcolor='green3',
        command=night, highlightcolor='white', length=50)
night_scale.grid(row=0, column=3, pady=5,sticky=E, ipadx=5)
night_var.set(1)

scroll_blink_key = Button(preset_window, text='scroll Blink ',fg='snow',bg=bg_color, bd=0, command=scroll_blink, )
scroll_blink_key.grid(row=3, column=0,padx=5, ipadx=10,pady=5,sticky=W)

random_blink_key = Button(preset_window, text='random Blink ',fg='snow',bg=bg_color, bd=0, command=random_blink, )
random_blink_key.grid(row=4, column=0,padx=5, ipadx=10,pady=5,sticky=W)


reset_layout = Button(root, text='Set to Current', command=set_to_profile,bg='grey50', fg='black')
reset_layout.grid(row=5,column=2, ipadx=20, padx=10, pady=10)

load_layout = Button(root, text='Load', command=load_profile, bg='grey50', fg='black')
load_layout.grid(row=5,column=1, ipadx=20, padx=10, pady=10)

a_key = StringVar()
brightness = StringVar()


brightness_lbl = Label(root, text='Pick a key and brightness',bg='grey8',fg=fg_keys, font='ariel 14')
brightness_lbl.grid(row=0,column=0)

key_to_change = Entry(root, width=10,font='ariel 33', justify='center',bg='grey90' )
key_to_change.grid(row=1, column=0,padx=20, pady=10)
key_to_change.focus()

on_off_label = Label(root, text="Current Brightness:", fg=fg_keys, bg='grey8', font='ariel, 13')
on_off_label.grid(row=0, column=1, sticky=W)

on_off = Scale(root, from_=0,to_=99, resolution=3, orient=HORIZONTAL, variable=brightness, font='system 18', fg='red3',)
on_off.grid(row=1, column=1, padx=30, columnspan=2, sticky=SW)
on_off.set('00')

keyboard_info = sub.check_output('g610-led --print-device', shell=True)

keyboard_info_label = Label(root, text=keyboard_info, fg='white',bg='grey8', font='ariel 10')
keyboard_info_label.grid(row=1,column=3)

invalid = Label(root, text="INVALID ENTRY", fg='red', font='ariel 14')

change_button = Button(root, text='Change', bg='grey16', fg='green2', command=change)
change_button.grid(row=3, column=1, padx=20,ipadx=20, sticky=E)

quit_button = Button(root, text='Quit', bg='grey16', fg='red2', command=quitapp, font='ariel 12')
quit_button.grid(row=3, column=0, sticky=W, padx=10, pady=10, ipadx=20)


root.mainloop()
