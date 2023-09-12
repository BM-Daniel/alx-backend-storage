-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_value;

    SET average_value = (SELECT AVG(score) FROM corrections AS total
                        WHERE total.user_id = user_id);

    UPDATE users
    SET average_score = average_value
    WHERE id = user_id;
END
// DELIMITER