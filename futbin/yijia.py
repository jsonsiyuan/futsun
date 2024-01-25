from futbin import futbinPrice
import time

BergamoCal=[214092,266866,217196,252154,216150,207993,265188,220093,208165]
Bologna=[50574312,233556,231836,50533672,223671,189908]
Cagliari=[50547337,211302]
Empoli=[189053,235813,269312]
Fiorentina=[50555678,189125,246258,246431,220523,238095,230658,234612,235866,205812,234711]
Genoa=[231969,240938,241850,236295]
HellasVerona=[201046,230065,195272,255561,260697,215363]
Inter=[184392,228093,198176,228413,258648]
Juventus=[238744,236610,211320,266872,206058,268802,205175,198009]
Latium=[237712,219985,210864,211361,189505,255001,206098]
Lecce=[235949,201858,277839]
Milan=[256261,229758,178509,227796,203551,50564080,213666,216065]
Monza=[219812,235840,198946,202848,206654,239613]
NapoliFC=[202325,200752,241390,211515,240716,216816]
RomaFC=[213955,234906,262113,222558,212602,245426,233301,208268,224490,207439,208596,231352]
Salernitana=[236368,173221]
Sassuolo=[243593,163489,244253,50542265,205659,254487]
Torino=[243656,193352,253473,241095,258683]
Udinese=[222844,190745,223866,244238,244206]
Juventusnv=[47724,265859,256094,241844,227098,265861,266939]

all=[BergamoCal,Bologna,Cagliari,Empoli,Fiorentina,Genoa,HellasVerona,Inter
     ,Juventus,Latium,Lecce,Milan,Monza,NapoliFC,RomaFC,Salernitana,Sassuolo,Torino,Udinese,Juventusnv]

def futbinPrice_yijia():
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
    futbinPrice_yijia()