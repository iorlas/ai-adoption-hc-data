/* ============================================================================
   Stem Cell Register — legacy reporting stored procedure
   ----------------------------------------------------------------------------
   You have inherited this procedure. There is no documentation and no comment
   header describing what it does. That is the point of the exercise.

   HANDS-ON (Section 1): open this file in Claude Code and ask it to explain, in
   plain English, WHAT this procedure returns and HOW. You are only READING here,
   not running it (the tables it touches are part of the full week's schema, not
   today's file). The goal is to feel how quickly the tool makes unfamiliar code
   legible, then to stay sceptical: does its explanation actually match the SQL?

   Do not tidy this file. Later in the week you will reverse-engineer a README
   for it and then optimise it.
   ============================================================================ */

IF OBJECT_ID('dbo.fn_AgeAtRegistration', 'FN') IS NOT NULL DROP FUNCTION dbo.fn_AgeAtRegistration;
GO
CREATE FUNCTION dbo.fn_AgeAtRegistration (@dob DATE, @registered DATE)
RETURNS INT
AS
BEGIN
    -- naive age calc, ignores month/day, good enough for the smell
    RETURN DATEDIFF(YEAR, @dob, @registered);
END;
GO

IF OBJECT_ID('dbo.usp_DonorRegistryReport', 'P') IS NOT NULL DROP PROCEDURE dbo.usp_DonorRegistryReport;
GO
CREATE PROCEDURE dbo.usp_DonorRegistryReport
    @registered_since DATE = '2000-01-01'
AS
BEGIN
    SET NOCOUNT ON;

    SELECT * INTO #candidates FROM dbo.donor
    WHERE status = 'Active'
      AND dbo.fn_AgeAtRegistration(date_of_birth, registered_date) BETWEEN 16 AND 30
      AND CONVERT(VARCHAR(10), registered_date, 120) >= CONVERT(VARCHAR(10), @registered_since, 120);

    CREATE TABLE #report (
        donor_id      INT,
        registry_id   VARCHAR(10),
        full_name     NVARCHAR(120),
        loci_typed    INT,
        times_matched INT,
        donations_made INT
    );

    DECLARE @id INT, @rid VARCHAR(10), @fn NVARCHAR(50), @ln NVARCHAR(50);

    DECLARE donor_cur CURSOR FOR
        SELECT donor_id, registry_id, first_name, last_name FROM #candidates;

    OPEN donor_cur;
    FETCH NEXT FROM donor_cur INTO @id, @rid, @fn, @ln;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        INSERT INTO #report (donor_id, registry_id, full_name, loci_typed, times_matched, donations_made)
        VALUES (
            @id,
            @rid,
            @fn + ' ' + @ln,
            (SELECT COUNT(DISTINCT locus) FROM dbo.hla_typing WHERE donor_id = @id),
            (SELECT COUNT(*) FROM dbo.match_result WHERE donor_id = @id),
            (SELECT COUNT(*) FROM dbo.donation d
                JOIN dbo.workup w   ON w.workup_id = d.workup_id
                JOIN dbo.match_result m ON m.match_id = w.match_id
                WHERE m.donor_id = @id)
        );

        FETCH NEXT FROM donor_cur INTO @id, @rid, @fn, @ln;
    END

    CLOSE donor_cur;
    DEALLOCATE donor_cur;

    SELECT donor_id, registry_id, full_name, loci_typed, times_matched, donations_made
    FROM #report
    ORDER BY donations_made DESC, times_matched DESC;

    DROP TABLE #report;
    DROP TABLE #candidates;
END;
GO

PRINT 'Created dbo.fn_AgeAtRegistration and dbo.usp_DonorRegistryReport';
GO
