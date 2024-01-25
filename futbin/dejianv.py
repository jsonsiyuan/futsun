from futbin import futbinPrice
import time

FCKoln=[264985,265025,265093]
FCBayern=[270525,233337,264901,264876,264899,264903]
Frankfurt=[264950,265054,264933,264975,257530]
Leverkusen=[264922,264930,264915,265118]
MSVDuisburg=[271862,271866,271837,271819,271867,271865]
RBLeipzig=[262089]
SCFreiburg=[265070,265079,271838,265080,265076,264992,227302,265060]
SGSEssen=[265039,265085,265047,272340]
SVWerderB=[265116,265119,265121]
TSGHoffenh=[227300,265020,265004,272337,265000,264999,264989,265058]
VfLWolfsburg=[253417,233839,265023,264058,244301,241847,265078]

all=[FCKoln,FCBayern,Frankfurt,Leverkusen,MSVDuisburg,RBLeipzig,SCFreiburg,SGSEssen,SVWerderB,TSGHoffenh,VfLWolfsburg]

def futbinPrice_dejianv():
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
    futbinPrice_dejianv()