 #BT 9
def party_late(arrivals,name):
    khach = arrivals.index(name) #tìm khách được chỉ định trong dsach
    khach_den_truoc = khach
    khach_den_tre = khach_den_truoc > len(arrivals)/2
    return khach_den_tre
arrivals = ['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
print(party_late(arrivals,name= 'Gilbert'))
print(party_late(arrivals,name= 'Fleda'))
print(party_late(arrivals,name= 'Mona'))