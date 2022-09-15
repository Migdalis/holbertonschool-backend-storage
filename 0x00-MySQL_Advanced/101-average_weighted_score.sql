-- Script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(project.weight * correction.score) / SUM(project.weight) FROM corrections AS correction
    RIGHT JOIN projects AS project ON correction.project_id = project.id
    WHERE correction.user_id = users.id);
END;
//
DELIMITER ;
