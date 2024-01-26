from futbin import futbinPrice
import time

ASMonaco=[252802,263781,50579111,232440,244915,227055]
Clermont=[208861]
FCLorient=[228290,242577,213367,206003]
FCNantes=[233885,224019,199393]
HavreAC=[223058]
LosCLille=[239763,190674,193476,205600,251752,240507,246565,201119,213296]
Montpellier=[206306,200726,208615]
OGCNice=[50576540,224422,234686,235134,236477,255000,210896,158625,255533]
OL=[246646,225263,195086,251570,219683]
OM=[263829,251573,242835,255125,215330,241707,221087]
ParisSG=[257289,200888,226166,255253,243780,226271,50596300]
RCLens=[252059,221284,204883,201955,208787,226789,50555245]
stadebrestois29=[230020,200110]
Stadedereims=[239356,235432,242914,235633,258575,206493]
staderennaisfc=[256854,246350,257278,231102,253444,219792,50572401,163705]
Strasbourg=[206167,199641,227222,176600]
ToulouseFC=[235244,50559270,252021]

all=[ASMonaco,Clermont,FCLorient,FCNantes,HavreAC,LosCLille,Montpellier,OGCNice,OL,OM,ParisSG,
     RCLens,stadebrestois29,Stadedereims,staderennaisfc,Strasbourg,ToulouseFC]

def futbinPrice_fajianan():
    tmp = 0
    for i in all:
        tmp_tmp = 0

        for k in i:
            time.sleep(1)
            price = futbinPrice(k)
            if (price > 800):
                print("one is %d %d %d" % (tmp, k, price))
            tmp_tmp = tmp_tmp + price

        tmp_tmp = tmp_tmp / len(i)

        if (tmp_tmp > 800):
            print("all %d is ok %d" % (tmp, tmp_tmp))
        tmp = tmp + 1
if __name__ == '__main__':
    futbinPrice_fajianan()