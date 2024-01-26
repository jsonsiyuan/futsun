from futbin import futbinPrice
import time

AFC=[260908,220714,237477,225539,236506]
Arsenal=[213051,240273,232938,236988,256958,227813]
AstonVilla=[207948,227174,216393,226162,212501,50552088,212419,207557,210881,189242]
Brentford=[210697,234824,243014,229723,235167,248484,238717,241508,224258]
Brighton=[199915,190765,186146,241585,138412,237942,218339,242418,258498]
Burnley=[228092,228151,198719,220659,242660]
Chelsea=[254796,242578,259197,239231,248695,229942,230918]
CrystalPalace=[247827,224221,241159,242619,50564954,235794,233866,213991,240947,236461,50559943]
Everton=[152908,202695,221479,211575,243282,211117,207599,208135,232080]
Fulham=[180403,205990,50545303,204838,236699,231633,220710,216266,203502,208450]
Liverpool=[242434,232223,246174]
Manchestercity=[224081,200159]
Manchesterutd=[237238,50576927,259399,233064,169588,268438,221363,50555806]
NewcastleUtd=[234742,220407,203487,206085,242964,198032]
NottmForest=[192123,186801,235642,273106,207863,225859,50572388]
SheffieldUtd=[193182,262929,234741]
Spurs=[246785,50583069,241042,246791,205923,235883,240091,247204,202335]
WestHam=[183855,220621,226229,190717,244749,244470,215798,164835,205569,236792,224371,210736,226456]
Wolves=[212811,226380,239901,240243,194806,212442,273463,227928,50569306,238616,201417]

all=[AFC,Arsenal,AstonVilla,Brentford,Brighton,Burnley,Chelsea,CrystalPalace,Everton,Fulham,Liverpool,Manchestercity,
     Manchesterutd,NewcastleUtd,NottmForest,SheffieldUtd,Spurs,WestHam,Wolves]

def futbinPrice_yingchaonan():
    tmp = 0
    for i in all:
        tmp_tmp = 0

        for k in i:
            time.sleep(1)
            price = futbinPrice(k)
            if (price > 800):
                print("one is %d %d %d" % (tmp,k,price))
            tmp_tmp = tmp_tmp + price

        tmp_tmp = tmp_tmp / len(i)

        if (tmp_tmp > 800):
            print("all %d is ok %d" % (tmp,tmp_tmp))
        tmp = tmp + 1
if __name__ == '__main__':
    futbinPrice_yingchaonan()