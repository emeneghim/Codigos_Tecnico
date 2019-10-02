#Alunos: Eduardo Meneghim e Kamila Alexandre
#Turma: 301

DROP FUNCTION IF EXISTS fibo;
DELIMITER $$
CREATE FUNCTION fibo(n INT) RETURNS VARCHAR(255)
BEGIN	
	DECLARE numero_atual INT DEFAULT 1;
	DECLARE numero_anterior INT DEFAULT 1;
	DECLARE fim VARCHAR(255) DEFAULT '0,1';
	DECLARE var INT DEFAULT 1;
	DECLARE cont INT DEFAULT 0;
	
	REPEAT 
		SET cont = cont + 1;
		SET var = numero_atual;
		SET numero_atual = numero_atual + numero_anterior;
		SET numero_anterior = var;
		SET fim = concat(fim,',',numero_anterior);
	UNTIL (cont = n)
	END REPEAT;
	
RETURN fim;
END$$
DELIMITER ;
	
select fibo(30);