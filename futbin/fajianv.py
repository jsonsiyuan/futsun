from futbin import futbinPrice
import time

Bordeaux=[269959,265855]
DijonFCO=[265875,265879,265878]
EnAvant=[267661,267660,264885]
FCFleury91=[265833,268989,246568,264982,265947]
HavreAC=[227349,269208,270895,265865,269218]
LosCLille=[265952,264962]
Montpellier=[265850,265903,266947,264904,264807]
OL=[258706,227330,265092]
ParisFC=[264864,264963,265937]
ParisSG=[264967,264895,274644,274754,253469,264892,264905]
Stadede=[265893,265901]

all=[Bordeaux,DijonFCO,EnAvant,FCFleury91,HavreAC,LosCLille,Montpellier,OL,ParisFC,ParisSG,Stadede]

def futbinPrice_fajianan():
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
    futbinPrice_fajianan()