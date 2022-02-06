# Blocks_Problem_Reinterpreted_KR
 Based on a KR Uni Project I had to implement a reinterpreted version of Blocks Problem

# Reinterpretation of the problem.

Avem un set de stive de blocuri. Se considera ca fiecare bloc estes fie bloc fie de tip soarece fie de tip pisica flămândă, fie pisica sătulă, și are un identificator unic (număr). În starea initiala toate pisicile trebuie sa fie pisici flamande.

Exemplu de stare initiala:

![alt text](https://github.com/CristianUlmeanu/Blocks_Problem_Reinterpreted_KR/blob/local/RequirmentsPics/pb-blocuri-soareci-si-pisici(initiala).png?raw=true)

configuratie initiala
Mutarea blocurilor se face cu urmatoarele restrictii si efecte:

daca mutam un bloc pisica-flămândă peste un bloc soarece, blocul pisica inghite toate blocurile soarece pe stiva in jos, pana ajunge la un bloc pisica. Dacă un bloc pisica-flămândă era de dinainte (din starea inițială) peste blocuri-șoarece, pisica nu le face nimic (atacă doar la mutare).
o pisică sătulă nu mai manâncă șoareci. O pisică devine sătulă după ce a mancat minim un șoarece.
nu putem muta un bloc pisica peste alt bloc pisica, decat daca una dintre pisici este satula (altfel se iau la bataie)
blocurile soareci pot fi plasate fara restrictii
Exemplu de stare după o mutare:

![alt text](https://github.com/CristianUlmeanu/Blocks_Problem_Reinterpreted_KR/blob/local/RequirmentsPics/pb-blocuri-soareci-si-pisici(dupa%20o%20mutare).png?raw=true)

configuratie initiala
Costul mutării unui bloc este 3 pentru pisica satula, 2 pentru pisica flamanda si 1 pentru soareci.

Scopul este sa nu mai avem pisici flamande in configuratie (toate pisicile sa ajunga satule).

Observatie. Starea initiala poate contine blocurile in orice configuratie (conditiile de disparitie sau imposibilitate de plasare a blocurilor se aplica doar in urma unei mutari; de exemplu in starea initiala putem avea bloc pisica plasat peste bloc soarece, si pisica nu va manca soarecii; o pisica manaca soarecii de sub ea doar daca ajunge acolo in urma unei mutari).

Model fișier input. O stare în fișierul de input se va reprezenta astfel:

fiecare stivă pe câte un rând. Se consideră că baza stivei e la stânga și vârful stivei e la dreapta.
blocurile de pe o stivă se vor separa cu simbolul "#"
informația dintr-un bloc va avea forma: identificator:tip, unde tip poate avea valorile: pf (pisică flămândă), s (șoarece), ps (pisică sătulă).
Stivele vide se evidențiază prin simbolul "=".
De exemplu, pentru starea inițială dată ca exemplu:

![alt text](https://github.com/CristianUlmeanu/Blocks_Problem_Reinterpreted_KR/blob/local/RequirmentsPics/pb-blocuri-soareci-si-pisici(initiala)%20(1).png?raw=true)

fișierul de intrare ar fi:<br />
1:s#4:pf<br />
5:s#2:s#3:pf<br />
9:ps#7:s#6:s<br />
10:s#8:s<br />
12:pf#13:s#11:ps<br />
Model fișier output. O stare în fișierul de output se va reprezenta afișând stivele de sus în jos, toate aliniate la bază. Afișarea unei configurații va avea un număr de rânduri egal cu înălțimea celei mai înalte stive. Dacă o stivă nu ajunge pănă la un anumit nivel în locul în care trebuia afișat blocul ei se vor pune spații (deci, dacă e cazul într-o stare finală, pentru stivă vidă vom avea spațiu începând cu cel mai de jos nivel). Un bloc pe stivă se va afișa în formatul [tip:numar] . Între două stive se va afișa o coloană de spații. Toate blocurile dintr-o stivă încep de la aceeași coloană în zona de afișare. Sub fiecare configurație se va afișa o linie de simboluri "#"(hashtag) care începe de sub prima stivă și se termină la ultima.

în afișarea drumului, configurațiile (nodurile) apar în ordine cronologică, numerotate (cu indice între 1 si ND, unde ND e numărul de noduri din drum). Se afișează pe o linie separată indicele și dedesubt configurația corespunzătoare.

Între două soluții se va afișa un separator, de exemplu "--------------------------------------".

De exemplu, pentru configurația de mai jos (care e starea inițială corespunzătoare fișierului de intrare dat caexemplu; de acolo s-au luat si identificatorii), dacă ar fi un nod în fișierul de output:

![alt text](https://github.com/CristianUlmeanu/Blocks_Problem_Reinterpreted_KR/blob/local/RequirmentsPics/pb-blocuri-soareci-si-pisici(finala).png?raw=true)

configuratie
presupunând ca e primul nod într-un drum, am avea:
1)<br />
<br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  [pf: 3] [&nbsp; s: 6]&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [ps:11]<br />
[pf: 4] [&nbsp; s: 2] [&nbsp; s: 7] [ s:&nbsp; 8] [&nbsp; s:13]<br />
[&nbsp; s: 1] [&nbsp; s: 5] [ps: 9] [ s:10] [pf:12]<br />
#######################################<br />
Pentru o aliniere ușoară, puteți considera că identificatorul nu are mai mult de 2 caractere (nu se vor da mai mult de 100 de blocuri într-o configurație).

Atenție, aici e exemplu pentru un singur nod; voi trebuie să afisați toate nodurile din drumul soluție în acest format.

# Requirments

 1. Fișierele de input vor fi într-un folder a cărui cale va fi dată în linia de comanda. În linia de comandă se va da și calea pentru un folder de output în care programul va crea pentru fiecare fișier de input, fișierul sau fișierele cu rezultatele. Tot în linia de comandă se va da ca parametru și numărul de soluții de calculat (de exemplu, vrem primele NSOL=4 soluții returnate de fiecare algoritm). Ultimul parametru va fi timpul de timeout. Se va descrie în documentație forma în care se apelează programul, plus 1-2 exemple de apel.
 2. Citirea din fisier + memorarea starii. Parsarea fișierului de input care respectă formatul cerut în enunț
 3. Functia de generare a succesorilor
 4. Calcularea costului pentru o mutare
 5. Testarea ajungerii în starea scop (indicat ar fi printr-o funcție de testare a scopului)
 6. 4 euristici:
    -Banala
    -Doua euristici admisibile posibile (se va justifica la prezentare si in documentație de ce sunt admisibile)
    -O euristică neadmisibilă (se va da un exemplu prin care se demonstrează că nu e admisibilă). Atenție, euristica neadmisibilă trebuie să depindă de stare (să se calculeze  în  funcție de valori care descriu starea pentru care e calculată euristica).
 7. Crearea a 4 fisiere de input cu urmatoarele proprietati:
    -Un fisier de input care nu are solutii
    -Un fisier de input care da o stare initiala care este si finala (daca acest lucru nu e realizabil pentru problema, aleasa, veti mentiona acest lucru, explicand si motivul).
    -Un fisier de input care nu blochează pe niciun algoritm și să aibă ca soluții drumuri lungime micuță (ca să fie ușor de urmărit), să zicem de lungime maxim 20.
un fisier de input care să blocheze un algoritm la timeout, dar minim un alt algoritm să dea soluție (de exemplu se blochează DF-ul dacă soluțiile sunt cât mai "în dreapta" în arborele de parcurgere)
    -Dintre ultimele doua fisiere, cel putin un fisier sa dea drumul de cost minim pentru euristicile admisibile si un drum care nu e de cost minim pentru cea euristica neadmisibila
 8. Pentru cele NSOL drumuri(soluții) returnate de fiecare algoritm (unde NSOL e numarul de soluții dat în linia de comandă) se va afișa:
numărul de ordine al fiecărui nod din drum
    -Lungimea drumului
    -Costului drumului
    -Timpul de găsire a unei soluții (atenție, pentru soluțiile de la a doua încolo timpul se consideră tot de la începutul execuției algoritmului și nu de la ultima soluție)
    -Numărul maxim de noduri existente la un moment dat în memorie
    -Numărul total de noduri calculate (totalul de succesori generati; atenție la DFI și IDA* se adună pentru fiecare iteratie chiar dacă se repetă generarea arborelui, nodurile se vor contoriza de fiecare dată afișându-se totalul pe toate iterațiile
    -Intre două soluții de va scrie un separator, sau soluțiile se vor scrie în fișiere diferite.
Obținerea soluțiilor se va face cu ajutorul fiecăruia dintre algoritmii studiați:

Pentru studenții de la seria CTI problema se va rula cu algoritmii: BF, DF, DFI, UCS, Greedy, A*.
Pentru studenții din seriile Mate-Info și Informatică, problema se va rula cu algoritmii: UCS, A* (varianta care dă toate drumurile), A* optimizat (cu listele open și closed, care dă doar drumul de cost minim), IDA*.
Pentru toate variantele de A* (cel care oferă toate drumurile, cel optimizat pentru o singură soluție, și IDA*) se va rezolva problema cu fiecare dintre euristici. Fiecare din algoritmi va fi rulat cu timeout, si se va opri daca depășește acel timeout (necesar în special pentru fișierul fără soluții unde ajunge să facă tot arborele, sau pentru DF în cazul soluțiilor aflate foarte în dreapta în arborele de parcurgere).
 
9. Afisarea in fisierele de output in formatul cerut
 10. Validări și optimizari. Veți implementa elementele de mai jos care se potrivesc cu varianta de temă alocată vouă:
găsirea unui mod de reprezentare a stării, cât mai eficient
verificarea corectitudinii datelor de intrare
găsirea unor conditii din care sa reiasă că o stare nu are cum sa contina in subarborele de succesori o stare finala deci nu mai merita expandata (nu are cum să se ajungă prin starea respectivă la o stare scop)
găsirea unui mod de a realiza din starea initială că problema nu are soluții. Validările și optimizările se vor descrie pe scurt în documentație.
 11. Comentarii pentru clasele și funcțiile adăugate de voi în program (dacă folosiți scheletul de cod dat la laborator, nu e nevoie sa comentați și clasele existente). Comentariile pentru funcții trebuie să respecte un stil consacrat prin care se precizează tipul și rolurile parametrilor, căt și valoarea returnată (de exemplu, reStructured text sau Google python docstrings).

## Bonuses
Doar pentru studenții de la seria CTI: se dă bonus 10% pentru implementarea Greedy și analizarea acestuia împreună cu ceilalți algoritmi.
Doar pentru studenții de la seria CTI: se dă bonus câte 10% pentru fiecare dintre următoarele optimizări pentru cazul în care se cere o singură soluție (deci în program veți avea un if care verifică dacă numărul inițial de soluții cerut era 1):
la BF să se returneze drumul imediat ce nodul scop a fost descoperit, și nu neapărat când ajunge primul în coadă
la UCS+A* (bonusul ar fi 10%+10% dacă se face pt ambele) să nu avem duplicate ale informației din noduri în coadă. În cazul în care tocmai dorim să adăugăm un nod în coadă și vedem că există informația lui deja, păstram în coadă, dintre cele 2 noduri doar pe cel cu costul cel mai mic

