SELECT AVG(speed)
FROM pc;

SELECT AVG(screen),maker
FROM product
JOIN laptop 
ON product.model=laptop.model 
GROUP BY maker;

SELECT AVG(speed) 
FROM laptop 
WHERE price>1000;

SELECT AVG(price) 
FROM pc 
GROUP BY hd;


SELECT AVG(price) 
FROM pc 
GROUP BY speed 
HAVING speed>500;

SELECT AVG(price) 
FROM product 
LEFT OUTER JOIN pc 
ON product.model=pc.model 
GROUP BY maker 
HAVING maker='A';


SELECT AVG(price) 
FROM (SELECT price 
FROM product  
JOIN pc 
ON product.model=pc.model 
WHERE maker='B' 
UNION ALL 
SELECT price 
FROM product 
JOIN laptop 
ON product.model=laptop.model 
WHERE maker='B');


SELECT maker 
FROM product 
JOIN pc 
ON product.model=pc.model 
GROUP BY maker 
HAVING COUNT(pc.model)>3;


SELECT maker,COUNT(pc.model) 
FROM product 
JOIN pc 
ON product.model=pc.model 
GROUP BY maker;


SELECT maker,price 
FROM product 
JOIN pc 
ON product.model=pc.model 
WHERE price=(SELECT max(pc.price) 
FROM product 
JOIN pc 
ON product.model=pc.model 
GROUP BY maker);  



SELECT AVG(hd) 
FROM product 
JOIN pc 
ON product.model=pc.model 
WHERE maker IN(SELECT maker 
FROM product 
JOIN printer 
ON product.model=printer.model);                                                                                                                           
