--Выведите все уникальные названия продуктов.
	SELECT DISTINCT product_name FROM products
  
--Выведите id, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов.
	SELECT products.product_id, products.product_name, products.price, nutritional_information.product_id FROM products join nutritional_information on products.product_id = nutritional_information.product_id  WHERE fiber > 5.0 
	
--Выведите название продукта с самым высоким содержанием белка (protein).
	SELECT MAX(protein) FROM products join nutritional_information on products.product_id = nutritional_information.product_id 

--Подсчитайте общую сумму калорий для продуктов каждой категории, но не учитывайте продукты с нулевым жиром (fat = 0). Выведите id категории, сумму калорий.
	SELECT  sum(calories) from products join nutritional_information on products.product_id = nutritional_information.product_id WHERE nutritional_information.fat != 0

--Рассчитайте среднюю цену товаров каждой категории. Выведите название категории, среднюю цену.
	SELECT sum(price)/count(category_name) from products join categories on products.category_id = categories.category_id