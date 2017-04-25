savefile=open("hash_part2.txt",'w');
savefile.write('{');

for i in range (6178315,11881378):
     savefile.write('"'+str(i)+'" : "t"')
     if (i!=11881377):
         savefile.write(',');
                         
                  

savefile.write('}');
                                
savefile.close()
