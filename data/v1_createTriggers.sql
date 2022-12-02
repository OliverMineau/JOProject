-- TODO 3.3 Créer un trigger pertinent
CREATE TRIGGER trigger_dateNais
BEFORE INSERT ON LesSportifsEQ
FOR EACH ROW
WHEN (new.dateNaisSp > DATE())
BEGIN
    SELECT RAISE (ABORT, "Date de naissance incorrecte");
END;
