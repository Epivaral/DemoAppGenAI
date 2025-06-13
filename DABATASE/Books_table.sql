-- Drop the Books table if it exists
IF OBJECT_ID('Books', 'U') IS NOT NULL
    DROP TABLE Books;
GO

-- Create the Books table
CREATE TABLE Books (
    BookID INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(255) NOT NULL,
    Author NVARCHAR(255) NOT NULL,
    Genre NVARCHAR(100),
    ReadStatus NVARCHAR(50),
    Description NVARCHAR(1000)
);
GO
