import random
dis = ['blind', 'deaf', 'missing limbs']
sit = ['applying for a job at Google', 'applying to be an athlete', 'asking for a raise']
his = ['volunteers at community events', 'works diligently', 'has a history of misbehavior', 'cheats in competitions', 'misplaces documents frequently', 'sometimes hands in work late']
dis1 = random.choice(dis)
heal = random.choice(his)

disperson =  dis1 + ' but very smart.'
healthy = 'completely healthy and ' + heal
situation = random.choice(sit)
print('Two people are both ' + situation + '.')
print('The first person is ' + disperson)
print('The second person is ' + healthy + '.')
a = input('Who do you choose? (1 for first and 2 for second) ')

if situation == sit[0] and a == '1':
    if heal == his[1]:
        print('This was a hard choice! It would depend on who you think is more suited for the job.')
    elif heal == his[0]:
        print('You made a hard choice. However, it is correct, because a job at Google would need knowledge.')
    else:
        print('You made the right choice(in our opinions)')
if situation == sit[0] and a =='2':
    print("We think you are incorrect. If you think otherwise, that's okay too!")



if situation == sit[1] and a == '1':
    print("It would be very hard for a person with any kind of disability to become an athlete. Not all the answers in this game are 1!")
if situation == sit[1] and a == '2':
    print("You're right! A healthy person would be a better athlete.")



if situation == sit[2] and a == '1':
    if not (heal == his[1] or heal == his[0]):
        print("You're right, bad behavior does not deserve a raise.")
    elif heal == his[0]:
        print("Volunteering doesn't necessarily mean a person deserves a raise, but we'll take it that.")
    else:
        print("Diligent work should be rewarded with a raise, even if they are healthier.")
if situation == sit[2] and a == '2':
    if heal == his[1]:
        print("You're right! Diligent work should be rewarded.")
    else:
        print('We think the other person should get the raise.')

print('----------------------------------------------')
print('The takeaway: Be fair, but make sure that you are being reasonable!')
