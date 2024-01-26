from futbin import futbinPrice
import time

AthleticClub=[272131,241517,272138,272212,246286,272135,272123]
AtleticodeMa=[264725,272114,265021,272115,272110,256302,233757]
CATenerife=[233576,273547,272228,272235,246357]
FCBarcelona=[268942,242896]
GranadaCF=[275779]
LevanteLP=[272159,272163]
LevanteUD=[272020,272021,272012,272013,262459,271944,272004]
MadridCFF=[246359,272079,246364,272064,272061,272067]
RealMadridCF=[233155,259372,271945,227466,258576,264946,273153,267326,264865]
RealSociedad=[276796,272200,272202,261843,272211]
SevillaFC=[268993,272050,272047,272053,272056,261853,241182]
SportingHuelva=[272251,272246]
ValenciaCF=[272098,272089,272099,271943,272094,272065]
VillarrealCF=[227195,272150]


all=[AthleticClub,AtleticodeMa,CATenerife,FCBarcelona,GranadaCF,LevanteLP,LevanteUD,MadridCFF,
    RealMadridCF,RealSociedad,SevillaFC,SportingHuelva,ValenciaCF,VillarrealCF]

def futbinPrice_xijianv():
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
    futbinPrice_xijianv()