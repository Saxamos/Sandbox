import base64
from collections import defaultdict

import numpy as np

auth_token = "7GBOWH73QNL`qbtdk"

bytes_key = bytes(42)
b64_string = "bENES0ZGUwoLCn1PCkJLXE8KSUZFWU9OCl5CTwpOT0tGCl1DXkIKXkJPClhLSEhDXlkKCwp+Qk9TCl1DRkYKXUVYQQpdQ15CCl9ZCktETgpdTwpdQ0ZGCk9ETgpCX0dLRENeUwpLRE4KXktBTwpFXE9YCl5CTwpdRVhGTgoLCmdLQU8KWV9YTwpPXE9YU15CQ0RNCkNZClhPS05TCkxFWApeQk8KWkZLRAQKZV9YCkRPUl4KR09ZWUtNTwpdQ0ZGCl5PRkYKU0VfCl1CT0QKXU8KRktfRElCCl5CTwpLXl5LSUEECmhPClhPS05TBA=="
bytes_string = base64.b64decode(b64_string)


print(
    "".join(
        [
            (byte ^ 42).to_bytes(1, byteorder="big").decode("utf-8")
            for byte in bytes_string
        ]
    )
)

coded_msg = "E.4%  .1%  .9%  .1%  eim An75,i771,u385,y157,x0cnehag4%  .0%  .7%  .9%  .itsaal1,a709,l325,f297,k00pesvai%  .2%  .7%  .1%  .7hraeas,t718,h454,w216,v149ecg ah  .0%  .1%  .5%  .7%reeta o848,s454,g226,m139  p,oae .2%  .5%  .3%  .5%Ttt .r 878,n582,d256,p147,ohey.g1.0%  .7%  .5%  .3%  edo.h196,r612,c275,b157,qd  u !"

matrix = np.zeros((26, 12)).astype("str")

k = 0
for j in range(12):
    for i in range(26):
        try:
            matrix[i, j] = coded_msg[k]
            k += 1
        except IndexError:
            pass

print()
print("".join(matrix.flatten()))


coded_msg = "mngj neua wvcnqk ! ncm vo ltn fvjam vc tvvo ! cnustucs oustlnjk ! qvd gjn fnaa gfgjn ltgl fn tgen gc gsjnnbncl fult ltn bgm jghhulk. ltnq gsjnnm lv oustl gavcskumn dk uo ltnq igc tgen gaa vo ltn igjjvlk gcm snl ncvdst gauen tdbgck kagenk lv sjvf bvjn. ftuit uk oucn, ltnq igc tgen ltn igjjvlk kucin fn vcaq cnnm sjgkk gcm havvm. vdj ivbhucnm ovjink fult agdcit gc gaa vdl gllgiz uc g onf tvdjk ! snl jngmq ! hjgin qvdjknao, lvcustl ltn fvjam uk vdjk ! fn tgen kvbn ivcinjck jnsgjmucs ltn ghuaulq vo kvbn kcngzq tdbgc ncsucnnjk lv hjngz vdj wvfnjoda iuwtnjucs gasvjultbk. lv wjnencl gcq zucm vo hjngit, ojvb cvf vc, ltn bnltvm fn fuaa dkn lv wjvlnil vdj ivbbdcuigluvck fuaa hn hq oujkl, kwaullucs vdj mglg uc havizk vo kuplq ovdj hulk. ltnc lv iuwtnj ngit haviz, fn fuaa gwwaq gc npiadkuen vj vo vdj znq lv ltn wjneuvdk haviz gcm dkn ltn jnkdal vo ltuk vwnjgluvc lv iuwtnj ltn idjjncl haviz dkucs gcvltnj npiadkuen vj vwnjgluvc. gk dk, wvcnqk, gjn hngdluoda, bustlq gcm neua, ltn znq fuaa hn kupkupkup. mvc'l tnkulgln lv kgijuouin jghhulk mdjucs ltn vwnjgluvc, ltnkn ijngldjnk igc hjnnm kv xduizaq ltgl ltnq mvc'l nenc cnnm lv ivdcl ltnuj mngm. tvf ivcencuncl. fn zcvf ltgl gaa vo qvd fuaa hn ogclgklui uc hgllan. fn gjn avvzucs ovjfgjm lv gmbujn qvdj savjuvdk euilvjq ! svvm adiz wvcnqk ! svjn gaa vo ltnb ! mnglt lv ltn tdbgck ! mun ! fn fuaa cnenj nenj tgen lv fgaz gjvdcm gsguc fult umuvl qnaaucs aullan ojngzk kullucs vc vdj hgiz gcm hdssucs dk ! cnultnj lv gwwngj gk ujjulglucs ijngldjnk uc gccvqucs igjlvvck ! ul'k lubn ovj vdj jgsn gcm wvfnj lv klvjb ltn fvjam ! ongj ltn wvcnqk !"

toto = defaultdict(int)
for c in coded_msg:
    if c in [" ", "!", ".", "'", ","]:
        continue
    toto[c] += 1
print()
toto = {
    k: round(v / len(coded_msg) * 100, 3)
    for k, v in sorted(toto.items(), key=lambda item: item[1], reverse=True)
}

arr1 = [
    "e",
    "o",
    "t",
    "a",
    "i",
    "r",
    "n",
    "s",
    "h",
    "l",
    "u",
    "c",
    "d",
    "g",
    "w",
    "f",
    "y",
    "b",
    "p",
    "m",
    "v",
    "k",
    "x",
    "q",
]

mapper = {b: a for a, b in zip(arr1, toto)}

cypher = []
for c in coded_msg:
    try:
        cypher.append(mapper[c])
    except:
        cypher.append(c)
print()
print("".join(cypher))
