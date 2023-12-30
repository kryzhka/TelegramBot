

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
 (nextval('seq_meals'), 'Макароны с сосиками и кетчупом', DEFAULT, DEFAULT, DEFAULT, DEFAULT);
 INSERT INTO meals VALUES
 (nextval('seq_meals'), 'Макароны с сосиками', DEFAULT, DEFAULT, DEFAULT, DEFAULT);

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


