-- TODO 1.3a : Créer les tables manquantes et modifier celles ci-dessous
CREATE TABLE LesSportifsEQ
(
  numSp NUMBER(4),
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  pays VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaisSp DATE,
  numEq NUMBER(4),
  CONSTRAINT SP_PK PRIMARY KEY (numSp),
  CONSTRAINT SP_FK FOREIGN KEY (numSp) REFERENCES LesInscriptions(numIn),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
  CONSTRAINT SP_CK3 CHECK(numEq > 0)
);

CREATE TABLE LesEpreuves
(
  numEp NUMBER(3),
  nomEp VARCHAR2(20),
  formeEp VARCHAR2(13),
  nomDi VARCHAR2(25),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (numEp > 0),
  CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0)
);

CREATE TABLE LesInscriptions
(
  numIn NUMBER(4),
  numEp NUMBER(3),
  CONSTRAINT IN_PK PRIMARY KEY (numEp,numIn),
  CONSTRAINT IN_FK FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp),
  CONSTRAINT IN_CK1 CHECK (numIn > 0),
  CONSTRAINT IN_CK2 CHECK (numEp > 0)
);

CREATE TABLE LesResultats
(
  numEp NUMBER(3),
  gold NUMBER(4),
  silver NUMBER(4),
  bronze NUMBER(4),
  CONSTRAINT RS_PK PRIMARY KEY (numEp),
  CONSTRAINT RS_FK FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp),
  CONSTRAINT RS_FK2 FOREIGN KEY (gold) REFERENCES LesInscriptions(numIn),
  CONSTRAINT RS_FK3 FOREIGN KEY (silver) REFERENCES LesInscriptions(numIn),
  CONSTRAINT RS_FK4 FOREIGN KEY (bronze) REFERENCES LesInscriptions(numIn),
  CONSTRAINT RS_CK1 CHECK (numEp > 0),
  CONSTRAINT RS_CK2 CHECK (gold > 0),
  CONSTRAINT RS_CK3 CHECK (silver > 0),
  CONSTRAINT RS_CK4 CHECK (bronze > 0)
)

-- TODO 1.4a : ajouter la définition de la vue LesAgesSportifs
-- TODO 1.5a : ajouter la définition de la vue LesNbsEquipiers
-- TODO 3.3 : ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)
