

## Algoritmusok bemutatása

### DFS
Miután felépítettük a gráfot, inicializálunk egy várólistát. Ez egy útvonalakból álló sor. A startot a sorba tesszük. Amíg van valami a sorban, addig vesszük az első elemet, kivesszük a sorból, és ellenőrizzük, hogy eléri-e a célt. Ha elértük 
G, kilépünk. Ellenkező esetben fogjuk a szomszédait, és hozzáadjuk őket a listához. A Depth-first algoritmus esetében pedig e sor hátuljához adjuk hozzá. Ezt addig folytatjuk, amíg meg nem találjuk a célt, vagy ki nem merítjük a várólistát.
### BFS
A Breadth-first algoritmus esetében minden elemet előre helyezünk, amíg meg nem találjuk a célt, vagy ki nem merítjük a várólistát.
### HC
Mindegyik csomópontot megvizsgálja és a heurisztikai távolságokat figyelembevéve terjeszti ki a csomópontokat.
### Beam
A Beam search az aktuálisan vizsgált csomópontok közül csak egy előre meghatározott számú legígéretesebbet tartja meg a további kiterjesztéshez.  
### Best-first
A Best-first search mindig a legígéretesebbnek tartott csomópontot vizsgálja tovább a heurisztikus érték alapján.  
### B&B
A Branch and Bound algoritmus a keresést részproblémákra bontja, és az alsó korlátok alapján vág el olyan ágakat, amelyek biztosan nem adnak jobb megoldást.  
#### Lista
A csomópontokat egy listában tárolja és ha mégegyszer előfordul a csomópont azt már nem vizsgálja az algoritmus.
#### Heurisztika
Vizsgálj a csomópontokhoz rendelt heuriszikai távolságot és ezeket vizsgálva halad végig a csomópontokon.
### A\*
Az A* algoritmus az B&B w. extended list és a B&B w. heuristic algoritmus együtteséből épül fel. Így azokat felhasználva kapjuk meg az A* algoritmushoz tartozó útvonalat.
## Futási eredmények
Graph 3 futási eredmények

| Algoritmus   | Útvonal | Futási idő (mp) | Kiterjesztések száma |
|:-------------|:--------|:---------------:|:--------------------:|
| DFS          | SZWG    |        0.0003s        |          -           |
| BFS          | SXWG    |        0.0002s        |          -           |
| HC           | SYWG    |        0.0002s        |          5           |
| Beam         | SYWG    |        0.0002s        |          4           |
| Best-first   | SYWG    |        0.0002s        |          5           |
| B&B          | SXWG    |        0.0002s        |          8           |
| B&B w. List  | SXWG    |        0.0004s        |          7           |
| B&B w. Heur. | SZWG    |        0.0005s        |          7           |
| A*           | SYWG    |        0.0005s        |          6           |

| Algoritmus   | Útvonal |        Futási idő (mp)         | Kiterjesztések száma |
|:-------------|:--------|:------------------------------:|:--------------------:|
| DFS          | SBCEG   |            0.0002s             |          3           |
| BFS          | SBCEG   |            0.0002s             |          7           |
| HC           | SBCEG   |            0.0002s             |          8           |
| Beam         | SBCEG   |            0.0001s             |          4           |
| Best-first   | SBCEG   |            0.0003s             |          8           |
| B&B          | SBCEG   |            0.0012s             |          19          |
| B&B w. List  | SBCEG   |            0.0010s             |          14          |
| B&B w. Heur. | SBCEG   |            0.0002s             |          10          |
| A*           | SBCEG   |            0.0008s             |          10          |
## Megoldás részletei

Megoldással töltött idő: kb. 10 óra \
Mi volt nehéz: Branch and Bound algoritmus. \
Mi volt érdekes: Pythonban való ismeretek bővítése. \
Mi volt unalmas: - \
Vélemény: Sokat kellett vele foglalkozni, hogy a megfelelő útvonalakat adják vissza az algoritmusok és a megfelelő sorrendben vizsgálja gráfokat.
# Search-algorithm
