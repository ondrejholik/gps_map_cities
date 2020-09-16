from termcolor import colored
colors = ["grey",  "magenta", "blue", "green","cyan", "red",  "yellow", "yellow", "yellow", "white"]
def print_mapa():
    for x in mapa:
        for y in x:
            if(y == 0):
                print(colored("-","grey"), end="")
            else:
                pos = round(((y - min_pop) / (max_pop - min_pop))*9)
                print(colored(pos, colors[pos]), end="")
        print()


obc = open("obce.csv")
obce = obc.readlines()
gps_cor = []
height = 25
width = 90
mapa = []
tmp = []

for x in range(height):
    tmp = []
    for y in range(width):
        tmp.append(0)
    mapa.append(tmp)


#----min---lat-,lon-
min_cor = [1000,1000]
max_cor = [0,0]


for x in obce:
    lat = float(x.split(";")[1])
    lon = float(x.split(";")[2])
    if(min_cor[0] > lat):
        min_cor[0] = lat
    if(min_cor[1] > lon):
        min_cor[1] = lon
    if(max_cor[0] < lat):
        max_cor[0] = lat
    if(max_cor[1] < lon):
        max_cor[1] = lon

    gps_cor.append((lat,lon))

for x in gps_cor:
    lat = round(((1 - ((x[0] - min_cor[0]) / (max_cor[0] - min_cor[0]))) * height)-1)
    lon = round(((((x[1] - min_cor[1]) / (max_cor[1] - min_cor[1]))) * width )-1)
    mapa[lat][lon] += 1

max_pop = 0
min_pop = 100000000


for x in mapa:
    for y in x:
        if(y > max_pop):
            max_pop = y
        if(y < min_pop):
            min_pop = y


print_mapa()

