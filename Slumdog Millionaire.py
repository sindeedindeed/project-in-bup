questions = [
[
    "What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "None", 3
],
[
    "Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "None", 2
],
[
    "How many continents are there in the world?", "5", "6", "7", "8", "None", 3
],
[
    "What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "None", 4
],
[
    "Which animal is known as the 'King of the Jungle'?", "Tiger", "Elephant", "Lion", "Giraffe", "None", 3
],
[
    "What is the boiling point of water?", "90°C", "100°C", "110°C", "120°C", "None", 2
],
[
    "Who is known as the 'Father of Computers'?", "Albert Einstein", "Isaac Newton", "Charles Babbage", "Thomas Edison", "None", 3
],
[
    "What is the hardest natural substance on Earth?", "Gold", "Silver", "Iron", "Diamond", "None", 4
],
[
    "What is the national currency of Japan?", "Dollar", "Euro", "Peso", "Yen", "None", 4
],
[
    "Which planet is known as the Earth’s twin?", "Mars", "Venus", "Jupiter", "Saturn", "None", 2
],
[
    "In which year did World War II end?", "1940", "1920", "1945", "1925", "None", 3
],
[
    "Which language has the most native speakers in the world?", "English", "French", "Mandarin", "Bangla", "None", 3
],
[
    "What is the longest river in the world?", "Amazon River", "Yangtze River", "Missisippi River", "Nile River", "None", 4
],
[
    "Which is the only metal that is liquid at room temperature?", "Mercury", "Gallium", "Sodium", "Cesium", "None", 2
],
[
    "Which ancient civilization built the Machu Picchu complex in Peru?", "Aztecs", "Mayans", "Olmecs", "Incas", "None", 4
],
[
    "What is the largest desert in the world?", "Arabian Desert", "Antarctic Desert", "Sahara DEsert", "Gobi Desert", "None", 2
],
[
    "What is the main ingredient in the Japanese dish 'miso soup'?", "Seaweed", "Tofu", "Soybean paste", "Rice", "None", 3
],
[
    "In what year did the Titanic sink?", "1905", "1910", "1912", "1920", "None", 3
],
[
    "Who is credited with inventing the World Wide Web?", "Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Tim Berners-Lee", "None", 4
],
[
    "Which ancient city is known for the legendary Hanging Gardens?", "Alexandria", "Athens", "Babylon", "Nineveh", "None", 3
],
[
    "What is the only country in the world with no official capital?", "Monaco", "Finland", "Nauru", "San Marino", "None", 3
],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000, 2560000, 3050000, 5050000, 10000000, 2000000, 4000000, 70000000]
money = 0

for i in range(0,len(questions)):

    question = questions[i]
    print(f"\nQuestion for Bdt. {levels[i]}:")
    print(f"\n{question[0]}")
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")
    reply = int(input("\nEnter your answer (1-4) or 0 to quit "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct Answer! You have won Bdt. {levels[i]}")
        if (i == 4):
            money = 10000
        elif(i == 9):
            money = 320000    
        elif(i == 14):
            money = 10000000
        elif(i == 19):
            money = 70000000
    else:
        print("Wrong Answer!")
        break


print(f"\nBetter Luck next time!")
print(f"Your take money home is {money}!")
print(" ")