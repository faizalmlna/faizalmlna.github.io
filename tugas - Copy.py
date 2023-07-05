#list dari sebuah data
tumpukan = [1,2,3,4,5]
#melihat list pada sebuah tumpukan
print("data saat ini = ", tumpukan )

#memasukkan sebuah data baru
tumpukan.append ('6')
tumpukan.append ('7')
tumpukan.append ('8')
print('\ndata masuk = ', 6,7,8)
print('data saat ini adalah = ', tumpukan)

#melakukan pop atau penghapusan pada tumpukan akhir
out = tumpukan.pop()
#melihat data yang keluar
print("\ndata keluar = ", out)
#hasil akhir setelah pop 
print ("data sekarang adalah = ", tumpukan)