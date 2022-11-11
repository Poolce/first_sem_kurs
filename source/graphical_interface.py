import matplotlib.pyplot as plt
import numpy as np

def get_table(title,xNames,yNames,array):
    fig, ax = plt.subplots() 
    ax.set_axis_off() 

    table = ax.table( 
        cellText = array,    
        rowLabels = yNames,
        colLabels = xNames,
        cellLoc ='center',  
        loc ='upper left')         

    table.auto_set_font_size(False)
    table.set_fontsize(10)

    ax.set_title(title,fontweight ="bold") 

    plt.show() 




def get_gistogram(array, tittle):
    a_min = min(array)
    a_max = max(array)
    fig, histMp = plt.subplots()

    histMp.hist(array, bins=50, linewidth=0.5, edgecolor="white")

    histMp.set(xlim=(a_min, a_max), xticks=np.linspace(a_min, a_max, 9))
    histMp.set_title(tittle)
    plt.show()

def get_gistograms(array, tittles,col = 1):
    
    rows = int(len(array)/col) + (len(array) % col>0)
        
    fig, histMp = plt.subplots(rows,col)

    for i in range(rows):
        for j in range(col):
            histMp[i][j].hist(array[i*col+j], bins=50, linewidth=0.5, edgecolor="white")
            a_min = min(array[i*col+j])
            a_max = max(array[i*col+j])
            histMp[i][j].set(xlim=(a_min, a_max), xticks=np.linspace(a_min, a_max, 9))
            histMp[i][j].set_title(tittles[i*col+j])
    plt.show()


def get_correllation(array, arg_names):
    array_cor=np.round(np.corrcoef(array),2)
    
    fig, cor = plt.subplots()
    im = cor.imshow(array_cor)
    cbar = fig.colorbar(im)
    cor.set_xticks(np.arange(8), labels=arg_names)
    cor.set_yticks(np.arange(8), labels=arg_names)

    for i in range(8):
        for j in range(8):
            text = cor.text(j, i, array_cor[i, j],
                        ha="center", va="center", color="r")

    fig.tight_layout()
    plt.show()

def get_scatter(array_1,array_2):
    fig, scat = plt.subplots()
    # cor=np.corrcoef()
    colors = np.random.uniform(15, 80, len(array_1))
    scat.scatter(array_1,array_2,s=10,c='blue')
    scat.scatter(array_2,array_1,s=10,c='red')
    scat.set(xlim=(0, 8), xticks=np.arange(1, 8),
             ylim=(0, 8), yticks=np.arange(1, 8))
    
    plt.show