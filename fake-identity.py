import random

first_names_male = ['Liam', 'Noah', 'Oliver', 'James', 'Elijah', 'Mateo', 'Theodore', 'Henry', 'Lucas', 'William', 'Benjamin', 'Levi', 'Sebastian', 'Jack', 'Ezra', 'Michael', 'Daniel', 'Leo', 'Owen', 'Samuel', 'Hudson', 'Alexander', 'Asher', 'Luca' 'Ethan', 'John', 'David', 'Jackson', 'Joseph', 'Mason', 'Luke', 'Matthew', 'Julian', 'Dylan', 'Elias', 'Jacob', 'Maverick', 'Gabriel', 'Logan', 'Aiden', 'Thomas', 'Isaac', 'Miles', 'Grayson', 'Santiago', 'Anthony', 'Wyatt', 'Carter', 'Jayden', 'Ezekiel', 'Caleb', 'Cooper', 'Josiah', 'Charles', 'Christopher', 'Isaiah', 'Nolan', 'Cameron', 'Nathan', 'Joshua', 'Kai', 'Waylon', 'Angel', 'Lincoln', 'Andrew', 'Roman', 'Adrian', 'Aaron', 'Wesley', 'Ian', 'Thiago', 'Axel', 'Brooks', 'Bennett', 'Weston', 'Rowan', 'Christian', 'Theo', 'Beau', 'Eli', 'Silas', 'Jonathan', 'Ryan', 'Leonardo', 'Walker', 'Jaxon', 'Micah', 'Everett', 'Robert', 'Enzo', 'Parker', 'Jeremiah', 'Jose', 'Colton', 'Luka', 'Easton', 'Landon', 'Jordan', 'Amir', 'Gael']
first_names_female = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Sophia', 'Mia', 'Isabella', 'Ava', 'Evelyn', 'Luna', 'Harper', 'Sofia', 'Camila', 'Eleanor', 'Elizabeth', 'Violet', 'Scarlett', 'Emily', 'Hazel', 'Lily', 'Gianna', 'Aurora', 'Penelope', 'Aria', 'Nora', 'Chloe', 'Ellie', 'Mila', 'Avery', 'Layla', 'Abigail', 'Ella', 'Isla', 'Eliana', 'Nova', 'Madison', 'Zoe', 'Ivy', 'Grace', 'Lucy', 'Willow', 'Emilia', 'Riley', 'Naomi', 'Victoria', 'Stella', 'Elena', 'Hannah', 'Valentina', 'Maya', 'Zoey', 'Delilah', 'Leah', 'Lainey', 'Lillian', 'Paisley', 'Genesis', 'Madelyn', 'Sadie', 'Sophie', 'Leilani', 'Addison', 'Natalie', 'Josephine', 'Alice', 'Ruby', 'Claire', 'Kinsley', 'Everly', 'Emery', 'Adeline', 'Kennedy', 'Maeve', 'Audrey', 'Autumn', 'Athena', 'Eden', 'Iris', 'Anna', 'Eloise', 'Jade', 'Maria', 'Caroline', 'Brooklyn', 'Quinn', 'Aaliyah', 'Vivian', 'Liliana', 'Gabriella', 'Hailey', 'Sarah', 'Savannah', 'Cora', 'Madeline', 'Natalia', 'Ariana', 'Lydia', 'Lyla', 'Clara', 'Allison']
last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
midle_name = ['test']
#birthplace = ['test']
ziodiac_sign = ['Ram', 'Bull', 'Twins', 'Crab', 'Lion', 'Virgin', 'Balance', 'Scorpion', 'Archer', 'Goat', 'Water Bearer', 'Fish']
gender = ['Male', 'Female']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
#car = ['test']

for male_person in range(1):
    first = random.choice(first_names_male)
    midle_name = random.choice(midle_name)
    last = random.choice(last_names)
    bday = f'{random.randint(1,30)}dd, {random.randint(1, 12)}mm, {random.randint(1500,2024)}'
    gender = 'Male'
    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'
    ssn = random.randint(000000000, 999999999)
    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    zodiac = random.choice(ziodiac_sign)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'
    email = f'{first}{last}@gmail.com'
    driver_license = f'A{random.randint(0000000, 9999999)}'
#    print('=========PHYSICAL APPEARANCE=====')
#    hair_color = 
#    eyes_color = 
#    height = 
#    weight =
#    shoe_size =
#    blood_type = 
#    print('=========PERSONALITY==============')
#    religion = 
#    political_side =
#    favorite_color = 
#    favorite_food = 
#    favorite_cereal = 
#    favorite_season = 
#    favorite_animle =
#    lucky_number = 
#    print('US CAR ') #(https://www.businer.com/uscarlicenseplates.php)
    print(f'{first} {midle_name} {last}\n{bday}\n{zodiac}\n{gender}\n{phone}\n{address}\n{ssn}\n{email}\n{driver_license}\n')