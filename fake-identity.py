import random
from datetime import datetime, timedelta
import string

# Names Lists
first_names_male = ['Victor', 'Reed', 'Tobias', 'Axel', 'Chase', 'Milo', 'Nolan', 'Dean', 'Owen', 'Gage',
    'Rowan', 'Shane', 'Dorian', 'Graham', 'Vaughn', 'Dexter', 'Cole', 'Xander', 'Weston', 'Alec',
    'Warren', 'Bryce', 'Mason', 'Alfred', 'Julian', 'Isaiah', 'Aidan', 'Miles', 'Ryder', 'Nathaniel',
    'Ezra', 'Blake', 'Brayden', 'Caden', 'Jackson', 'Rylan', 'Jaxon', 'Rhett', 'Travis', 'Zane',
    'Kai', 'Hunter', 'Joel', 'Titus', 'Carter', 'Levi', 'Ethan', 'Theo', 'Leo', 'Elliott', 'Reid',
    'Beckett', 'Myles', 'Ezekiel', 'Aiden', 'Emmett', 'Victor', 'Archer', 'Dylan', 'Amos', 'Isaac',
    'Jace', 'Braxton', 'Carter', 'Parker', 'Gabriel', 'George', 'Nash', 'Finn', 'Benjamin', 'Elijah',
    'Mason', 'Joseph', 'Levi', 'Lucas', 'Oliver', 'David', 'Zachary', 'Samuel', 'Evan', 'Roman',
    'Nicholas', 'Jude', 'Jack', 'Milo', 'Gavin', 'Kai', 'Riley', 'Maxwell', 'Mateo', 'Jaxon', 'Isaac',
    'Eli', 'Liam', 'Luca', 'Parker', 'Hudson', 'Wyatt', 'Landon', 'James', 'Kaden', 'Isaiah', 'Jasper',
    'Owen', 'Finn', 'Harrison', 'Henry', 'Caleb', 'Axel', 'David', 'Elijah', 'Matthew', 'Charles',
    'Graham', 'Seth', 'Jordan', 'Giovanni', 'Theo', 'Roman', 'Zion', 'Jackson', 'Grayson', 'Emmett',
    'Ryder', 'Levi', 'Maverick', 'Elijah', 'Asher', 'Theo', 'Dylan', 'Liam', 'Isaac', 'Miles', 'Maximus',
    'Lucas', 'Gabriel', 'Caleb', 'David', 'Santiago', 'Xander', 'Gage', 'Jack', 'Kai', 'Emerson', 'Elijah',
    'Mason', 'Colton', 'Maddox', 'Gavin', 'Nathaniel', 'Axel', 'Jase', 'Milo', 'Caden', 'Hunter', 'Eli',
    'Tristan', 'Dean', 'Grayson', 'Hudson', 'Asher', 'Charles', 'Caleb', 'Easton', 'Roman', 'Finn', 'Aidan',
    'Sullivan', 'Griffin', 'August', 'Maxwell', 'Declan', 'Hayden', 'Charlie', 'Carson', 'Jace', 'Xander',
    'Wyatt', 'Blake', 'Tobias', 'Dylan', 'Dax', 'Jett', 'Cameron', 'Milo', 'Riley', 'Leo', 'Nolan', 'Jameson',
    'Everett', 'Dominic', 'Zane', 'Gage', 'Avery', 'Silas', 'Declan', 'Jude', 'Joseph', 'Leo', 'Elliot', 'Aaron',
    'Bentley', 'Jason', 'Phoenix', 'Xander', 'Luca', 'Aiden', 'Harrison', 'Isaac', 'Zayden', 'Ryder', 'Jordan',
    'Matias', 'Wesley', 'Jaxson', 'Jayden', 'Charles', 'Carter', 'Blake', 'Jacob', 'Emmett', 'Jaxon', 'Weston',
    'Gavin', 'Oliver', 'Joshua', 'Mason', 'Ethan', 'Sebastian', 'Isaiah', 'Noah', 'Elijah', 'Liam', 'Hudson',
    'Wyatt', 'Zachary', 'James', 'Lucas', 'Aiden', 'Eli', 'Jackson', 'Levi', 'Carter', 'Jack', 'Miles', 'Matthew',
    'Andrew', 'Benjamin', 'William', 'Samuel', 'David', 'Daniel', 'Nolan', 'Logan', 'Sebastian', 'Henry', 'Julian',
    'Luke', 'Isaac', 'Joseph', 'Jack', 'Maverick', 'Santiago', 'Hudson', 'Landon', 'Caleb', 'Jace', 'Carter',
    'Emmett', 'Asher', 'Giovanni', 'Grayson', 'Zane', 'Calvin', 'Sawyer', 'Kai', 'Graham', 'Jasper', 'Colton',
    'Benjamin', 'Thomas', 'Leo', 'Ryan', 'Jeremiah', 'Levi', 'Matthew', 'Aiden', 'Roman', 'Jaxon', 'Jackson',
    'Eli', 'Jacob', 'Michael', 'David', 'John', 'Nathaniel', 'Adam', 'Elliot', 'Bennett', 'Brayden', 'Finn',
    'Jameson', 'Cameron', 'Reid', 'Isaiah', 'Zane', 'Miles', 'Caleb', 'Wyatt', 'Xander', 'Henry', 'Avery',
    'Christopher', 'Robert', 'Aidan', 'Tyler', 'Oliver', 'Liam', 'Mateo', 'Emerson', 'Griffin', 'Benjamin', 
    'Jack', 'Levi', 'Matthew', 'Jordan', 'Asher', 'Milo', 'Jackson', 'Benjamin', 'Jonah', 'Samuel', 'Xavier',
    'Jackson', 'Finn', 'Dylan', 'Carter', 'Easton', 'Jaxon', 'Bryce', 'Rowan', 'Victor', 'Zachary', 'Ezekiel',
    'Aidan', 'Beckett', 'Zane', 'Christian', 'Jameson', 'Zion', 'Julian', 'Eli', 'Avery', 'Brady', 'Zachary',
    'Daniel', 'Carter', 'Sebastian', 'Benjamin', 'Sawyer', 'Emmett', 'Joshua', 'Hudson', 'Robert', 'Max',
    'Landon', 'Samuel', 'Levi', 'Oliver', 'Lucas', 'Aiden', 'Miles', 'Nolan', 'Xander', 'Maxwell', 'Jordan',
    'Hudson', 'Declan', 'Griffin', 'Benjamin', 'Wyatt', 'Isaiah', 'Dylan', 'Hudson', 'Aidan', 'Roman', 'Mason',
    'Oliver', 'Jaxon', 'Eli', 'Caleb', 'James', 'Maverick', 'Harrison', 'Theo', 'Xavier', 'Finn', 'Reed', 'Liam',
    'Sawyer', 'Kaden', 'Ezekiel', 'Giovanni', 'Jonah', 'Zachary', 'Tyler', 'Ryan', 'Blake', 'Mason', 'Levi',
    'Blake', 'Landon', 'Bennett', 'Luke', 'Isaac', 'Roman', 'Milo', 'Nolan', 'Eli', 'Nathaniel', 'Hunter', 'Christian']
first_names_female = ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Harper', 'Evelyn',
    'Abigail', 'Ella', 'Scarlett', 'Grace', 'Aria', 'Chloe', 'Isla', 'Mila', 'Lily', 'Luna',
    'Zoe', 'Nora', 'Riley', 'Leah', 'Audrey', 'Hazel', 'Violet', 'Addison', 'Brooklyn', 'Bella',
    'Avery', 'Lucy', 'Skylar', 'Paisley', 'Everly', 'Anna', 'Sophie', 'Natalie', 'Hannah', 'Layla',
    'Lillian', 'Camila', 'Avery', 'Ellie', 'Stella', 'Aurora', 'Zoey', 'Willow', 'Emilia', 'Paisley',
    'Autumn', 'Ariana', 'Genesis', 'Eleanor', 'Caroline', 'Nova', 'Sadie', 'Allison', 'Gabriella', 'Kinsley',
    'Naomi', 'Sarah', 'Madelyn', 'Cora', 'Ruby', 'Eva', 'Eva', 'Emery', 'Clara', 'Madeline', 'Adeline',
    'Alexa', 'Vivian', 'Charlie', 'Quinn', 'Josephine', 'Samantha', 'Maya', 'Brielle', 'Peyton', 'Katherine',
    'Eva', 'Mackenzie', 'Delilah', 'Emerson', 'Catherine', 'Penelope', 'Lydia', 'Aubrey', 'Elliana', 'Elena',
    'Sophie', 'Sydney', 'Kennedy', 'Hailey', 'Melanie', 'Leilani', 'Valentina', 'Autumn', 'Reagan', 'Mackenzie',
    'Taylor', 'Gabrielle', 'Piper', 'Julia', 'Peyton', 'Daisy', 'Kylie', 'Genesis', 'Everleigh', 'Maddison',
    'Bailey', 'Alicia', 'Josephine', 'Lillian', 'Emilia', 'Eliza', 'Rachel', 'Ariana', 'Charlotte', 'Skylar',
    'Adalynn', 'Serenity', 'Nina', 'Amaya', 'Kaitlyn', 'Addison', 'Charlotte', 'Eden', 'Sadie', 'Zoey',
    'Madison', 'Nina', 'Sienna', 'Lindsey', 'Ariana', 'Melody', 'Morgan', 'Charlie', 'Dakota', 'Reese',
    'Paige', 'Camila', 'Ava', 'Emerson', 'Avery', 'Sophia', 'Ellie', 'Harper', 'Kendra', 'Piper', 'Arianna',
    'Kaitlyn', 'Lydia', 'Autumn', 'Reagan', 'Isabella', 'Jessica', 'Paige', 'Kennedy', 'Charlotte', 'Gianna',
    'Emery', 'Charlotte', 'Julia', 'Eva', 'Hazel', 'Ruby', 'Lily', 'Olivia', 'Aubrey', 'Isla', 'Leah', 'Mila',
    'Sophie', 'Madeline', 'Gabriella', 'Alaina', 'Sierra', 'Adeline', 'Naomi', 'Maya', 'Hannah', 'Sophia',
    'Caroline', 'Addison', 'Cora', 'Kennedy', 'Ivy', 'Sienna', 'Madeline', 'Zoe', 'Ellie', 'Lily', 'Paisley',
    'Kinsley', 'Layla', 'Peyton', 'Isabel', 'Violet', 'Makayla', 'Samantha', 'Riley', 'Lillian', 'Jocelyn',
    'Everly', 'Emilia', 'Gabrielle', 'Victoria', 'Grace', 'Ella', 'Hazel', 'Savannah', 'Aaliyah', 'Sophie',
    'Alexa', 'Brianna', 'Harlow', 'Avery', 'Alicia', 'Gianna', 'Kylie', 'Zoe', 'Lillian', 'Amaya', 'Sophie',
    'Camila', 'Autumn', 'Sarah', 'Gabriela', 'Genesis', 'Brooklyn', 'Emma', 'Ariana', 'Addison', 'Sienna',
    'Valentina', 'Eden', 'Avery', 'Naomi', 'Evelyn', 'Mackenzie', 'Eloise', 'Elena', 'Anna', 'Kayla',
    'Clara', 'Sophie', 'Lydia', 'Ashley', 'Zoe', 'Juliana', 'Arianna', 'Jade', 'Leilani', 'Vera', 'Samantha',
    'Addison', 'Scarlett', 'Ariana', 'Anna', 'Kylie', 'Lillian', 'Ariana', 'Ellie', 'Emery', 'Paisley', 'Kaylee',
    'Vivian', 'Josephine', 'Mackenzie', 'Everly', 'Lola', 'Kaitlyn', 'Isabella', 'Stella', 'Eva', 'Alaina',
    'Maya', 'Arianna', 'Zoey', 'Amelia', 'Valerie', 'Addison', 'Piper', 'Madelyn', 'Lucy', 'Lilah', 'Lena',
    'Zoey', 'Caroline', 'Sofia', 'Mia', 'Bella', 'Emory', 'Gianna', 'Autumn', 'Jade', 'Camille', 'Lena',
    'Josephine', 'Jocelyn', 'Leilani', 'Vivian', 'Leah', 'Adeline', 'Natalie', 'Savannah', 'Alina', 'Riley',
    'Ella', 'Quinn', 'Olivia', 'Valentina', 'Norah', 'Stella', 'Amaya', 'Addison', 'Violet', 'Willow', 'Ruby',
    'Zoe', 'Ariana', 'Penelope', 'Sophie', 'Julia', 'Aubrey', 'Hannah', 'Lucy', 'Ava', 'Autumn', 'Madeline',
    'Leilani', 'Caroline', 'Julia', 'Charlotte', 'Vera', 'Adeline', 'Eleanor', 'Scarlett', 'Addison', 'Zoe',
    'Vivian', 'Kaitlyn', 'Avery', 'Lily', 'Emma', 'Mackenzie', 'Reagan', 'Sarah', 'Hannah', 'Paige', 'Josephine']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'García', 'Rodríguez', 'Wilson',
    'Martínez', 'Anderson', 'Taylor', 'Thomas', 'Hernández', 'Moore', 'Martin', 'Jackson', 'Thompson', 'White',
    'Lopez', 'Lee', 'González', 'Harris', 'Clark', 'Lewis', 'Roberts', 'Walker', 'Young', 'Allen',
    'King', 'Scott', 'Green', 'Adams', 'Baker', 'Nelson', 'Hall', 'Rivera', 'Carter', 'Mitchell',
    'Perez', 'Robinson', 'Miller', 'Murphy', 'King', 'Wright', 'Evans', 'Torres', 'Collins', 'Stewart',
    'Sanchez', 'Morris', 'Rodriguez', 'Reed', 'Cook', 'Morgan', 'Bell', 'Bailey', 'Cooper', 'Richardson',
    'Cox', 'Howard', 'Ward', 'Flores', 'Garcia', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders',
    'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Hughes', 'Chavez', 'Stevens', 'Dixon', 'Ramirez',
    'Grant', 'Duncan', 'Peters', 'Long', 'Bryant', 'Alexander', 'Russell', 'Douglas', 'Harrison', 'Jenkins',
    'Perry', 'Powell', 'Sullivan', 'Russell', 'West', 'Terry', 'Nguyen', 'Craig', 'Chavez', 'Richardson',
    'Shaw', 'Walsh', 'Henry', 'West', 'Bishop', 'Schmidt', 'Sullivan', 'Henderson', 'Spencer', 'George',
    'Graham', 'Carroll', 'Burns', 'Simmons', 'Foster', 'Bryan', 'Jenkins', 'Vasquez', 'Snyder', 'Simpson',
    'Mason', 'Wagner', 'Olson', 'Ryan', 'Murray', 'Freeman', 'Holland', 'George', 'Gibson', 'Gomez',
    'Miller', 'Chapman', 'Webb', 'Day', 'Watson', 'Harrison', 'Gonzalez', 'Nash', 'Alvarez', 'Mendez',
    'Gibbs', 'Griffin', 'Roman', 'Diaz', 'Vazquez', 'Kelly', 'Franklin', 'Wood', 'Hicks', 'Curtis',
    'Patterson', 'Jensen', 'Serrano', 'Dunn', 'Murray', 'Carlson', 'Mejia', 'Willis', 'Fisher', 'Meyer',
    'Wallace', 'Jenkins', 'Maldonado', 'Hines', 'Bishop', 'Wells', 'Alvarez', 'Douglas', 'Burgess',
    'Curtis', 'Snyder', 'Hawkins', 'Williamson', 'Hoffman', 'Schneider', 'Shaw', 'Bowman', 'Morrison',
    'Craig', 'Chavez', 'Serrano', 'Fletcher', 'Petersen', 'Romero', 'Santiago', 'Davis', 'Johnston',
    'Davidson', 'George', 'Tucker', 'Harrison', 'Hughes', 'Trujillo', 'Davis', 'Fisher', 'Chang',
    'Singh', 'Ford', 'Russell', 'Patterson', 'Lambert', 'Bailey', 'Austin', 'Sanchez', 'Mills', 'Greer',
    'Kim', 'Barker', 'Reed', 'Grant', 'Francis', 'Parker', 'Freeman', 'Morrison', 'Brady', 'Kim',
    'Sanders', 'Hicks', 'Freeman', 'Marshall', 'Barnett', 'Walker', 'Hughes', 'O’Connor', 'Price',
    'Miller', 'Bailey', 'Ford', 'Diaz', 'Wilkerson', 'Stevenson', 'James', 'Horton', 'Black', 'Gordon',
    'Manning', 'Cameron', 'Harmon', 'Carlson', 'Martin', 'Wilkins', 'Whitehead', 'Parker', 'Hicks',
    'Stone', 'Chang', 'Curtis', 'Rowe', 'Gibson', 'Barker', 'Harrison', 'Holloway', 'Richards', 'Fowler',
    'Howard', 'Perry', 'Mason', 'Watson', 'Kelley', 'Vazquez', 'Sims', 'Mendoza', 'Bowman', 'Ramos',
    'Santiago', 'Liu', 'Nunez', 'Peters', 'Barnes', 'Parker', 'Franklin', 'Wood', 'Murphy', 'Klein',
    'Nichols', 'O’Neill', 'Spencer', 'Matthews', 'Diaz', 'Harris', 'Willis', 'Mcdonald', 'Williamson']
male_middle_names = ['James', 'John', 'William', 'Joseph', 'David', 'Michael', 'Thomas', 'Charles', 'Lee', 'Edward',
    'Ray', 'Jameson', 'Robert', 'Alexander', 'Paul', 'Allen', 'Richard', 'Benjamin', 'Elliott', 'Josephine',
    'Ryan', 'Scott', 'Daniel', 'Samuel', 'George', 'Patrick', 'Andrew', 'Thomas', 'Christopher', 'William',
    'Raymond', 'Kenneth', 'Thomas', 'David', 'Francis', 'Joshua', 'Matthew', 'Michael', 'Arthur', 'Martin',
    'Louis', 'Gregory', 'Brian', 'Donald', 'Keith', 'Jacob', 'Eric', 'Henry', 'George', 'Anthony', 'Joseph',
    'Frederick', 'Thomas', 'Walter', 'Steven', 'Keith', 'Douglas', 'Benjamin', 'Joseph', 'Daniel', 'Benjamin',
    'Patrick', 'Charles', 'Richard', 'Henry', 'Samuel', 'Edward', 'Harold', 'Victor', 'Harvey', 'Walter',
    'Albert', 'Leonard', 'Thomas', 'Alan', 'Brian', 'Howard', 'Jack', 'Craig', 'Joseph', 'Clifford', 'Brian',
    'Joseph', 'Matthew', 'Martin', 'James', 'Caleb', 'David', 'George', 'Maxwell', 'Seth', 'Bryan', 'Austin',
    'Russell', 'Christopher', 'Ernest', 'Cameron', 'Frank', 'Timothy', 'Ernest', 'Leonard', 'Chad', 'Zachary',
    'Clinton', 'Arthur', 'Edward', 'Jeremy', 'Johnathan', 'Grant', 'Douglas', 'Luke', 'Clyde', 'Morgan',
    'Carl', 'Cameron', 'Lee', 'Frederick', 'Franklin', 'Dean', 'Henry', 'Mitchell', 'Grant', 'Raymond',
    'Carter', 'Donald', 'Norman', 'Walter', 'Cecil', 'Scott', 'Warren', 'Seth', 'Jameson', 'Abraham', 'Darren',
    'Tyler', 'Kenneth', 'Jackson', 'Hugh', 'Jared', 'Jesse', 'Curtis', 'Harvey', 'Nathaniel', 'Samuel',
    'Nolan', 'Russell', 'Walter', 'Freeman', 'Dylan', 'Caleb', 'Jaden', 'Jesse', 'Emmett', 'Patrick',
    'Cameron', 'Bradley', 'Seth', 'Jacob', 'Douglas', 'Garrett', 'Tanner', 'Walter', 'Christopher', 'Emmanuel',
    'Calvin', 'Kurt', 'Lewis', 'Cole', 'Harrison', 'Isaiah', 'Cameron', 'Martin', 'Joshua', 'Isaac', 'Clark',
    'Wyatt', 'Mason', 'Hunter', 'Blake', 'Brandon', 'Harold', 'Dustin', 'Stephen', 'Douglas', 'Victor', 'Evan',
    'Scott', 'Glen', 'Jace', 'Joel', 'Tyson', 'Nicholas', 'Bennett', 'Roy', 'Eugene', 'Victor', 'Bruce', 'Stewart',
    'Luke', 'Roger', 'Morris', 'Wyatt', 'Isaiah', 'Anthony', 'Colin', 'Albert', 'Quinton', 'Craig', 'Wayne',
    'Mack', 'Jared', 'Travis', 'Steven', 'Mason', 'Elliott', 'Franklin', 'Russell', 'Avery', 'Trenton', 'Dorian',
    'Donovan', 'Kendall', 'Landon', 'Roy', 'Gage', 'Reed', 'Owen', 'Adrian', 'Eli', 'Lyle', 'Nash', 'Zachariah',
    'Damien', 'Derrick', 'Randy', 'Chad', 'Lamar', 'Cameron', 'Jeffrey', 'Colton', 'Lee', 'Reid', 'Mitchell', 'Dustin']
female_middle_names = ['Marie', 'Ann', 'Elizabeth', 'Grace', 'Rose', 'Lynn', 'Lee', 'Jane', 'Eve', 'Mae',
    'Nicole', 'Alice', 'Ruth', 'Claire', 'Faith', 'Jean', 'Catherine', 'Victoria', 'Louise', 'Diane',
    'Joan', 'May', 'Jeanette', 'Helen', 'Jade', 'Sophia', 'Paige', 'Charlotte', 'Leigh', 'Irene',
    'Faye', 'Isabel', 'Camille', 'Morgan', 'Lillian', 'Louisa', 'Kate', 'Rebecca', 'Sophie',
    'Rachel', 'Maria', 'Elaine', 'Michelle', 'Rosemary', 'Catherine', 'Eleanor', 'Victoria', 'Grace',
    'Lola', 'Caroline', 'Lindsey', 'Kimberly', 'Angelina', 'Alexis', 'Monica', 'Olivia', 'Daisy',
    'Evelyn', 'Ivy', 'Charlotte', 'Emma', 'Ava', 'Megan', 'Adeline', 'Violet', 'Madeline', 'Olivia',
    'Gabrielle', 'Juliette', 'Clara', 'Eleanor', 'Lydia', 'Amelia', 'Tess', 'Aubrey', 'Emily',
    'Lily', 'Scarlett', 'Julia', 'Eden', 'Mia', 'Jasmine', 'Hannah', 'Bella', 'Emma', 'Morgan',
    'Audrey', 'Sophia', 'Zoe', 'Harper', 'Ashley', 'Vivian', 'Chloe', 'Isabelle', 'Felicity',
    'Adriana', 'Katherine', 'Madison', 'Delilah', 'Eliza', 'Megan', 'Leah', 'Lydia', 'Tessa',
    'Autumn', 'Paige', 'Lillian', 'Madeline', 'Lacey', 'Hazel', 'Ariana', 'Lena', 'Brielle',
    'Jasmine', 'Willow', 'Olivia', 'Madeline', 'Brooklyn', 'Alexa', 'Abigail', 'Jordan', 'Cecilia',
    'Harriet', 'Mila', 'Brianna', 'Georgia', 'Melanie', 'Riley', 'Quinn', 'Sophie', 'Brittany',
    'Grace', 'Vivienne', 'Serenity', 'Bailey', 'Natalie', 'Peyton', 'Willa', 'Ava', 'Leah',
    'Olivia', 'Iris', 'Ruby', 'Vera', 'Carmen', 'Talia', 'Sydney', 'Maya', 'Brooklyn', 'Jade',
    'Emma', 'Sadie', 'Kaitlyn', 'Nina', 'Addison', 'Samantha', 'Amelia', 'Jocelyn', 'Jada', 'Anastasia',
    'Ivy', 'Tiffany', 'Chloe', 'Zoey', 'Talia', 'Sydney', 'Eloise', 'Caroline', 'Molly', 'Holly',
    'Natalie', 'Brianna', 'Kaitlyn', 'Megan', 'Zoe', 'Riley', 'Diana', 'Emma', 'Alison', 'Taylor',
    'Lena', 'Ella', 'Faith', 'Alexandra', 'Eve', 'Marlene', 'Paige', 'Sophie', 'Hannah', 'Abigail',
    'Sierra', 'Camila', 'Irene', 'Angelina', 'Tori', 'Carissa', 'Savannah', 'Jade', 'Ariana', 'Mia',
    'Rebecca', 'Sienna', 'Scarlett', 'Maddie', 'Delaney', 'Caitlyn', 'Brielle', 'Madeline', 'Carly',
    'Emma', 'Samantha', 'Arianna', 'Sophia', 'Morgan', 'Ashley', 'Mikayla', 'Natalie', 'Lydia',
    'Ella', 'Riley', 'Lillian', 'Zoe', 'Bailey', 'Gabrielle', 'Taylor', 'Gianna', 'Melanie', 'Adrianna',
    'Jade', 'Fiona', 'Elise', 'Tessa', 'Addison', 'Faith', 'Mikayla', 'Eva', 'Andrea', 'Isabel', 'Ruby',
    'Caroline', 'Taylor', 'Marissa', 'Ruth', 'Emily', 'Mila', 'Mariana', 'Adeline', 'Catherine', 'Lydia']

# Zodiac and Location
ziodiac_sign = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 
    'Capricorn', 'Aquarius', 'Pisces']
street_names = [
    'Main Street', 'First Street', 'Second Street', 'Third Street', 'Elm Street', 'Oak Street', 'Pine Street',
    'Maple Street', 'Washington Street', 'Broadway', 'High Street', 'Park Avenue', 'King Street', 'Church Street',
    'Cedar Street', 'River Road', 'Lake Road', 'Sunset Boulevard', 'North Avenue', 'South Avenue', 'East Road',
    'West Road', 'Hill Street', 'Monroe Street', 'Jefferson Street', 'Franklin Street', 'Adams Street', 'Lincoln Street',
    'State Street', 'Victory Road', 'Rose Street', 'Baker Street', 'Pleasant Street', 'Green Street', 'Spring Street',
    'Woods Road', 'Sunnyvale Road', 'Cottonwood Drive', 'Independence Avenue', 'Heritage Way', 'Hilltop Drive',
    'Ridge Road', 'Country Road', 'Sunshine Street', 'Silver Avenue', 'Golden Drive', 'Main Avenue', 'Kingston Road',
    'Broadway Avenue', 'Peachtree Street', 'Lakeside Drive', 'Shady Lane', 'Oakwood Drive', 'Rainbow Boulevard',
    'Cherry Blossom Drive', 'Cypress Street', 'Sunset Drive', 'Sierra Avenue', 'Mountain View Road', 'Water Street',
    'Pinehurst Drive', 'Clearview Street', 'Bluebell Road', 'Hawthorne Avenue', 'Riverfront Road', 'Wellington Drive',
    'Summit Street', 'Miller Road', 'Maple Avenue', 'Redwood Street', 'Tanglewood Drive', 'Linden Street', 'Ash Street',
    'Briargate Road', 'New Hope Road', 'Parkwood Drive', 'Thornhill Street', 'Windsor Road', 'Chestnut Street',
    'Hickory Lane', 'Crescent Avenue', 'Valley Road', 'Sunrise Boulevard', 'Silver Oak Drive', 'Rolling Hills Road',
    'Riverstone Lane', 'Belfast Road', 'Bristol Drive', 'Cottonwood Avenue', 'Chestnut Avenue', 'Glenwood Road',
    'Silver Creek Drive', 'Eagle Street', 'Springdale Road', 'Copperstone Drive', 'Mountain View Drive', 'Beach Street']
cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 
    'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'San Francisco',
    'Charlotte', 'Indianapolis', 'Seattle', 'Denver', 'Washington D.C.', 'Boston', 'El Paso', 
    'Detroit', 'Nashville', 'Portland', 'Memphis', 'Oklahoma City', 'Las Vegas', 'Louisville', 
    'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Mesa', 'Sacramento', 'Kansas City', 
    'Long Beach', 'Atlanta', 'Colorado Springs', 'Raleigh', 'Miami', 'Omaha', 'Oakland', 'Minneapolis',
    'Tulsa', 'Wichita', 'Arlington', 'New Orleans', 'Cleveland', 'Bakersfield', 'Tampa', 'Henderson', 
    'Aurora', 'Honolulu', 'Anaheim', 'Santa Ana', 'Riverside', 'Corpus Christi', 'Lexington', 'St. Louis', 
    'Stockton', 'Pittsburgh', 'St. Paul', 'Cincinnati', 'Anchorage', 'Greensboro', 'Plano', 'Newark', 
    'Lincoln', 'Orlando', 'Irvine', 'Toledo', 'Jersey City', 'Chula Vista', 'Durham', 'Fort Wayne', 
    'Buffalo', 'Madison', 'Lubbock', 'Chandler', 'Glendale', 'Reno', 'Norfolk', 'Winston-Salem', 'Gilbert', 
    'Hialeah', 'Arlington', 'Huntington Beach', 'Montgomery', 'Boise', 'Richmond', 'Des Moines', 
    'Spokane', 'Tacoma', 'San Bernardino', 'Modesto', 'Fontana', 'Santa Clarita', 'Birmingham', 
    'Oxnard', 'Fayetteville', 'Moreno Valley', 'Shreveport', 'Aurora', 'Yonkers', 'Columbia', 'Lakewood',
    'Cape Coral', 'Peoria', 'Jackson', 'Naperville', 'Escondido', 'Fullerton', 'McKinney', 'Killeen', 
    'Bellevue', 'Rockford', 'McAllen', 'Costa Mesa', 'Inglewood', 'Manchester', 'Waterbury', 'Charleston',
    'West Valley City', 'Lewisville', 'Huntington', 'Gresham', 'Fargo', 'Glendale', 'South Bend', 'Edmond',
    'Columbus', 'Round Rock', 'Nampa', 'Shreveport', 'Lafayette', 'Baton Rouge', 'Tallahassee', 
    'Tempe', 'Chattanooga', 'Syracuse', 'Albany', 'Denton', 'Allentown', 'Lansing', 'Evansville', 'Toledo', 
    'Pueblo', 'Chico', 'Bend', 'Springfield', 'Cedar Rapids', 'Tallahassee', 'Lincoln', 'Overland Park']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
car = ['Toyota Corolla', 'Honda Civic', 'Ford F-150', 'Chevrolet Silverado', 'Ram 1500', 'Honda Accord', 
    'Toyota Camry', 'Nissan Altima', 'Ford Mustang', 'Chevrolet Equinox', 'Jeep Grand Cherokee', 'Tesla Model 3', 
    'BMW 3 Series', 'Audi A4', 'Mercedes-Benz C-Class', 'Volkswagen Jetta', 'Hyundai Elantra', 'Chevrolet Malibu',
    'Nissan Rogue', 'Subaru Outback', 'Kia Sorento', 'Mazda CX-5', 'Chrysler Pacifica', 'Honda CR-V', 'Toyota RAV4', 
    'Ford Escape', 'Chevrolet Traverse', 'BMW X5', 'Jeep Wrangler', 'Honda Pilot', 'Ram 2500', 'Chevrolet Tahoe', 
    'Toyota Tacoma', 'Nissan Frontier', 'GMC Sierra 1500', 'Ford Explorer', 'Hyundai Tucson', 'Tesla Model X', 
    'Ford Expedition', 'Lincoln Navigator', 'Kia Telluride', 'Subaru Forester', 'Mazda 3', 'Chevrolet Colorado', 
    'BMW X3', 'Toyota Highlander', 'Ford Ranger', 'Audi Q5', 'Honda Odyssey', 'Ford Focus', 'Chevrolet Spark', 
    'Toyota 4Runner', 'Honda Fit', 'Hyundai Santa Fe', 'Mazda MX-5 Miata', 'Nissan Sentra', 'Chrysler 300', 
    'Buick Enclave', 'Ford Fusion', 'GMC Terrain', 'BMW 5 Series', 'Ford Fusion Hybrid', 'Toyota Sienna', 'Nissan Murano',
    'Chevrolet Impala', 'Dodge Charger', 'Mazda CX-9', 'Chevrolet Suburban', 'Honda Ridgeline', 'Ford Bronco', 
    'Toyota Prius', 'Honda Insight', 'Chevrolet Bolt EV', 'Kia Forte', 'Toyota Land Cruiser', 'GMC Yukon', 
    'Chrysler 200', 'Toyota Sequoia', 'Ford Mustang Mach-E', 'Tesla Model S', 'Nissan Leaf', 'Jeep Cherokee', 
    'Hyundai Ioniq', 'Rivian R1T', 'Ford F-250 Super Duty', 'Chevrolet Bolt', 'Toyota 86', 'Nissan Juke', 
    'Jeep Gladiator', 'Chrysler Voyager', 'Hyundai Kona', 'Subaru Crosstrek', 'GMC Canyon', 'Honda HR-V', 
    'Chevrolet Sonic', 'Nissan Titan', 'Ram 3500', 'BMW Z4', 'Toyota Avalon', 'Tesla Model Y', 'Kia Niro', 
    'Chevrolet Traverse', 'Toyota Venza', 'Ford F-350 Super Duty', 'Dodge Durango', 'Mazda 6', 'Hyundai Veloster', 
    'BMW 7 Series', 'Toyota Mirai', 'Cadillac Escalade', 'Chevrolet Corvette', 'Lexus RX', 'Acura MDX', 
    'Lexus ES', 'Audi Q7', 'BMW X7', 'Jaguar F-Pace', 'Lexus GX', 'Subaru Legacy', 'Ford F-450 Super Duty',
    'Ram 1500 Classic', 'Chevrolet Malibu Hybrid', 'Ford Mustang GT', 'Toyota Supra', 'Chevrolet Camaro', 
    'Honda Civic Type R', 'Tesla Roadster', 'Dodge Challenger', 'Subaru WRX', 'Ford F-450', 'Nissan Altima Hybrid',
    'Toyota Yaris', 'Honda CR-V Hybrid', 'Chevrolet Silverado HD', 'Ford F-150 Raptor', 'Toyota Corolla Hatchback', 
    'Honda Insight Hybrid', 'Hyundai Palisade', 'Chevrolet Traverse High Country', 'Ford F-250', 'Honda Passport', 
    'Toyota Tundra', 'Kia Stinger', 'Hyundai Ioniq Electric', 'Mazda CX-30', 'Chrysler 300C', 'Nissan Titan XD',
    'Ford Expedition Max', 'Dodge Ram ProMaster', 'Chevrolet Express', 'Chevrolet Silverado 2500HD', 'Toyota Land Cruiser Prado',
    'Ford F-350', 'GMC Sierra HD', 'Chevrolet Colorado ZR2', 'Nissan Rogue Sport', 'Mazda CX-50', 'Ram 3500 Limited',
    'Toyota Venza Hybrid', 'Jeep Wagoneer', 'Dodge Grand Caravan', 'Chevrolet Spark EV', 'Chevrolet Volt', 'Ford Transit',
    'Honda Civic Sedan', 'Honda Civic Hatchback', 'BMW i3', 'Mercedes-Benz E-Class', 'Ford Focus ST', 'Chevrolet Malibu RS', 
    'Hyundai Genesis', 'Chevrolet Traverse RS', 'Honda Civic Si', 'Ram ProMaster City', 'Chrysler 300S', 'Tesla Model S Plaid',
    'Toyota Camry Hybrid', 'Nissan 370Z', 'Chevrolet Camaro ZL1', 'Ford Bronco Sport', 'Audi S4', 'Volkswagen Passat', 
    'Toyota C-HR', 'Lexus LS', 'Ford F-150 Lightning', 'Mazda 2', 'Kia K900', 'Hyundai Sonata Hybrid', 'Jeep Renegade', 
    'Toyota Sequoia TRD Pro', 'Dodge Journey', 'Buick Encore', 'Ford Mustang Shelby GT500', 'Chevrolet Colorado WT',
    'Chevrolet Silverado Z71', 'Mazda 5', 'Nissan Versa', 'Hyundai Sonata', 'Lexus RX 350', 'Nissan Leaf SV', 
    'BMW X1', 'Dodge Durango SRT', 'Subaru Ascent', 'Honda Civic LX', 'Chevrolet Blazer', 'Ford Transit Connect', 
    'Toyota Tacoma TRD Off-Road', 'Ram 2500 Power Wagon', 'Tesla Model X Performance', 'Kia Soul EV', 'Lexus GX 460',
    'Chevrolet Malibu Premier', 'Ford Edge ST', 'Toyota Sienna Hybrid', 'Buick Envision', 'Jeep Compass', 'Toyota Prius Prime',
    'Hyundai Santa Fe XL', 'Ford Focus Electric', 'Cadillac XT5', 'Chevrolet Silverado 3500HD', 'Tesla Model 3 Long Range',
    'Honda Clarity', 'BMW i4', 'Mazda MX-30', 'Nissan Maxima', 'Ford Fusion Energi', 'Toyota Highlander Hybrid', 
    'Hyundai Ioniq Hybrid', 'GMC Terrain Denali', 'Nissan Leaf Plus', 'Chevrolet Bolt EUV', 'Audi Q3', 'Subaru Impreza',
    'BMW 2 Series', 'Honda HR-V Sport', 'Ford Escape Hybrid', 'Hyundai Kona Electric', 'Kia Sorento Hybrid', 
    'Ram 1500 Laramie', 'Chevrolet Traverse Premier', 'Toyota Avalon Hybrid', 'Mazda CX-3', 'Lexus UX 250h', 
    'Subaru Outback Wilderness', 'Ford F-150 Platinum', 'Chevrolet Trailblazer', 'Dodge Charger SRT', 'Chevrolet Traverse RS',
    'Hyundai Tucson Hybrid', 'Jeep Cherokee Trailhawk', 'Tesla Model Y Performance', 'Nissan Murano Platinum', 
    'Cadillac Escalade ESV', 'Honda Accord Hybrid', 'Buick Cascada', 'Ford Mustang Mach-E GT', 'Toyota Prius V', 
    'Chevrolet Silverado Custom', 'Hyundai Elantra N', 'Ram 3500 Laramie', 'Volkswagen Golf R', 'Honda Civic Touring',
    'GMC Canyon Denali', 'Jeep Renegade Trailhawk', 'Kia Niro EV', 'Chrysler 300 Limited', 'Ford Edge Titanium', 
    'BMW X6', 'Chevrolet Tahoe Z71', 'Nissan Pathfinder', 'Toyota Land Cruiser 70', 'Honda Accord Sport', 'Hyundai Ioniq 5',
    'Ram 2500 Tradesman', 'Ford F-150 Tremor', 'Chevrolet Malibu Hybrid', 'Mazda CX-7', 'Kia Sportage', 'Chrysler Pacifica Hybrid',
    'Nissan Juke Nismo', 'Chevrolet Bolt', 'Subaru Crosstrek Hybrid', 'Audi Q8', 'GMC Sierra 2500HD', 'Jeep Cherokee Latitude',
    'Lexus RX 450h', 'Ford F-150 King Ranch', 'Nissan Rogue SV', 'Chevrolet Traverse LT', 'Hyundai Elantra GT', 'Ford Explorer ST']

# Physical Appearance
hair_color = ['Black', 'Brown', 'Blonde', 'Auburn', 'Red', 'Chestnut', 'Gray', 'White']
eyes_color = ['Brown', 'Amber', 'Hazel', 'Green', 'Blue', 'Gray']
blood_type = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

# Personality
religion = ['Christianity', 'Islam', 'Hinduism', 'Buddhism', 'Judaism', 'Sikhism', 'Bahá\'í Faith', 'Shinto',
    'Confucianism', 'Jainism', 'Taoism', 'Zoroastrianism', 'Paganism', 'Atheism', 'Agnosticism', 
    'Unitarian Universalism', 'Church of Scientology', 'Rastafarianism', 'Wicca', 'Shamanism', 
    'Baha\'i Faith', 'New Age Spirituality', 'Humanism', 'Deism', 'Pastafarianism']
favorite_color = ['Red', 'Yellow', 'Green', 'Cyan', 'Blue', 'Magenta', 'Violet', 'Rose', 'Azure', 'Spring green', 'Chartreuse', 'Orange']
political_side = ['Democratic Part (Left-wing/Progressive)', 'Republican Party (Right-wing Conservative)', 'Libertarian Party (Lbertarianism)', 'Green Party (Environment/Progressivism)', 'Constitution Party (Conservatism/Traditionalism)', 'Socialist Party USA (Socialism)', 'Independent (Unaffiliated)', 'Progressive Movement (Progressivism)', 'Tea Party Movement (Conservatism)', 'Alt-right (Far-right)', 'Anarchism (Anarchist Movement)', 'Democratic Socialist Movement']
favorite_animals = ['Dog', 'Cat', 'Elephant', 'Tiger', 'Lion', 'Dolphin', 'Horse', 'Penguin', 'Koala', 'Kangaroo',
    'Panda', 'Giraffe', 'Monkey', 'Bear', 'Wolf', 'Eagle', 'Gorilla', 'Zebra', 'Cheetah', 'Horse',
    'Parrot', 'Rabbit', 'Turtle', 'Snake', 'Fox', 'Owl', 'Sloth', 'Shark', 'Whale', 'Otter',
    'Raccoon', 'Alligator', 'Horse', 'Bat', 'Bat', 'Lizard', 'Dragonfly', 'Peacock', 'Flamingo',
    'Leopard', 'Crow', 'Bee', 'Duck', 'Frog', 'Bison', 'Pigeon', 'Chicken', 'Swan', 'Bat',
    'Mole', 'Bald Eagle', 'Beaver', 'Cheetah', 'Mole', 'Deer', 'Squirrel', 'Buffalo', 'Lynx',
    'Jaguar', 'Tiger', 'Albatross', 'Horse', 'Ostrich', 'Aardvark', 'Platypus', 'Swan', 'Rhino',
    'Hippopotamus', 'Anteater', 'Llama', 'Yak', 'Chameleon', 'Crab', 'Penguin', 'Dingo', 'Raven',
    'Armadillo', 'Starfish', 'Seahorse', 'Gecko', 'Camel', 'Moose', 'Rattlesnake', 'Toucan', 'Vulture',
    'Skunk', 'Wombat', 'Woodpecker', 'Coyote', 'Meerkat', 'Mantis', 'Squid', 'Elephant Seal',
    'Seal', 'Manatee', 'Pufferfish', 'Dromedary', 'Sea Lion', 'Pelican', 'Marmot', 'Chipmunk', 'Octopus']
favorite_seasons = ['Spring', 'Summer', 'Autumn', 'Fall', 'Winter']
favorite_cereals = ['Frosted Flakes', 'Cheerios', 'Lucky Charms', 'Cinnamon Toast Crunch', 'Cap\'n Crunch', 'Honey Nut Cheerios',
    'Raisin Bran', 'Fruity Pebbles', 'Cornflakes', 'Coco Pebbles', 'Special K', 'Reese\'s Puffs', 'Kix', 'Frosted Mini Wheats',
    'Rice Krispies', 'Quaker Oatmeal', 'Shredded Wheat', 'Trix', 'Grape Nuts', 'Wheaties', 'Count Chocula',
    'Apple Jacks', 'Life Cereal', 'Golden Grahams', 'Honey Bunches of Oats', 'Cocoa Krispies', 'Post Selects',
    'Peanut Butter Crunch', 'Chex', 'Corn Pops', 'Cheerios (Apple Cinnamon)', 'Crave', 'Malt-O-Meal', 'Grape-Nuts Flakes',
    'Sugar Smacks', 'Oatmeal Crisp', 'Smart Start', 'Puffed Rice', 'Puffed Wheat', 'Waffle Crisp', 'Crispix', 'Froot Loops']
favorite_foods = ['Hamburger', 'Pizza', 'Hot Dog', 'Fried Chicken', 'Mac and Cheese', 'Tacos', 'Burritos', 'Spaghetti',
    'Steak', 'Ribs', 'Chicken Wings', 'Cheeseburger', 'Sandwich', 'French Fries', 'Pasta', 'BBQ',
    'Donuts', 'Apple Pie', 'Ice Cream', 'Pancakes', 'Waffles', 'Grilled Cheese', 'Caesar Salad', 'Poke Bowl',
    'Nachos', 'Bagels', 'Buffalo Wings', 'Chili', 'Clam Chowder', 'Philly Cheesesteak', 'Potato Salad', 'Cornbread',
    'Fried Shrimp', 'Tater Tots', 'Popcorn', 'Sushi', 'Lobster Roll', 'Eggs Benedict', 'Chocolate Cake',
    'Cupcakes', 'Cheese Fries', 'Beef Tacos', 'Chicken Parmesan', 'Quesadillas', 'Corn on the Cob', 'Cobb Salad',
    'Jambalaya', 'Meatloaf', 'Cornbread', 'Pork Ribs', 'Gravy', 'Baked Potato', 'Cinnamon Rolls', 'Pasta Salad',
    'Muffins', 'Mashed Potatoes', 'Pasta Primavera', 'Roast Beef', 'Sliders', 'Lobster Bisque', 'Bacon',
    'Sausage', 'Pot Roast', 'Fried Green Tomatoes', 'Chicken Fried Steak', 'Po Boy Sandwich', 'Ramen',
    'Bagel with Lox', 'BLT Sandwich', 'Brisket', 'Rice Pudding', 'Cheesecake', 'S’mores', 'Banana Bread',
    'Tiramisu', 'Margarita Pizza', 'Pecan Pie', 'Peach Cobbler', 'Chocolate Chip Cookies', 'Pasta Alfredo',
    'Tuna Salad', 'Minestrone Soup', 'Beef Stew', 'Gravy', 'Shrimp Cocktail', 'Mushroom Risotto',
    'Roast Chicken', 'Baked Ziti', 'Chicken Tenders', 'Lamb Chops', 'Churros', 'Fish and Chips', 'Peking Duck',
    'Beef Burritos', 'Pulled Pork Sandwich', 'Chicken and Dumplings', 'Baked Beans', 'Peking Duck', 'Pasta Bolognese']
email_providers = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'aol.com', 'protonmail.com',
    'zoho.com', 'mail.com', 'yandex.com', 'gmx.com', 'comcast.net', 'me.com', 'msn.com', 'mail.ru', 
    'live.com', 'rocketmail.com', 'fastmail.com', 'tutanota.com', 'hushmail.com', 'inbox.com', 
    'rediffmail.com', 'yahoo.co.uk', 'gmx.de', 'virmail.com', 'bluebottle.com', 'mailchimp.com', 
    'mac.com', 'seznam.cz', 'gawab.com', 'lycos.com', 'cableone.net', 'shaw.ca', 'virginmedia.com',
    'sbcglobal.net', 'att.net', 'earthlink.net', 'juno.com', 'netzero.net', 'optimum.net', 'bell.net',
    'cox.net', 'charter.net', 'fuse.net', 'epix.net', 'frontier.com', 'rcn.com', 'windstream.net',
    'mailinator.com', 'temp-mail.org', 'guerrillamail.com', '10minutemail.com', 'yopmail.com', 
    'dispostable.com', 'trashmail.com', 'spambox.us', 'spamex.com', 'maildrop.cc', 'throwawaymail.com',
    'spamgourmet.com', 'mailcatch.com', 'getnada.com', 'tempinbox.com', 'dodgit.com', 'fakeinbox.com',
    'mailnesia.com', 'inbox.lv', 'simplicmail.com', 'zapto.org', 'myself.com', 'tutanota.de', 'mailfence.com']

def choose_gender():
    gender_choice = input("[!] Please choose a gender (Male/Female): ")
    if gender_choice == "Male":
        gender = "Male"
    elif gender_choice == "Female":
        gender = "Female"
    else:
        print("[ERROR] Invalid choice! Please select 'Male' or 'Female'.")
        return choose_gender()
    return gender
chosen_gender = choose_gender()
print(f"[INFO] The selected gender is: {chosen_gender}")

def generate_random_birthday():
    today = datetime.today()
    age_range_start = 18
    age_range_end = 100
    age = random.randint(age_range_start, age_range_end)
    birth_year = today.year - age
    random_month = random.randint(1, 12)
    days_in_month = [31, 29 if (birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    random_day = random.randint(1, days_in_month[random_month - 1])
    random_birthday = datetime(birth_year, random_month, random_day)
    return random_birthday, age
birthday, age = generate_random_birthday()

def get_random_item(item_list):
    return random.choice(item_list)

def generate_driver_license():
    state = random.choice(states)
    number_length = random.randint(7,9)
    number = ''.join(random.choices(string.digits, k=number_length))
    letter_suffix = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 2)))
    license_number = f"{state}-{number}-{letter_suffix}"
    return license_number
random_license = generate_driver_license() 
    
def generate_random_address():
    state = random.choice(states)
    city = random.choice(cities)
    street_number = random.randint(100, 9999)
    street_name = random.choice(street_names)
    street_address = f"{street_number} {street_name} St."
    zip_code = random.randint(10000, 99999)
    address = f"{street_address} {city}, {state} {zip_code}"
    return address
random_address = generate_random_address()

def generate_random_person():
    if chosen_gender == 'Male':
        first_name = get_random_item(first_names_male)
        middle_name = get_random_item(male_middle_names)
    else:
        first_name = get_random_item(first_names_female)
        middle_name = get_random_item(female_middle_names)
    last_name = get_random_item(last_names)
    full_name = f"{first_name} {middle_name} {last_name}"
    return {
        print("\n====PERSONAL INFORMATION===="),
        print(f"Name: {full_name}"),
        print(f"Gender: {chosen_gender}"),
        print(f"Birthday: {birthday.strftime('%B %d, %Y')} (Age: {age})"),
        print(f"Birthplace: {get_random_item(cities)}, USA"),
        print(f"Phone: ({random.randint(100,999)})-{random.randint(200,999)}-{random.randint(1000,9999)}"),
        print(f"Social Security Number (SSN): {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000,9999)}"),
        print(f"Address: {random_address}"),
        print(f"Ziodiac sign: {get_random_item(ziodiac_sign)}"),
        print(f"E-mail: {first_name.lower()}{last_name.lower()}@{get_random_item(email_providers)}"),
        print(f"Driver license: {random_license}"),
        print(f"Car: {get_random_item(car)}"),
        print('\n====PHYSICAL APPEARANCE===='),
        print(f"Hair color: {get_random_item(hair_color)}"),
        print(f"Eyes color: {get_random_item(eyes_color)}"),
#        print(f"Height: {random.randint(0, 1)}, {random.ranadint(0, 99)}"),
        print(f"Weight: {random.randint(45, 100)}kg"),
        print(f"Shoe size: {random.randint(5, 20)}"),
        print(f"Blood type: {get_random_item(blood_type)}"),
        print('\n====PERSONALITY===='),
        print(f"Religion: {get_random_item(religion)}"),
        print(f"Political side: {get_random_item(political_side)}"),
        print(f"Favorite color: {get_random_item(favorite_color)}"),
        print(f"Favorite cereal: {get_random_item(favorite_cereals)}"),
        print(f"Favorite season: {get_random_item(favorite_seasons)}"),
        print(f"Favorite animal: {get_random_item(favorite_animals)}"),
        print(f"Lucky number: {random.randint(0, 99)}")
    }

person = generate_random_person()
print(person)
