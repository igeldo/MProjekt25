Starten einer Postgres DB im Docker Container:

Zunächst Dockerimage laden:
![img.png](img.png)

docker pull postgres
im Terminal ausführen

Dann taucht das dockerimage im DockerDesktop auf

![img_1.png](img_1.png)

nun das image im container mittels run starten

![img_2.png](img_2.png)

Dabei optionale Settings Ports etc setzen:

![img_4.png](img_4.png)

Nun kann man das Python-Program starten und die Eingabe Maske erscheint

![img_5.png](img_5.png)

Nun kann man in Pycharm eine DataSource für Postgres einrichten und die Connection testen:

![img_8.png](img_8.png)

wichtig ist es unter dem "Reiter Schema" All schemas für die betreffende dB auszuwählen:

![img_9.png](img_9.png)

 Mit der rechten Maustaste auf der DB die query-Console auswählen:

![img_7.png](img_7.png)

Eingabe  SQL-Command
SELECT * from person;
oder
SELECT * from measurement;
Ausführen über das grüne Dreieck

![img_10.png](img_10.png)

Ergebnis:
![img_11.png](img_11.png)

oder 

![img_12.png](img_12.png)

