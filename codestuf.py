

# def function(num):
#     for i in range(num):
#         print(i)
# function(10)

# def convert(fairenheit):
#     celcius = (fairenheit-32)*(5/9)
#     print (celcius)
# convert(-32)

# def convert2(celcius):
#     fairenheit = celcius * (9/5) + 32
#     print (fairenheit)
# convert2(-28)

# def palindromechecker(word):
#     backword = ""
#     for i in range(len(word)-1, -1, -1):
#         backword += word[i]
#     if backword == word:
#         return True
#     else:
#         return False
# print (palindromechecker("tacocat"))
# def primechecker(num):
#     divisiblecount = 0
#     for i in range(1, num+1):
#         if num%i == 0:
#             divisiblecount += 1
#     print(divisiblecount)
#     if divisiblecount == 2:
#         return True
#     else:
#         return False
    
# print(primechecker(8))

# def uniqueifier(listonumbers):
#     list = []
#     for i_is in listonumbers:
#         if i_is not in list:
#             list.append(i_is)
#     return list
# print(uniqueifier([2,2,4,6,7,3,8,2,902,76,12,723,6,21,76,123,67,23]))

# def highestifier(primeronumero, segundonumero,tregundonemro):
#     if primeronumero > segundonumero:
#         if primeronumero >tregundonemro:
#             return primeronumero
#         else:
#             return tregundonemro
#     elif segundonumero > tregundonemro:
#         return segundonumero
#     else:
#         return tregundonemro
# print(highestifier(3,2,4))

# def highestinalistifier(listofnumbers):
#     highestnum = 0
#     for i in listofnumbers:
#         if i > highestnum:
#             highestnum = i
#     return highestnum

# print(highestinalistifier([1,2,3]))

# def counterdownerfrominputednumberifier(num):
#     if num == 0:
#         print(num)
#     else:
#         print(num)
#         counterdownerfrominputednumberifier(num-1)
# counterdownerfrominputednumberifier(10)

# def counterfrominputednumbertoanotherinputednumberifier(numerouno, numerodos):
#     if numerodos == numerouno:
#         print(numerodos)
#     else:
#         print(numerouno)
#         counterfrominputednumbertoanotherinputednumberifier(numerouno + 1, numerodos)
# counterfrominputednumbertoanotherinputednumberifier(1,9)

# def takeroftwonumbersandfindingthesumofthenumberswhenaddedtogetherifier(thefirstnumberusedinthisfunctiontoaddthingstogether, thesecondnumberusedinthisfunctiontoaddthingstogether):
#     if thefirstnumberusedinthisfunctiontoaddthingstogether == 9 and thesecondnumberusedinthisfunctiontoaddthingstogether == 10:
#         return 21
#     if thesecondnumberusedinthisfunctiontoaddthingstogether == 0:
#         return thefirstnumberusedinthisfunctiontoaddthingstogether
#     else:
#         return takeroftwonumbersandfindingthesumofthenumberswhenaddedtogetherifier(thefirstnumberusedinthisfunctiontoaddthingstogether+1, thesecondnumberusedinthisfunctiontoaddthingstogether-1)
# print(takeroftwonumbersandfindingthesumofthenumberswhenaddedtogetherifier(11,12))
# # def takeroftwonumbersandfindingtheexponentialpowerofthembcalculatingtheexponentofthetwovaluestogetherifier(thebasenumberusedtomakeanexponentialvaluebecausethatisthepurposeofthisfunction, thesecondnumberusedtomultiplyanothernumberbecausethatisthepurposeofthisfunction):
# #     if thesecondnumberusedtomultiplyanothernumberbecausethatisthepurposeofthisfunction == 0:
# #         return thebasenumberusedtomakeanexponentialvaluebecausethatisthepurposeofthisfunction
# #     else:
# #         return takeroftwonumbersandfindingtheexponentialpowerofthembcalculatingtheexponentofthetwovaluestogetherifier(thebasenumberusedtomakeanexponentialvaluebecausethatisthepurposeofthisfunction+thebasenumberusedtomakeanexponentialvaluebecausethatisthepurposeofthisfunction, thesecondnumberusedtomultiplyanothernumberbecausethatisthepurposeofthisfunction-1)
# # print(takeroftwonumbersandfindingtheexponentialpowerofthembcalculatingtheexponentofthetwovaluestogetherifier(34, 23))
# def mult(smol, tiny):
#     if tiny == 1:
#         return smol
#     else:
#         return mult(smol, tiny-1) + smol
# print(mult(1,996))

# def takeroftwonumbersandusingthefirstnumbertocreateabaseforeanexponentialequationandusingthesecondnumbertocreatetheexponentforanexponentialequationifier(x,y):
#     if y == 1:
#         return x
#     else:
#         return takeroftwonumbersandusingthefirstnumbertocreateabaseforeanexponentialequationandusingthesecondnumbertocreatetheexponentforanexponentialequationifier(x, y-1) * x
# print(takeroftwonumbersandusingthefirstnumbertocreateabaseforeanexponentialequationandusingthesecondnumbertocreatetheexponentforanexponentialequationifier(4,3))

# def takerofonenuberthenmultiplyingitbyallthewholenonnegativenumbersthatcamebeforeitthereforcreatingthefactorialofthatnumberifier(num):
#     if num == 0:
#         return 1
#     else:
#         return takerofonenuberthenmultiplyingitbyallthewholenonnegativenumbersthatcamebeforeitthereforcreatingthefactorialofthatnumberifier(num-1)*(num)
# print(takerofonenuberthenmultiplyingitbyallthewholenonnegativenumbersthatcamebeforeitthereforcreatingthefactorialofthatnumberifier(5))

# def fibeomoochisenquencesial(num):
#     if num == 1 or num ==2:
#         return 1
#     else:
#         return fibeomoochisenquencesial(num-1)+fibeomoochisenquencesial(num-2)
# print(fibeomoochisenquencesial(7))

# def takerofonelistandonevariableandlookingforthatvariableinthatlisttheeasybutslowerwayifier(list, var):
#     for i in range(len(list)):
#         if var == list[i]:
#             return i
#     return -1

# def binarysearcherthatusesrecursionithinkbecausethatiswhatmathewsaidifier(list, start, end, tagetpuppy):
#     if start > end:
#         return -1
#     mid1 = (start + end) / 2
#     mid = round(mid1)
#     if list[mid] == tagetpuppy:
#         return mid
#     if list[mid] < tagetpuppy:
#         return binarysearcherthatusesrecursionithinkbecausethatiswhatmathewsaidifier(list, mid + 1, end, tagetpuppy)
#     if list[mid] > tagetpuppy:
#         return binarysearcherthatusesrecursionithinkbecausethatiswhatmathewsaidifier(list, start, mid - 1, tagetpuppy)
# print(binarysearcherthatusesrecursionithinkbecausethatiswhatmathewsaidifier([1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 8 ,9, 90], 1, 15, 5))
# def kindaclosetothatone(list):
#     for i in range(len(list)):
#         index = i
#         while index > 0:
#             if list[index-1] > list[index]:
#                 temporayvcariablethatstoresoneoftheindexsitdoesntmatterwhichoneyoucanwritewhatitdoesiguessok = list[index - 1]
#                 list[index-1] = list[index]
#                 list[index] = temporayvcariablethatstoresoneoftheindexsitdoesntmatterwhichoneyoucanwritewhatitdoesiguessok
#                 index -= 1
#             else:
#                 index = 0
#     return list
# print(kindaclosetothatone([1,6,3,8,2,7,3,8,2,8,3,0,3,8,3,6,3]))

# def sowearebassicllyjustlookingattwoelementsandswapingthemifier(list):
#     for o in range(len(list)):
#         for i in range(len(list) - 1):
#             if list[i+1] < list[i]:
#                 temporayvariablethatstoresoneoftheindexsitdoesntmatterwhichoneyoucanwritewhatitdoesiguessok = list[i+1]
#                 list[i+1] = list[i]
#                 list[i] = temporayvariablethatstoresoneoftheindexsitdoesntmatterwhichoneyoucanwritewhatitdoesiguessok
#     return list
# print(sowearebassicllyjustlookingattwoelementsandswapingthemifier([1,6,3,8,2,7,3,8,2,8,3,0,3,8,3,6,3]))

# def mergesortbassicallytheideaisthatyouhaveanarrayofelementyoubreakitdownintosingleelemnetandmergethembacktogetherintoasortedlistifier(list,start,end):
#     if start == end:
#         return
#     mid = (start + end) // 2

#     mergesortbassicallytheideaisthatyouhaveanarrayofelementyoubreakitdownintosingleelemnetandmergethembacktogetherintoasortedlistifier(list, start, mid)
#     mergesortbassicallytheideaisthatyouhaveanarrayofelementyoubreakitdownintosingleelemnetandmergethembacktogetherintoasortedlistifier(list, mid + 1, end)
#     whatever(list, start, end)
# def whatever(list,start,end):
#     sortedstufs = []
#     mid = (start + end) // 2
#     stort = start
#     med = mid + 1
#     while stort < mid + 1 and med < end + 1:
#         if list[stort] < list[med]:
#             sortedstufs.append(list[stort])
#             stort += 1
#         else:
#             sortedstufs.append(list[med])
#             med += 1
#     while stort < mid + 1:
#         sortedstufs.append(list[stort])
#         stort += 1
#     while med < end + 1:
#         sortedstufs.append(list[med])
#         med += 1
#     for i in range(len(sortedstufs)):
#         list[i + start] = sortedstufs[i]
# listo = [1,6,3,8,2,7,3,8,2,8,3,0,3,8,3,6,3]
# mergesortbassicallytheideaisthatyouhaveanarrayofelementyoubreakitdownintosingleelemnetandmergethembacktogetherintoasortedlistifier(listo, 0, 16)
# print(listo)
#
def swap(list, index1, index2):
    indexy = list[index1]
    list[index1] = list[index2]
    list[index2] = indexy