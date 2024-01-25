from futbin import futbinPrice
import time


Arsenal=[245873,263013,244064,262866,265243,227003,265571]
AstonVilla=[265332,265326,50559045,245875,265311]
Brighton=[226355,246029,265217,267274,261835,50593442,227118,50564978,258915]
BristolCity=[265294]
Chelsea=[227282,263007,263009,246317,265247,262093,271568,243379,265250]
Everton=[227092,245443,263966,266551,261786,265335,227252]
LeicesterCity=[238096,227734,258704,261785,265281,245877]
Liverpool=[265301,266922]
Manchestercity=[264875,245830,226358,233150,253435,263964,265340,247796,248799]
Manchesterutd=[265350,50598860,50585744,265277,227397,50598199,265263]
Spurs=[235594,264896,265323,265264,265258,265254,266598,265265]
WestHam=[265300,227925,241549,271739,248728,245826,265297]


all=[Arsenal,AstonVilla,Brighton,BristolCity,Chelsea,Everton,LeicesterCity,Liverpool,Manchestercity,Manchesterutd,
     Spurs,WestHam]

def futbinPrice_yingchaonv():
    tmp = 0
    for i in all:
        tmp_tmp = 0
        print("now is %d" % (tmp))
        for k in i:
            time.sleep(1)
            tmp_tmp = tmp_tmp + futbinPrice(k)

        tmp_tmp = tmp_tmp / len(i)

        if (tmp_tmp > 800):
            print("%d is ok %d" % (tmp,tmp_tmp))
        tmp = tmp + 1
if __name__ == '__main__':
    futbinPrice_yingchaonv()