# 1.0 Fake ID Generator
## 1.1 Introduction
This repository is designed to allow a python3 script to generate a randomized fake IDs, producing identification details that closely mimic real-world ID formats.
The generated IDs are entirely fictitious and do not contain any real or personal information.
This tool is invaluable for **developers**, **testers**, and **data scientists** who need realistic yet fake data for applications, testing environments, or simulations. It is particularly useful for generating mock data in situations where real user information is either unsuitable or unavailable, maintaining privacy and anonymity in the process.

>[!IMPORTANT]
> This script generates random first names, last names, addresses, and other personal details, based on common formats used in the United States.

## 1.2 Features Overview
- **1000+ American names, middle names and last names**:  
  The script includes a curated list of over 1,000 male and female names with last names, sourced from reputable references for accuracy. <sub>**Source:** [1,000 boy names in the U.S](https://www.parents.com/top-1000-baby-boy-names-2757618), [1,000 girl names in the U.S](https://www.parents.com/top-1000-baby-girl-names-2757832), [1,000 most common surnames in the U.S](https://probablyhelpful.com/most_common_surnames.htm)</sub>
- **Random date of birth (DOB)**:  
  The script generate a random date of birth that are including the month, day, and year. It also calculates the current age.
- **Random real address**:  
  The script generates random real addresses, including street names, cities, and zip codes. The dataset are retrieved using the api of [overpass](https://overpass-turbo.eu/). <sub>**Source:** [overpass turbo](https://overpass-turbo.eu/)</sub>
  <details>

  <summary>The script supports only the following cities in the U.S:</summary>

  - [X] Chicago

  </details>
- **Random height and weight**:  
  The script generates random height and weight.
- **Random eyes and hair color**:  
  The script generate a random color that are assigned to your fake identity
- **Random birthplace**:  
  The script generates random cities that are assigned as the birthplace for your fake identity.
- **Random bloodtype**:  
  The script generates a random blood type.
- **Random zodiac sign**:  
  The script generate a zodiac sign.
- **Random religion**:  
  The script generate a religion.
- **Random favorite color, animal, food, number**:  
  The script generates a favorite color, animal, food, and number, all assigned to your fake identity.
- **Random e-mail**:  
  The script generates a random, non-functional email address.
- **Random phone number**:  
  The script generates a random, unusable phone number.
- **Random political side**:  
  The script generates a random political affiliation that is assigned to your fake identity.
  
# 2.0 I/O Interface
## 2.1 Usage
```bash
user@Fake-ID:~/Desktop$ git clone https://github.com/Pv0t/Fake-ID.git
user@Fake-ID:~/Desktop$ cd Fake-ID
user@Fake-ID:~/Desktop/Fake-ID$ python3 fakeID.py
```

## 2.2 Output

![fakeID](https://github.com/user-attachments/assets/f84e9ff0-6161-4737-98f8-484dfb914269)

----
>[!WARNING]
>## Warning & Disclaimer:
>**This script is intended solely for educational purposes or legitimate testing scenarios.** The creation of fake IDs for fraudulent, deceptive, or illegal activities is both unethical and illegal. The generated data is for use in controlled environments only and should not be used for unlawful purposes.
