# KubbGenerator

Simple Kubb Playoff Generator

Wenn mehr Teams geweunscht oder mehr Spieler je Team, einfach die beiden Listen anpassen:

```python
  NUMBER_OF_TEAMS =  8
  NUMBER_OF_PLAYERS_PER_TEAM = 2
```  	
Die Spielernamen bzw. die Teamnamen koennen hier angepasst werden:

```python
  playerList 
  teamNames 
```  
Ausfuehrung:

```python
  python PlayoffTeamGenerator.py
```    
v 0.1
Dieser (Kubb-) Generator erstellt, abhaengig von der Anzahl der Spieler und der Anzahl der benoetigten Spieler je Team, zufaellig ausgewaehlte Teams. Existieren nicht genuegend Spieler, so wird die Liste mit "-"-Spielern aufgefuellt. Nachdem ein Spieler aus der Liste zufaellig gewaehlt wurde, wird die Spielerliste neu gemischt.
Nach Erstellung der Teams werden auch die ersten Spielbegegnungen zufaellig ausgewaehlt.

Fehler: sicherlich einige

