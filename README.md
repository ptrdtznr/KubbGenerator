
# KubbGenerator

# Was ist Kubb?
"Kubb ist ein Geschicklichkeitsspiel, das meistens draußen gespielt wird. Es symbolisiert eine Schlacht, in der zwei verfeindete Gruppen für ihren König kämpfen. In der heutigen Form wird es seit circa 1990 gespielt und ist vor allem in Schweden und Norwegen beliebt, doch auch im deutschsprachigen Raum nicht mehr selten. Teilweise wird es dort unter dem Titel „Hägars Wikingerschach“, „Wikingerspiel“, „Bauernkegeln“, „Stöckchenspiel“, „Schwedenschach“ oder „Wikingerkegeln“ vermarktet oder gespielt." [Quelle](https://de.wikipedia.org/wiki/Kubb "Wikipedia Kubb")

## Simple Kubb Playoff Generator

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

