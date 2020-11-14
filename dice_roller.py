import random
def main():



  dice_rolls =2*int(input('How many dice each player want to roll? '))
  dice_size = int(input('How many sides are the dice? '))

  team1 = input('Enter First Team name: ')
  team2 = input('Enter second Team name: ')

  team1_dice_sum = 0
  team2_dice_sum = 0

  team1_rolls=[]
  team2_rolls=[]

  for i in range(0, dice_rolls):

    roll = random.randint(1, dice_size)
    if (i % 2) == 0:
      team1_dice_sum += roll
      team1_rolls.append(team1_dice_sum)
      if roll == 1:
        print(f'{team1} rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'{team1} rolled a {roll}! Critical Success!')
      else:
        print(f'{team1} rolled a {roll}')    
      print(f'{team1} rolled a sum of {team1_dice_sum}')

    else:
      team2_dice_sum += roll
      team2_rolls.append(team2_dice_sum)
      if roll == 1:
        print(f'{team2} rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'{team2} rolled a {roll}! Critical Success!')
      else:
        print(f'{team2} rolled a {roll}')    
      print(f'{team2} rolled a sum of {team2_dice_sum}')      


  print(f'{team1} rolls sum are: {team1_rolls}')
  print(f'{team2} rolls sum are: {team2_rolls}')

if __name__== "__main__":
  main()