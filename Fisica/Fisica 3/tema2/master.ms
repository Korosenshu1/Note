.de LI
.IP \(bu 2
..
.EQ
delim $$
.EN

.TL
Confinamento della radiazione Cherenkov
.AU
Manuel Deodato
.AB
.LP
Determinare le condizioni sulla velocità $beta$ e l'indice di rifrazione $n$ affinché la radiazione Cherenkov emessa da una particella, che incide perpendicolarmente su una lastra di materiale trasparente con indice di rifrazione $n=1.5$, possa restare contenuta nel mezzo stesso. 
Scrivere un programma che calcoli la frazione di luce che resta confinata nel mezzo in funzione dell'angolo di incidenza, con velocità arbitraria.
.AE
.NH
Condizioni su $beta$ e $n$ per il confinamento.
.LP
Si sa che $cos theta sub c = 1 over {beta n( omega " ")}$, quindi:
.EQ
1 over {beta " "sup 2 n sup 2 ( omega " ")} = cos sup 2 theta sub c = 1 - sin sup 2 theta sub c -> sin theta sub c = left ( 1 - 1 over {beta " " sup 2 n sup 2 ( omega " ")} right ) sup 1/2", con " n( omega " " ) == 1.5
.EN
L'indice del mezzo radiatore è $n sub r = 1.5$; si cerca $n sub a$ indice di rifrazione dell'ambiente circostante il mezzo radiatore tale che la radiazione rimane confinata nel mezzo. 
Evidentemente, $n sub a == n sub a ( beta " " )$. 
.PP
Usando la legge di Snell per mettere in relazione il radiatore con il mezzo circostante, si ha: $n sub a sin theta sub a = 1.5 sin theta sub c$.
La richiesta è che la radiazione rimanga confinata, quindi si prende $theta sub a = pi / 2 -> sin theta sub a = 1$, quindi si trova la relazione
.EQ
n sub a ( beta " " ) = 1.5 cdot left ( 1 - 1 over {beta " " sup 2 n sup 2 ( omega " ")} right ) sup 1/2 = left ( 1.5 sup 2 - 1 over {beta " " sup  2} right ) sup 1/2
.EN
.NH
Frazione di luce confinata
.LP
La radiazione Cherenkov è omogenea rispetto all'angolo azimutale ed è emessa su un intero angolo solido, il cui differenziale è $d Omega  = 2 pi sin theta " " d theta$. Allora, la radiazione complessiva è emessa su tutto l'angolo solido, quindi
.EQ
Omega sub tot = int from 0 to theta sub c 2 pi sin theta " " d theta = 2 pi (1 - cos theta sub c )
.EN
mentre la parte di radiazione confinata nel mezzo è ottenuta tramite
.EQ
Omega sub conf = int from theta sub crit to theta sub c 2 pi sin theta " " d theta = 2 pi ( cos theta sub crit - cos theta sub c )
.EN
Si trova la frazione di radiazione confinata dal rapporto:
.EQ
f sub conf == Omega sub conf over Omega sub tot = { cos theta sub crit - cos theta sub c } over {1 - cos theta sub c }
.EN
In questa, si possono esplicitare i valori 
.EQ
cos theta sub c = 1 over { beta n } " ,  " cos theta sub crit = left ( 1- n sub rad over n sub a right ) sup 1/2
.EN
.EQ
-> f = {left ( 1- n sub rad / n sub a right ) sup 1/2 - 1 /  beta n } over { 1 - 1 /  beta n  } 
.EN

