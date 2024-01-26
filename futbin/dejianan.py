from futbin import futbinPrice
import time

FCKoln=[195038,224041,240916,200318,239340]
FSVMainz=[216158,229071,198118,236636,245253,219733,228518,221671,238068]
BorussiaDor=[50537079,240833,229891,245541,202371]
FCAugsburg=[232144,238900,251182,237629,202201,231227]
FCBayernM=[183569,209889]
Frankfurt=[234573,248573,256675,225126,212187,236532,215353,200215,257889]
Heidenheim=[214096]
Leverkusen=[225309,246618,255223,250955,50586871,213331,199503]
Mgladbach=[222493,222028,246919,221491,231838,223550,223724,220876,204024,234943]
RBLeipzig=[260592,195365,238463,207791,257876,204092,228579,208448,242187]
SCFreiburg=[231366,199897,226168,232639,209846,208335,244112,234171,199439]
SVDarmstad=[209987]
SVWerderB=[50552531,197031,206591,220971,236583]
TSGHoffenh=[50568969,204082,203605,253170,228336,244390,239890,235526,235424,223689]
UnionBerlin=[247028,232658,233642,193254,227234,234575,201269,200610,223697]
VfBStuttgart=[215441,223885,244176,229476]
VfLBochum=[204497,199288,216283,206606,199339]
VfLWolfsburg=[242663,234678,216860,212245,244261,230084,252495,228946]

all=[FCKoln,FSVMainz,BorussiaDor,FCAugsburg,FCBayernM,Frankfurt,Heidenheim,Leverkusen,
     Mgladbach,RBLeipzig,SCFreiburg,SVDarmstad,SVWerderB,TSGHoffenh,UnionBerlin,VfBStuttgart,VfLBochum,VfLWolfsburg]

def futbinPrice_dejianan():
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
    futbinPrice_dejianan()