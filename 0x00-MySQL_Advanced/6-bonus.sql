-- Script that creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus (
    user_id INT, project_name VARCHAR(255), score INT
)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name WHERE project_name NOT IN (SELECT name FROM projects);
    SET @project_id = (SELECT id from projects WHERE name=project_name);
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
END;
//
DELIMITER ;
