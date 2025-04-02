import random

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
    'Vivian', 'Kaitlyn', 'Avery', 'Lily', 'Emma', 'Mackenzie', 'Reagan', 'Sarah', 'Hannah', 'Paige', 'Josephine'
]
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
    'Nichols', 'O’Neill', 'Spencer', 'Matthews', 'Diaz', 'Harris', 'Willis', 'Mcdonald', 'Williamson'
]
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
    'Damien', 'Derrick', 'Randy', 'Chad', 'Lamar', 'Cameron', 'Jeffrey', 'Colton', 'Lee', 'Reid', 'Mitchell', 'Dustin'
]
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
    'Caroline', 'Taylor', 'Marissa', 'Ruth', 'Emily', 'Mila', 'Mariana', 'Adeline', 'Catherine', 'Lydia'
]
#birthplace = ['test']
ziodiac_sign = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 
    'Capricorn', 'Aquarius', 'Pisces'
]
gender = ['Male', 'Female']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
#car = ['test']
##############====PHYSICAL APPEARANCE==========##########
hair_color = ['Black', 'Brown', 'Blonde', 'Auburn', 'Red', 'Chestnut', 'Gray', 'White']
eyes_color = ['Brown', 'Amber', 'Hazel', 'Green', 'Blue', 'Gray']
blood_type = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
#############====PERSONALITIES=============#############
religion = ['Buddhism', 'Christianity', 'Confucianism', 'Hinduism', 'Islam', 'Jainism', 'Judaism', 'Sikhism', 'Taoism', 'Unaffiliated']
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
    'Seal', 'Manatee', 'Pufferfish', 'Dromedary', 'Sea Lion', 'Pelican', 'Marmot', 'Chipmunk', 'Octopus'
]
favorite_seasons = ['Spring', 'Summer', 'Autumn', 'Fall', 'Winter'
]
favorite_cereals = ['Frosted Flakes', 'Cheerios', 'Lucky Charms', 'Cinnamon Toast Crunch', 'Cap\'n Crunch', 'Honey Nut Cheerios',
    'Raisin Bran', 'Fruity Pebbles', 'Cornflakes', 'Coco Pebbles', 'Special K', 'Reese\'s Puffs', 'Kix', 'Frosted Mini Wheats',
    'Rice Krispies', 'Quaker Oatmeal', 'Shredded Wheat', 'Trix', 'Grape Nuts', 'Wheaties', 'Count Chocula',
    'Apple Jacks', 'Life Cereal', 'Golden Grahams', 'Honey Bunches of Oats', 'Cocoa Krispies', 'Post Selects',
    'Peanut Butter Crunch', 'Chex', 'Corn Pops', 'Cheerios (Apple Cinnamon)', 'Crave', 'Malt-O-Meal', 'Grape-Nuts Flakes',
    'Sugar Smacks', 'Oatmeal Crisp', 'Smart Start', 'Puffed Rice', 'Puffed Wheat', 'Waffle Crisp', 'Crispix', 'Froot Loops'
]
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
    'Beef Burritos', 'Pulled Pork Sandwich', 'Chicken and Dumplings', 'Baked Beans', 'Peking Duck', 'Pasta Bolognese'
]

for male_person in range(1):
    output_first_names_male = random.choice(first_names_male)
    output_middle_name = random.choice(male_middle_names)
    output_last_names = random.choice(last_names)
    output_bday = f'{random.randint(1,30)}dd, {random.randint(1, 12)}mm, {random.randint(1500,2024)}'
    output_gender = 'Male'
    output_phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'
    output_ssn = random.randint(000000000, 999999999)
    output_street_num = random.randint(100, 999)
    output_street = random.choice(street_names)
    output_city = random.choice(fake_cities)
    output_state = random.choice(states)
    output_zip_code = random.randint(10000, 99999)
    output_zodiac = random.choice(ziodiac_sign)
    output_address = f'{output_street_num} {output_street} St., {output_city} {output_state} {output_zip_code}'
    output_email = f'{output_first_names_male.lower()}{output_last_names.lower()}@gmail.com'
    output_driver_license = f'A{random.randint(0000000, 9999999)}'
    # =========PHYSICAL APPEARANCE=====
    output_hair_color = random.choice(hair_color)
    output_eyes_color = random.choice(eyes_color)  
    output_height =  f'{random.randint(0, 1), random.randint(0, 99)}'
    output_weight = random.randint(45, 100)
#    shoe_size =
    output_blood_type = random.choice(blood_type)
#   =========PERSONALITIES==============
    output_religion = random.choice(religion)
    output_political_side = random.choice(political_side)
    output_favorite_color = random.choice(favorite_color)
    output_favorite_food = random.choice(favorite_foods)
    output_favorite_cereal =  random.choice(favorite_cereals)
    output_favorite_season = random.choice(favorite_seasons)
    output_favorite_animal = random.choice(favorite_animals)
    output_lucky_number = random.randint(0, 99)
#    print('US CAR ') #(https://www.businer.com/uscarlicenseplates.php)
    print(f'Name: {output_first_names_male}\nMiddle Name: {output_middle_name}\nLast Name: {output_last_names}\nBirthday: {output_bday}\nZodiac Sign: {output_zodiac}\nGender: {output_gender}\nPhone: {output_phone}\nAddress: {output_address}\nSocial Security Number (SSN): {output_ssn}\nE-mail: {output_email}\nDriver license: {output_driver_license}\n')
    print('=====PHYSICAL APPERANCE====')
    print(f'Hair color: {output_hair_color}\nEyes color: {output_eyes_color}\nHeight: {output_height}\nWeight: {output_weight}\nBlood Type: {output_blood_type}')
    print('====PERSONALITIES====')
    print(f'Religion: {output_religion}\nPolitical Side: {output_political_side}\nFavorite Color: {output_favorite_color}\nFavorite Food: {output_favorite_food}\nFavorite Animal: {output_favorite_animal}\nLucky Number: {output_lucky_number}')
