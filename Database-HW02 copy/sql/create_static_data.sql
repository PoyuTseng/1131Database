-- 建立學院表
CREATE TABLE College (
    CollegeID INT PRIMARY KEY AUTO_INCREMENT,
    NameCN VARCHAR(50) NOT NULL,
    NameEN VARCHAR(50) NOT NULL
);

-- 建立系所表
CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    NameCN VARCHAR(50) NOT NULL,
    NameEN VARCHAR(50) NOT NULL,
    CollegeID INT,
    FOREIGN KEY (CollegeID) REFERENCES College(CollegeID)
);

-- 建立課程表
CREATE TABLE Course (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    NameCN VARCHAR(50) NOT NULL,
    NameEN VARCHAR(50) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

-- 插入學院資料
INSERT INTO College (NameCN, NameEN) VALUES
('工學院', 'Engineering College'),
('理學院', 'Science College');

-- 插入系所資料
INSERT INTO Department (NameCN, NameEN, CollegeID) VALUES
('機械工程系', 'Department of Mechanical Engineering', 1),
('土木工程系', 'Department of Civil Engineering', 1),
('數學系', 'Department of Mathematics', 2),
('物理系', 'Department of Physics', 2);

-- 插入課程資料
INSERT INTO Course (NameCN, NameEN, DepartmentID) VALUES
-- 機械工程系
('熱力學', 'Thermodynamics', 1),
('機械設計', 'Mechanical Design', 1),
('材料科學', 'Materials Science', 1),
-- 土木工程系
('結構力學', 'Structural Mechanics', 2),
('工程材料', 'Engineering Materials', 2),
('基礎建築設計', 'Fundamentals of Architectural Design', 2),
-- 數學系
('高等代數', 'Advanced Algebra', 3),
('微積分', 'Calculus', 3),
('數據分析', 'Data Analysis', 3),
-- 物理系
('量子物理', 'Quantum Physics', 4),
('光學', 'Optics', 4),
('電磁學', 'Electromagnetism', 4);
