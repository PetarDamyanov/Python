 SELECT `SHIPS`.`NAME`,`CLASSES`.`COUNTRY`,`CLASSES`.`NUMGUNS`,`SHIPS`.`LAUNCHED` 
 FROM `SHIPS` 
 JOIN `CLASSES` 
 ON `SHIPS`.`CLASS`= `CLASSES`.`CLASS`;


SELECT `SHIPS`.`NAME`,`CLASSES`.`COUNTRY`,`CLASSES`.`NUMGUNS`,`SHIPS`.`LAUNCHED` 
FROM `CLASSES` 
LEFT OUTER JOIN `SHIPS` 
ON `SHIPS`.`CLASS`= `CLASSES`.`CLASS` 
WHERE `SHIPS`.`NAME` ISNULL
UNION
SELECT `SHIPS`.`NAME`,`CLASSES`.`COUNTRY`,`CLASSES`.`NUMGUNS`,`SHIPS`.`LAUNCHED` 
FROM `SHIPS` 
JOIN `CLASSES` 
ON `SHIPS`.`CLASS`= `CLASSES`.`CLASS`;




SELECT `SHIPS`.`NAME` 
FROM `SHIPS` 
WHERE `NAME` NOT IN (SELECT `SHIPS`.`NAME` 
FROM `OUTCOMES` 
JOIN `SHIPS` 
ON `OUTCOMES`.`SHIP`=`SHIPS`.`NAME`);




SELECT `SHIPS`.`NAME` 
FROM `OUTCOMES` 
JOIN `SHIPS` 
ON `OUTCOMES`.`SHIP`= `SHIPS`.`NAME` 
JOIN `BATTLES` 
ON `OUTCOMES`.`BATTLE`= `BATTLES`.`NAME` 
WHERE `BATTLES`.`DATE` LIKE( '1942%');  