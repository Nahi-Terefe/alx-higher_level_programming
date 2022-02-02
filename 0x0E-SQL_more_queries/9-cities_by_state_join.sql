-- list all cities in database
-- display id, city name, state name
SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM `cities` JOIN `states` ON `cities`.`state_id` = `states`.`id`;
