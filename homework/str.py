print('%10s' % ('nice')) 
print('{:>10}'.format('nice')) 

print("%-10s" % ('nice')) 
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice')) 
 
print('%.5s' % ('nice'))
print("%.5s" % ("pythonstudy"))
print("%5s" % ("pythonstudy")) 
print("{:10.5}".format("pythonstudy"))


# 出力
#       nice
#       nice
# nice      
# nice      
# ______nice
# $$$$$$nice
#    nice   
# nice
# pytho
# pythonstudy
# pytho     