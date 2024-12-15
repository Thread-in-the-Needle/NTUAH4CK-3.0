from Crypto.Util.number import getPrime, isPrime
from secret import FLAG
from secrets import randbelow
from supercomputer import superfast_product_up_to_x_mod_n # you need to have a supercomputer to use this sorry :/
# superfast_product_up_to_x_mod_n(x, n) returns 0 if x % n == 0, otherwise it calculates the product prod([i for i in range(x + 1) if i % n != 0]) % n

randbound = 10**3
while True:
    p = getPrime(256)
    if isPrime((p-1)//2):
        break
rands_used = []
values = []
for i in range(len(FLAG)):
    value = 0
    for j in range(len(FLAG)):
        rand = randbelow(randbound)
        rands_used.append(rand)
        value += FLAG[j] * superfast_product_up_to_x_mod_n(p - randbound//2 + rand, p)
        value %= p
    values.append(value)

print(f"{p = }")
print(f"{rands_used = }")
print(f"{values = }")

'''
p = 77679947832191133523517888021553169001562422468712596390238771089056438084667
rands_used = [588, 900, 583, 583, 113, 566, 172, 393, 108, 239, 267, 518, 796, 570, 671, 331, 66, 655, 264, 439, 887, 189, 159, 547, 219, 785, 963, 771, 180, 720, 435, 67, 430, 112, 291, 271, 739, 198, 245, 329, 246, 188, 15, 572, 576, 416, 398, 976, 830, 615, 503, 715, 616, 923, 184, 443, 430, 72, 525, 92, 147, 933, 569, 837, 190, 372, 877, 626, 499, 174, 325, 392, 136, 460, 607, 615, 305, 71, 380, 478, 208, 144, 110, 496, 864, 992, 453, 911, 213, 578, 641, 403, 755, 800, 455, 342, 429, 368, 403, 47, 591, 854, 423, 590, 252, 144, 364, 935, 17, 312, 785, 104, 768, 169, 685, 802, 771, 167, 532, 880, 713, 297, 741, 382, 128, 302, 19, 804, 907, 25, 798, 775, 435, 592, 623, 2, 491, 240, 748, 938, 342, 857, 875, 961, 922, 667, 140, 428, 188, 382, 58, 640, 262, 848, 578, 364, 300, 680, 624, 334, 372, 453, 419, 843, 324, 486, 535, 411, 457, 121, 348, 974, 524, 17, 439, 350, 674, 191, 378, 365, 623, 932, 193, 514, 305, 203, 861, 899, 89, 682, 660, 513, 70, 60, 156, 82, 927, 513, 713, 360, 702, 331, 960, 293, 352, 150, 798, 190, 761, 571, 601, 860, 836, 390, 620, 412, 162, 942, 581, 254, 424, 131, 628, 830, 68, 93, 526, 216, 748, 797, 457, 366, 250, 930, 292, 533, 640, 590, 984, 379, 242, 483, 234, 641, 386, 743, 369, 971, 289, 817, 800, 243, 99, 502, 268, 109, 724, 5, 984, 582, 432, 486, 190, 685, 360, 872, 421, 828, 508, 340, 379, 220, 873, 980, 431, 57, 416, 223, 93, 150, 318, 261, 881, 798, 356, 918, 283, 129, 262, 840, 772, 654, 762, 392, 870, 100, 229, 778, 876, 194, 797, 893, 704, 631, 268, 212, 632, 377, 778, 655, 103, 609, 115, 434, 353, 784, 505, 215, 241, 970, 553, 137, 348, 686, 169, 289, 165, 548, 779, 59, 956, 45, 592, 47, 512, 537, 829, 70, 734, 731, 364, 4, 496, 788, 73, 409, 813, 26, 594, 389, 486, 209, 693, 280, 753, 205, 337, 954, 813, 474, 855, 817, 799, 577, 48, 719, 75, 953, 867, 438, 186, 571, 375, 386, 972, 980, 794, 576, 532, 674, 3, 324, 305, 305, 449, 860, 908, 296, 661, 404, 839, 309, 224, 275, 585, 646, 288, 84, 907, 261, 959, 42, 869, 407, 587, 988, 814, 696, 557, 2, 622, 343, 459, 462, 760, 161, 766, 877, 387, 410, 313, 640, 506, 142, 241, 887, 261, 43, 998, 180, 246, 351, 982, 355, 120, 316, 630, 751, 508, 912, 292, 210, 646, 936, 178, 72, 324, 480, 216, 124, 83, 708, 237, 399, 515, 907, 367, 385, 607, 212, 126, 490, 401, 871, 23, 298, 946, 358, 733, 24, 625, 335, 815, 897, 914, 635, 113, 368, 652, 300, 72, 886, 372, 73, 76, 6, 745, 303, 332, 884, 779, 458, 53, 672, 805, 327, 967, 109, 718, 732, 922, 869, 939, 848, 790, 39, 81, 565, 81, 923, 570, 247, 46, 530, 303, 286, 663, 163, 563, 899, 939, 575, 104, 171, 155, 526, 479, 942, 567, 220, 244, 241, 491, 972, 832, 491, 978, 399, 855, 468, 14, 654, 539, 180, 972, 539, 156, 964, 634, 636, 938, 844, 894, 848, 816, 637, 355, 482, 964, 593, 891, 184, 66, 57, 270, 437, 536, 986, 924, 606, 224, 79, 945, 680, 176, 171, 968, 852, 904, 670, 446, 865, 56, 243, 264, 282, 659, 441, 962, 812, 226, 433, 710, 237, 991, 852, 399, 770, 148, 683, 20, 659, 388, 664, 790, 407, 658, 499, 767, 614, 256, 490, 899, 552, 77, 294, 282, 939, 171, 339, 704, 347, 126, 633, 753, 247, 395, 198, 686, 617, 633, 149, 828, 976, 722, 355, 829, 471, 462, 461, 509, 357, 268, 526, 663, 232, 55, 652, 826, 829, 489, 531, 526, 857, 865, 370, 562, 903, 362, 427, 301, 570, 900, 812, 29, 824, 446, 5, 173, 535, 542, 949, 57, 923, 766, 737, 759, 864, 348, 393, 708, 14, 808, 688, 401, 362, 338, 16, 526, 463, 502, 541, 592, 75, 884, 935, 935, 422, 794, 126, 998, 237, 195, 564, 911, 600, 8, 26, 350, 874, 95, 223, 681, 997, 199, 118, 154, 347, 826, 448, 911, 336, 546, 808, 163, 421, 748, 633, 885, 694, 467, 324, 111, 233, 296, 436, 410, 153, 290, 335, 568, 294, 392, 834, 91, 532, 740, 882, 353, 427, 175, 398, 60, 388, 873, 819, 523, 700, 20, 546, 173, 740, 317, 851, 889, 968, 125, 604, 87, 474, 216, 52, 294, 54, 416, 594, 351, 877, 739, 605, 37, 965, 662, 354, 531, 331, 376, 58, 248, 371, 82, 824, 23, 753, 170, 490, 952, 925, 10, 622, 53, 204, 88, 448, 77, 504, 513, 155, 112, 818, 882, 926, 698, 616, 743, 939, 231, 622, 945, 63, 873, 493, 500, 535, 877, 640, 913, 198, 188, 979, 247, 44, 950, 973, 567, 867, 306, 339, 923, 220, 420, 821, 777, 586, 901, 78, 556, 778, 952, 815, 190, 256, 756, 913, 564, 325, 724, 5, 353, 794, 437, 38, 18, 338, 292, 663, 954, 982, 254, 619, 933, 363, 158, 955, 868, 777, 580, 398, 285, 626, 472, 38, 592, 715, 556, 918, 893, 148, 517, 575, 677, 711, 838, 135, 939, 705, 475, 917, 654, 415]
values = [18961269313481979991860053878854528531459157717464103987553753334333047531767, 3679957926714948656076112901744861957272651757981943696998658686635312582563, 3213525680577645314442108056895271273374691758540968541740489480341017746960, 49876276707558599625726086945261885360493810410581278262323426918565586943289, 12364739860507994135164249337855230093985318927798547739945440367837477144030, 50260651584284655536443864775829546115455934786038579728843430801186201384488, 68407503406509136427407092941793928074676260782196376769006676001805751639097, 21026155163768981217604928261986903157322654807669766538831853909813764394555, 68371881291390859067742000942534098406807369310059364826208072363886215174805, 48291763769139356940934909549316155103494024860922885818870233669938264412711, 41613460402677414012537049310474028131097510882436428491997008198805942141592, 16132423720366627445793267705972161821046179814463134220179068885338603488256, 22727639301178067097772101434914526102390785635489314789009153242548161398500, 63432644907808354624920079263205720256236862230359007388270401704315647141534, 59725823074421701127056833740978666663933290178821108672735630979772184382185, 49134097443374726457102109526248286779260519461657250149176335077513192815278, 47887622371924353518042148335513576469407974428663895529535598655562758641712, 77401278667543355790216213576126389056480395142842522512493624067576478647957, 42421818740357345269008297125039063498256069155482230332110328373475756354880, 50720612166765302920113352573577158255644183047862574403453539677091407427379, 63876103360121232899510143818245143640105668544885877370276591093988014501704, 61721909807203663925252684985485621255012442643078377644356014617601131395253, 21803540953486285882395548264941786702036878587769524591818364510951568905732, 66508904537561939583829063825411713457963153580568751858743952780040078537699, 73955364347203093461812330732441423658324476755793246807078992636213770612564, 16154121404109490850133554295816799812259115120653988436050967907122483933240, 30204108548337170867664410488680406651955856502320160369224126288557354450287, 44927574127697857269608503864341333742622132730576555086431003389323507206039, 52771399683417732796641179937781051074039930328470780435942535498621209477173, 56291951698406177798528654460283085130489679703644377707771892796738757306635]
'''