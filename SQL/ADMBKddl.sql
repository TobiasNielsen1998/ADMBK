CREATE TABLE Users (
 UserID varchar(6) NOT NULL,
 
 PRIMARY KEY (UserID)
);

CREATE TABLE Teachers (
 TeacherName varchar(30) NOT NULL,   
 TeacherUserID varchar(6) NOT NULL,
 CprNumber varchar(11) NOT NULL,
 Phone varchar(12) NOT NULL,
 Email varchar(30) NOT NULL,
 
 PRIMARY KEY (TeacherUserID),
 FOREIGN KEY (TeacherUserID) REFERENCES Users(UserID)
);

CREATE TABLE Courses (
 CourseID INT NOT NULL,   
 CourseName varchar(50) NOT NULL,
 CourseFaculty varchar(50) NOT NULL,
 CourseRoom INT NOT NULL,
 CourseTeacher varchar(6) NOT NULL,
 
 PRIMARY KEY (CourseID),
 FOREIGN KEY (CourseTeacher) REFERENCES Teachers(TeacherUserID)
);


CREATE TABLE Schedules (
 CurrentSchedules INT NOT NULL AUTO_INCREMENT,
 CourseDays datetime NOT NULL,
 CourseDayEnd time NOT NULL,
 CourseID int NOT NULL,
 CourseName varchar(50) NOT NULL,
 CourseFaculty varchar(50) NOT NULL,
 CourseRoom INT NOT NULL,
 
 PRIMARY KEY (CurrentSchedules),
 FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Requests (
 Requests INT NOT NULL AUTO_INCREMENT,
 RequestStatus varchar(10) NOT NULL,
 CourseID int NOT NULL,
 CourseName varchar(50) NOT NULL,
 CourseDays datetime NOT NULL,
 CourseDayEnd time NOT NULL,
 CourseFaculty varchar(50) NOT NULL,
 CourseRoom INT NOT NULL,
 CourseTeacher varchar(6) NOT NULL,
 CourseNote varchar(255),  
 
 PRIMARY KEY (Requests),
 FOREIGN KEY (CourseID) REFERENCES Schedules(CourseID),
 FOREIGN KEY (CourseTeacher) REFERENCES Teachers(TeacherUserID)
);

CREATE TABLE AdmEmployees (
 AdmEmpName varchar(30) NOT NULL,   
 AdmEmpUserID varchar(6) NOT NULL,
 CprNumber varchar(11) NOT NULL,
 Phone varchar(12) NOT NULL,
 Email varchar(30) NOT NULL,
 
 PRIMARY KEY (AdmEmpUserID),
 FOREIGN KEY (AdmEmpUserID) REFERENCES Users(UserID)
);