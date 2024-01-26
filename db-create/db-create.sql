

CREATE TABLE product(
product_id int NOT NULL,
name varchar(50) NOT NULL,
calories numeric(15,2) NOT NULL, 
squirrels numeric(15,2) NOT NULL,
fats numeric(15,2) NOT NULL,
carbohydrates numeric(15,2) NOT NULL,
CONSTRAINT productPK
PRIMARY KEY (product_id));

CREATE TABLE users(
user_id bigint NOT NULL,
username varchar(50) NOT NULL,
CONSTRAINT userPK
PRIMARY KEY (user_id));

CREATE TABLE meals(
meals_id int NOT NULL,
creator_id int NOT NULL,
name_meals varchar(50) NOT NULL,
number_of_calories numeric(15, 2) NULL,
number_of_squirrels numeric(15, 2) NULL,
number_of_fats numeric(15, 2) NULL,
number_of_carbohydrates numeric(15, 2) NULL,
CONSTRAINT mealsPK
PRIMARY KEY (meals_id));

CREATE TABLE product_meals(
product_id int NOT NULL,
meals_id int NOT NULL,
quantity int NOT NULL,
CONSTRAINT product_mealsPK
PRIMARY KEY (product_id, meals_id),
CONSTRAINT product_meals_productFK
FOREIGN KEY (product_id)
REFERENCES product (product_id)
ON DELETE CASCADE,
CONSTRAINT product_meals_mealsFK
FOREIGN KEY (meals_id)
REFERENCES meals (meals_id)
ON DELETE CASCADE);

CREATE TABLE journal(
log_id int NOT NULL,
user_id bigint NOT NULL,
meals_id int NOT NULL,
CONSTRAINT journalPK
PRIMARY KEY (log_id),
CONSTRAINT journaluserFK
FOREIGN KEY (user_id)
REFERENCES users (user_id),
CONSTRAINT journalmealsFK
FOREIGN KEY (meals_id)
REFERENCES meals (meals_id));

CREATE SEQUENCE SEQ_product
INCREMENT BY 1
START WITH 1
MINVALUE 0;

CREATE SEQUENCE SEQ_users
INCREMENT BY 1
START WITH 1
MINVALUE 0;

CREATE SEQUENCE SEQ_meals
INCREMENT BY 1
START WITH 1
MINVALUE 0;

CREATE SEQUENCE SEQ_journal
INCREMENT BY 1
START WITH 1
MINVALUE 0;

CREATE OR REPLACE FUNCTION update_meal_calories()
	RETURNS TRIGGER AS $$
DECLARE 
	total_calories NUMERIC(15,2);
BEGIN
    SELECT SUM((p.calories * pm.quantity)/100) INTO total_calories
    FROM product p
    INNER JOIN product_meals pm ON p.product_id = pm.product_id
    WHERE pm.meals_id = NEW.meals_id;
    
    UPDATE meals
    SET number_of_calories = total_calories
    WHERE meals_id = NEW.meals_id;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_meal_calories_trigger
AFTER INSERT ON product_meals
FOR EACH ROW
EXECUTE FUNCTION update_meal_calories();


CREATE OR REPLACE FUNCTION update_meal_squirrels()
	RETURNS TRIGGER AS $$
DECLARE 
	total_squirrels NUMERIC(15,2);
BEGIN
    SELECT SUM((p.squirrels * pm.quantity)/100) INTO total_squirrels
    FROM product p
    INNER JOIN product_meals pm ON p.product_id = pm.product_id
    WHERE pm.meals_id = NEW.meals_id;
    
    UPDATE meals
    SET number_of_squirrels = total_squirrels
    WHERE meals_id = NEW.meals_id;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_meal_squirrels_trigger
AFTER INSERT ON product_meals
FOR EACH ROW
EXECUTE FUNCTION update_meal_squirrels();


CREATE OR REPLACE FUNCTION update_meal_fats()
	RETURNS TRIGGER AS $$
DECLARE 
	total_fats NUMERIC(15,2);
BEGIN
    SELECT SUM((p.fats * pm.quantity)/100) INTO total_fats
    FROM product p
    INNER JOIN product_meals pm ON p.product_id = pm.product_id
    WHERE pm.meals_id = NEW.meals_id;
    
    UPDATE meals
    SET number_of_fats = total_fats
    WHERE meals_id = NEW.meals_id;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_meal_fats_trigger
AFTER INSERT ON product_meals
FOR EACH ROW
EXECUTE FUNCTION update_meal_fats();


CREATE OR REPLACE FUNCTION update_meal_carbohydrates()
	RETURNS TRIGGER AS $$
DECLARE 
	total_carbohydrates NUMERIC(15,2);
BEGIN
    SELECT SUM((p.carbohydrates * pm.quantity)/100) INTO total_carbohydrates
    FROM product p
    INNER JOIN product_meals pm ON p.product_id = pm.product_id
    WHERE pm.meals_id = NEW.meals_id;
    
    UPDATE meals
    SET number_of_carbohydrates = total_carbohydrates
    WHERE meals_id = NEW.meals_id;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_meal_carbohydrates_trigger
AFTER INSERT ON product_meals
FOR EACH ROW
EXECUTE FUNCTION update_meal_carbohydrates();   


 INSERT INTO product VALUES
 (nextval('seq_product'), 'Макароны', '333', '14.63', '1.4', '60.00');
 INSERT INTO product VALUES
 (nextval('seq_product'), 'Сосиски', '250', '11.3', '22', '1.7');
 INSERT INTO product VALUES
 (nextval('seq_product'), 'Кетчуп', '93', '1.8', '1', '22.2');

 INSERT INTO users VALUES
 (nextval('seq_users'), 'Леша');

 INSERT INTO meals VALUES
 (nextval('seq_meals'),0, 'Макароны с сосиками и кетчупом', DEFAULT, DEFAULT, DEFAULT, DEFAULT);
 INSERT INTO meals VALUES
 (nextval('seq_meals'),0, 'Макароны с сосиками', DEFAULT, DEFAULT, DEFAULT, DEFAULT);

INSERT INTO product_meals VALUES
(1, 1, 300);
INSERT INTO product_meals VALUES
(2, 1, 200);
INSERT INTO product_meals VALUES
(3, 1, 25);
INSERT INTO product_meals VALUES
(1, 2, 300);
INSERT INTO product_meals VALUES
(2, 2, 200);

 INSERT INTO journal VALUES
 (nextval('seq_journal'), '1', '1');
 INSERT INTO journal VALUES
 (nextval('seq_journal'),'1', '2');


-- add new meals and products
INSERT INTO meals VALUES(nextval('seq_meals'),0, 'Салат с Тунцом', DEFAULT, DEFAULT, DEFAULT, DEFAULT);

INSERT INTO meals VALUES(nextval('seq_meals'),0, 'Сырники', DEFAULT, DEFAULT, DEFAULT, DEFAULT);

INSERT INTO meals VALUES(nextval('seq_meals'),0, 'Курица и Паста с Овощами', DEFAULT, DEFAULT, DEFAULT, DEFAULT);

INSERT INTO meals VALUES(nextval('seq_meals'),0, 'Зеленый Смузи', DEFAULT, DEFAULT, DEFAULT, DEFAULT);

INSERT INTO product VALUES
 (nextval('seq_product'), 'Тунец', '108', '23.38', '0.95', '0');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Зеленый горошек', '81', '5.42', '0.4', '14.46');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Вареное яйцо', '154', '12.53', '10.57', '1.12');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Соленые огурцы с укропом', '18', '0.62', '0.19', '4.12');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Сметана', '214', '3.16', '20.96', '4.27');

INSERT INTO product VALUES
 (nextval('seq_product'), 'Мука рисовая', '356', '5.84', '1.44', '77.73');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Яйцо', '147', '12.58', '9.94', '0.77');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Творог 9%', '157', '16.01', '9', '2.99');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Разрыхлитель теста', '79', '0.2', '0', '19.6');

INSERT INTO product VALUES
 (nextval('seq_product'), 'Соевый соус', '75', '10', '0', '3');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Куриная грудка', '195', '29.55', '7.72', '0');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Лук', '42', '0.92', '0.08', '10.11');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Болгарский перец', '26', '0.99', '0.3', '6.03');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Помидоры', '18', '0.88', '0.2', '3.92');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Масло подсолнечное', '899', '0', '99.9', '0');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Кукурузный крахмал', '381', '0.26', '0.05', '91.27');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Сахар', '387', '0', '0', '99.98');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Паста', '359', '14', '2', '69.7');

INSERT INTO product VALUES
 (nextval('seq_product'), 'Яблоко желтое', '52', '0.26', '0.17', '13.73');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Банан', '105', '1.29', '0.39', '26.95');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Листья салата', '13', '1.05', '0.13', '2.68');
INSERT INTO product VALUES
 (nextval('seq_product'), 'Пучек шпината', '23', '2.86', '0.39', '3.63');


INSERT INTO product_meals VALUES
(4, 3, 65);
INSERT INTO product_meals VALUES
(5, 3, 80);
INSERT INTO product_meals VALUES
(6, 3, 115);
INSERT INTO product_meals VALUES
(7, 3, 63);
INSERT INTO product_meals VALUES
(8, 3, 20);

INSERT INTO product_meals VALUES
(9, 4, 48);
INSERT INTO product_meals VALUES
(10, 4, 40);
INSERT INTO product_meals VALUES
(11, 4, 177);
INSERT INTO product_meals VALUES
(12, 4, 1);

INSERT INTO product_meals VALUES
(13, 5, 100);
INSERT INTO product_meals VALUES
(14, 5, 600);
INSERT INTO product_meals VALUES
(15, 5, 200);
INSERT INTO product_meals VALUES
(16, 5, 200);
INSERT INTO product_meals VALUES
(17, 5, 200);
INSERT INTO product_meals VALUES
(18, 5, 100);
INSERT INTO product_meals VALUES
(19, 5, 10);
INSERT INTO product_meals VALUES
(20, 5, 8);
INSERT INTO product_meals VALUES
(21, 5, 200);

INSERT INTO product_meals VALUES
(22, 6, 100);
INSERT INTO product_meals VALUES
(23, 6, 50);
INSERT INTO product_meals VALUES
(24, 6, 16);
INSERT INTO product_meals VALUES
(25, 6, 500);


