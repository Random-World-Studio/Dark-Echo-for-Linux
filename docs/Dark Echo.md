# Dark Echo

## map file format

Map file consists of apex structs.
The maps must ensure that all the apexes will enclose some closed figures.
the struct has members as follows:
1.identifer : int
2.coordinate : `\[float, float\]`
3.adjactApex : `\[int, int\]`  
    adjactApex[0] is the last apex' identifer, sdjact[1] is the next apex's identifer
4.arcEnable : `bool`  
    this enables items 5 6 and 7
5.center : `float`
6.radius : `float`
7.radian : 'float'

In map files, the first 8 bits is magic number 0x4f7102a7d5004c4f.  
After magic, there is apex-offset map(this map is the data structure with key-value pair);  
key is the identifer, value is the offet in map file of the apex;  
the table ends with two int(0).  

After the table, apex structs stores continuously.
