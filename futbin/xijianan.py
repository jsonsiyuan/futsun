from futbin import futbinPrice
import time

AthleticClub=[248550,171579,146947,231184,227950,191740,205157,216194]
AtleticodeMa=[251445,204639,177413,232119,252324,258390]
CAOsasuna=[188335,211022,224003,206590,193314,208137,238305,243976,225200]
CadizCF=[219391,239207,146439,205590,259173,229788,199247,229628]
DAlaves=[224415,226637,240953]
FCBarcelona=[199564,199576,192638]
GetafeCF=[223952,50570983,217940,234835,203843,240359,232665,239433,242201]
GironaFC=[186537,190815,50536718,50576685,234060,201505]
GranadaCF=[261204,50553689,251412,236679,183353,185020]
RayoVallecano=[173030,211348,189472,243558,243559,203581]
RCCelta=[240654,235997,50556733,201095,220673,240900,223061,50521338]
RCDMallorca=[228805,193171,263396,219585,208620,226777,223710,241727,198451]
RealBetis=[198141,171897,264698,195093,207566,210385,215699,203747,235945]
RealMadrid=[264309,206585,222509]
RealSociedad=[231627,233486,50565683,237681,226221,248148]
SevillaFC=[234426,231628,168651,231416,208330,208777,255106,202651,50571465,146536]
UDAlmeria=[50561628,245158,205976,219953,245598,271673,244316,205288,247500]
UDLasPalmas=[264388,243478,220253,217731,246657]
ValenciaCF=[247729,229010,246352,230578]
VillarrealCF=[205192,201143,259377,157481,237221,206545,205566,235781,216549,24630]


all=[AthleticClub,AtleticodeMa,CAOsasuna,CadizCF,DAlaves,FCBarcelona,GetafeCF,GironaFC,GranadaCF,RayoVallecano,
    RCCelta,RCDMallorca,RealBetis,RealMadrid,RealSociedad,SevillaFC,UDAlmeria,UDLasPalmas,ValenciaCF,VillarrealCF]

def futbinPrice_xijianan():
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
    futbinPrice_xijianan()