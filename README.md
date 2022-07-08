## Job Card Planner
App ERPNext
bench get-app git@github.com:scopen-coop/jobcard_planning.git
bench install-app jobcard_planning
bench migrate

FR

Ajoute une vue calendrier des Cartes de travail permettant de les planifiées en glissé-déposé

Ajoute 4 champs sur les cartes de travail : Date de Début Prévue; Date de fin planifié, Employee Prévue, Nom Employee Prévue

Sur vue calendrier des Carte de travail, selectionner le Calendrier Job Card Planning

Les cartes de travail grises sont celles qui n'ont pas de date prévisionnelles.

Une fois plannifiés elles passent en bleue, au rechargement elles prennent la coleur de leurs statuts

EN
This Apps 

- Add Job Card Calendar view and allow the to plan them by drag and drop

- Add 4 fields on Job Card : Planned date start, Planned end Date, Planned Employee, Planned Employee Name

On calendar Job Card View, select de calendar Job Card Planning.

Gray cards are those without planned date. On planned the go in blue. On Reolad the get colors of their status

![image](https://user-images.githubusercontent.com/1050053/173192435-2a46ee70-080a-4175-8120-b3eaa870928e.png)


#### License

AGPL 3.0
