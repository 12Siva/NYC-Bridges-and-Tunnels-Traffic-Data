from collections import defaultdict
import matplotlib.pyplot as plt
from numpy import *
import re
import os

# collect: data acquired from nyc mta open data sets (http://web.mta.info/developers/data/bandt/trafficdata.html)
# prepare: the data is in xml format
# 2 dict objects one for cash and one for electronic payments-> key: toll number (1,2...,11) value: list of collections
def loadDataSet(directory):
    cashdict = defaultdict(list)
    elcdict = defaultdict(list)
    totaldict = defaultdict(list)
    for file in os.listdir(directory):
        inf = open(directory+"/"+file, 'r') # file is only 1 line
        # extract all cash values from the data file
        cashtuples = re.findall(r'id="(\d+)" cash-count="(\d+)" etc-count="(\d+)"', inf.read())
        for tuple in cashtuples:
            cashdict[tuple[0]].append(tuple[1])
            elcdict[tuple[0]].append(tuple[2])
            totaldict[tuple[0]].append(tuple[1] + tuple[2])

    return cashdict, elcdict, totaldict

# analyze: plot the values
def plotCount(inDataSet, weeksplit=False, cash=True):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    NUM_COLORS = 12
    cm = plt.get_cmap('Set2')
    ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
    tollNum = [] # plot label
    tolldict = {1: "Robert F. Kennedy Bridge Bronx Plaza",
    2: "Robert F. Kennedy Bridge Manhattan Plaza",
    3: "Bronx-Whitestone Bridge",
    4: "Henry Hudson Bridge",
    5: "Marine Parkway-Gil Hodges Memorial Bridge",
    6: "Cross Bay Veterans Memorial Bridge",
    7: "Queens Midtown Tunnel",
    8: "Brooklyn-Battery Tunnel",
    9: "Throgs Neck Bridge",
    11: "Verrazano-Narrows Bridge"}
    for key in inDataSet.iterkeys():
        tollNum.append(key)
        plt.plot(inDataSet[key], linewidth=2)

    # Shrink current axis's height by 20% on the bottom
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])

    legendlabels = [str(tolldict[int(num)]) for num in tollNum]

    # add plot legend
    plt.legend(legendlabels, bbox_to_anchor=(1.12, -0.06),
          fancybox=True, shadow=True, ncol=5, title='Toll Booth', prop={'size':11})

    # for x in range(0, len(inDataSet['1']), 7):
    #     # text annotations to show each new cycle
    #     ax.annotate('New Week', xy=(x, inDataSet['3'][x]), xytext=(x+1, int(inDataSet['3'][x]) + 1000),
    #             arrowprops=dict(facecolor='red', shrink=0.05),
    #             )

    # add vertical line to depict the separation of each week/cycle
    if weeksplit==True:
        for w in range(6, len(inDataSet['1']), 7):
            plt.axvline(x=w, linestyle="--", color='r')
#
    if cash == True:
        plt.ylabel("Number of Cars Through Cash Booths")
    else:
        plt.ylabel("Number of Cars Through Electronic Booths")
    plt.title("Traffic Count in NYC")
    plt.xlabel("Number of Days")
    plt.xticks(range(-1, len(inDataSet['1'])+1, 1))
    plt.grid(True)

def standRegres(xArr, yArr):
    # ordinary least square
    xMat = mat(xArr); yMat = mat(yArr).T
    print xMat
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse."
        return
    ws = xTx.I * (xMat.T*yMat) # (regression weights) w = (x^Tx)^-1 x^T y
    return ws

if __name__=='__main__':
    datafile = 'NYC_Daily_Toll_Count'
    cashvalues, elcvalues, totalvalues = loadDataSet(datafile)
    plotCount(cashvalues, weeksplit=True)
    plotCount(elcvalues, weeksplit=True, cash=False)
    plt.show()
