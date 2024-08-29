# import random
# lifes=5
# while lifes>0:
#     res=random.randint(1,100)
#     a=int(input())
#     if a==res:
#         print("You Winn!")
#         break
#     if a>res:
#         print(f"Too high \nlifes:{lifes}")
#     elif a<res:
#         print(f"Too low \nlifes: {lifes}")
#     elif abs(a-res)==1 or abs(res-a)==1:
#         print("Too closer")
#     lifes-=1
#     if lifes==0:
#         print(f"Game Over!\n{res}")

# import random
# lst1 = [random.randint(0, 1) for i in range(5)]
# lst2 = [random.randint(0, 1) for i in range(5)]
# print(lst1)
# print(lst2)
# res=lst1==lst2
# print(res)

# import random
# letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits='0123456789'
# punctuation='!@#$%^&*()-_=+[]{}|;:,.<>?/'
# characters=letters+digits+punctuation
# cnt=int(input())
# password=''
# for i in range(cnt):
#     password += random.choice(characters)
# print(password)

# import random
# choices=["rock", "paper", "scissors"]
# def test(player, computer):
#     if player==computer:
#         return "It's a tie!"
#     elif (player == "rock" and computer == "scissors") or \
#          (player == "paper" and computer == "rock") or \
#          (player == "scissors" and computer == "paper"):
#         return "You win!"
#     else:
#         return "You lose!"
# while True:
#     print("Select your move: 1 - rock, 2 - paper, 3 - scissors")
#     player_choice = int(input("You chose: ")) - 1
#     computer_choice = random.choice(choices)
#     print(f"You chose: {choices[player_choice]}")
#     print(f"Computer chose: {computer_choice}")
#     result = test(choices[player_choice], computer_choice)
#     print(result)
