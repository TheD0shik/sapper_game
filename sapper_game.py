from tkinter import *
import random
import os
import sys
sys.setrecursionlimit(150000) 

n = 10
z=9
n=z*100
mini=10
btn = [[0 for _ in range(n)] for _ in range(n)] 
btncfg = [[0 for _ in range(n)] for _ in range(n)] 
btncfgz = [[0 for _ in range(n)] for _ in range(n)] 
win_main = 0



def game_over():
    for xx in range(z):
        for yy in range(z):
            if btncfg[xx][yy]==1:
                btn[xx][yy].configure(text="XX",bg="red") 
                btncfgz[xx][yy]=1
    los = Tk()
    los.geometry('400x400')
    los.title("sapper_game")
    btnchek = Button(los, text="НАЧАТЬ НОВУЮ ИГРУ", command=full_reset)
    btnchek.grid(column=z+1, row=z+2)
    btnchek = Button(los, text="перезапуск", command=reset)
    btnchek.grid(column=z+1, row=z+3)
    
    
    

def c_mini(minin):
    h=0
    global z
    while(h<minin):
        
        h=h+1
        mx=random.randint(0, z-1) 
        my=random.randint(0, z-1)  
        if  (btncfg[mx][my]==1):
            h=h-1
        btncfg[mx][my]=1
        
        
        


def st_chek(xxx1,yyy1):
    global z
    mini_in_cir_0=[0]*9
    fffff=0
    for q1 in (-1,0,1):
        for w1 in (-1,0,1):
            xxxx1=xxx1+q1
            yyyy1=yyy1+w1
            if (not(xxxx1>=z) and not(yyyy1>=z)):
                if (not(xxxx1<0) and not(yyyy1<0)):
                    if btncfgz[xxxx1][yyyy1]==0:
                        btncfgz[xxxx1][yyyy1]=1
                        button_click(xxxx1, yyyy1)
                    
    
    

#if (btncfg[xxxx][yyyy]==0 and btncfgz[xxxx][yyyy] ==0):
 #                       if (ccec(xxxx,yyyy)==0):
 #                           btncfgz[xxxx][yyyy]=-1
  #                          button_click(xxxx, yyyy)




def chek_circle(xxx,yyy):
    global z
    mini_in_cir=[0]*9
    fff=0
    for q in (-1,0,1):
        for w in (-1,0,1): 
            xxxx=xxx+q
            yyyy=yyy+w
            if (not(xxxx>=z) and not(yyyy>=z)):
                if (not(xxxx<0) and not(yyyy<0)):
                    mini_in_cir[fff]=btncfg[xxxx][yyyy]
                    fff=fff+1
                    
                
    return sum(mini_in_cir)
 
    
            
def chek():
    global z
    for xx in range(z):
        for yy in range(z):
            if btncfg[xx][yy]==1:
                btn[xx][yy].configure(text="XX",bg="red") 
                btncfgz[xx][yy]=1
            else:
                btncfgz[xx][yy]=1
                tth=chek_circle(xx,yy)
                
                btn[xx][yy].configure(text=f'0{tth}',bg="green",)  
                
                
                

def button_click(xx, yy):
    
    if btncfg[xx][yy]==1:
        game_over()
    elif btncfg[xx][yy]==0:
        
        tth=chek_circle(xx,yy)
        btn[xx][yy].configure(text=f'0{tth}',bg="green")
        btn[xx][yy].grid(column=xx, row=yy)
        if tth==0:
            st_chek(xx,yy)
            
        
win =0 



def d_game():
    
    global win,z,mini
    try:
        if win_main.winfo_exists():
            
            z= int(txt.get())
            mini= int(mIn.get())
            win_main.destroy()
    except TclError:
        pass
    
    
    print(f'поле-{z}_мины-{mini}')
    win = Tk()
    win.geometry('400x400')
    win.title("sapper_game")
    
    c_mini(mini)
    for x in range(z):
        for y in range(z):
            btn[x][y] = Button(win, text="XX", command=lambda xx=x, yy=y: button_click(xx, yy),bg="black")
            btn[x][y].grid(column=x, row=y)
    btnchek = Button(win, text="открыть все", command=chek)
    btnchek.grid(column=z+1, row=z+1)
    btnchek = Button(win, text="НАЧАТЬ НОВУЮ ИГРУ", command=full_reset)
    btnchek.grid(column=z+1, row=z+2)
    btnchek = Button(win, text="перезапуск", command=reset)
    btnchek.grid(column=z+1, row=z+3)
    
    win.mainloop()

def d_menu():
    global win_main ,txt,z,mIn
    win_main = Tk()
    win_main.geometry('400x400')
    win_main.title("sapper_game")
    lbl = Label(win_main, text="сапер", font=("Arial Bold", 50))  
    lbl.grid(column=0, row=0) 
    txt = Entry(win_main, width=10)
    txt.grid(column=1, row=5)
    lbl = Label(win_main, text="размер поля:", font=("Arial Bold", 16))  
    lbl.grid(column=0, row=5) 
    mIn = Entry(win_main, width=10)
    mIn.grid(column=1, row=6)
    lbl = Label(win_main, text="кол_во мин:", font=("Arial Bold", 16))  
    lbl.grid(column=0, row=6) 
    bt = Button(win_main, text="запустить игру", command=d_game)
    bt.grid(column=0, row=7)
    win_main.mainloop()

def reset():
    win.destroy()
    ress()
    d_game()
    
def ress():
    global btn,btncfg,btncfgz
    btn = [[0 for _ in range(n)] for _ in range(n)] 
    btncfg = [[0 for _ in range(n)] for _ in range(n)] 
    btncfgz = [[0 for _ in range(n)] for _ in range(n)] 
 
def full_reset():
    win.destroy()
    
    ress()
    main()
    
def main():
    
    ress()
    d_menu()
    
    #d_game()


if __name__ == "__main__":
    main()