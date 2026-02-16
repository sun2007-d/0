import streamlit as st
st.title('volley game')
import random

import time
class Scoreboard:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0

    def add_score(self,team, point=1,):
        if team == 'A':
            self.score1 += point
        if team == 'B':
            self.score2 += point

    def reset(self):
        self.score1 = 0
        self.score2 = 0

    def show_score(self):
        print(f"team A vs team B: {self.score1} / {self.score2}")
board = Scoreboard()


a1 = 1
a2 = 1
serveA=0
serveB=0
defenceA=0
defenceB=0
setA=0
setB=0
attackA=0
attackB=0
character='S'





print("请B队分配点数，你一共有15点，满分五分")
print("需分配给 发球 防守 二传 进攻")

while True:
    serveB_str=input("发球：")
    serveB=int(serveB_str)
    if not serveB_str.isdigit() :
        print("请重新输入：")
        continue
    if serveB not in [0,1,2,3,4,5,]:
        print("请重新输入：")
        continue
    break


while True:
    print(f"还有{15-serveB}点数没有用")
    defenceB_str=input("防守：")
    defenceB=int(defenceB_str)
    if not defenceB_str.isdigit() :
        print("请重新输入：")
        continue
    if defenceB not in [0,1,2,3,4,5,]:
        print("请重新输入：")
        continue
    break
while True:
    print(f"还有{15-serveB-defenceB}点数没有用")
    setB_str=input("二传：")
    setB=int(setB_str)
    if not setB_str.isdigit() :
        print("请重新输入：")
        continue
    if setB not in [0,1,2,3,4,5,]:
        print("请重新输入：")
        continue


    print(f"进攻剩余点数为{15-serveB-defenceB-setB}")
    attackB=15-serveB-defenceB-setB
    attackB_str=str(attackB)
    if not attackB_str.isdigit() :
        print("请重新输入：")
        continue
    if attackB not in [0,1,2,3,4,5,]:
        print("请重新输入：")
        continue
    break
print("请B队选择拦网战术：")
while True:
    print("1-集中式拦网")
    print("2-双边拦网")
    print("3-盯人拦网")
    choice = input("请输入选项数字：")
    if choice in ["1", "2", "3"]:
        if choice == "1":
            blockpositionB = random.sample(range(2, 11), 3)
            break
        elif choice == "2":
            blockpositionB = [2, 3, 9, 10] + random.sample(range(4, 9), 1)
            break



        elif choice == "3":
            print("请选择盯防人员：")
            print("1-主攻")
            print("2-副攻")
            print("3-接应")
            choice1 = input("请输入选项数字：")
            if choice1 == "1":
                blockpositionB = random.sample(range(1, 3), 1) + random.sample(range(3, 11), 3)
                break
            if choice1 == "2":
                nums = [1, 2, 3, 7, 8, 9, 10, 11]
                blockpositionB = random.sample(range(4, 7), 2) + random.sample(nums, 2)
                break
            if choice1 == "3":
                blockpositionB = random.sample(range(10, 12), 1) + random.sample(range(1, 10), 3)
                break
    else:
        print("请重新输入")
        continue
















choice0=input("enter team A/B: ")
while True:
    if choice0 == 'A':
        attackteam = 1
        break
    if choice0 == 'B':
        attackteam = 0
        break
    else:
        print("请重新输入")
        choice0=input("enter team B/A: ")
while True:
    if attackteam == 1:
        print("现在请B队发球，A队接球")
        while True:
            if a1 == 1:
                if setA >= 2:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")
                    print("3-二次球")
                if setA == 0 or setA == 1:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")


            elif a1 == 0:
                if setA >= 2:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")
                    print("3-接应战术")
                if setA == 0 or setA == 1:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")

            if setA >= 2:
                choice1 = input("请输入选项数字：")
                if choice1 in ["1", "2", "3"]:
                    if choice1 == '1':
                        character = "OH"
                        print("setter:交给你了，主攻！！！")
                    elif choice1 == '2':
                        character = "MB"
                        print("setter:交给你了，副攻！！！")
                    else:
                        if a1 == 1:
                            print("setter:就喜欢偷：）")
                            character = "S"
                        else:
                            character = "OP"
                            print("setter:交给你了，接应！！！")
                    break
                else:
                    print("好好打球：（")
                    continue
            if setA == 0 or setA == 1:
                choice1 = input("请输入选项数字：")
                if choice1 in ["1", "2"]:
                    if choice1 == '1':
                        character = "OH"
                        print("setter:交给你了，主攻！！！")
                    elif choice1 == '2':
                        character = "MB"
                        print("setter:交给你了，副攻！！！")

                    break
                else:
                    print("好好打球：（")
                    continue

        while True:
            if character == "OH":
                if setA >= 3 and attackA >= 3:
                    print("Outside Hitter:你要扣哪条线路？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")
                    print("4-直线")
                    print("5-小斜线")
                choice2 = input("请输入选项数字：")
                if choice2 in ["1", "2", "3", "4,", "5"]:
                    print("Outside Hitter:交给我吧！！！")
                    if choice2 == "1":
                        position = 3
                    elif choice2 == "2":
                        position = 2
                    elif choice2 == "3":
                        position = 4
                    elif choice2 == "4":
                        position = 1
                    elif choice2 == "5":
                        position = 5

                elif     setA <= 2 or attackA <= 2:
                    print("Outside Hitter:你要扣哪条线路？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")

                choice2 = input("请输入选项数字：")
                if choice2 in ["1", "2", "3"]:
                    print("Outside Hitter:交给我吧！！！")
                    if choice2 == "1":
                        position = 3
                    elif choice2 == "2":
                        position = 2
                    elif choice2 == "3":
                        position = 4

                break
            if character == "MB":
                print("Middle Blocker:你要扣哪条线呢？")
                print("1-顺手线")
                print("2-回手线")
                choice3 = input("请输入选项数字：")
                if choice3 in ["1", "2"]:
                    print("Middle Blocker:交给我吧！！！")
                    if choice3 == "1":
                        position = 6
                    if choice3 == "2":
                        position = 4
                break
            if character == "S":
                position = 5
                break

            if character == "OP":
                if setA >= 3 and attackA >= 3:
                    print("Opposite Hitter:你要扣哪条线？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")
                    print("4-直线")
                    print("5-小斜线")
                    choice4 = input("请输入选项数字：")
                    if choice4 in ["1", "2", "3", "4", "5"]:
                        print("Opposite Hitter:交给我吧！！！")
                        if choice4 == "1":
                            position = 9
                        if choice4 == "2":
                            position = 10
                        if choice4 == "3":
                            position = 8
                        if choice4 == "4":
                            position = 11

                        if choice4 == "5":
                            position = 7
                    break

                if setA <= 2 or attackA <= 2:
                    print("Opposite Hitter:你要扣哪条线？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")
                    choice4 = input("请输入选项数字：")
                    if choice4 in ["1", "2", "3", ]:
                        print("Opposite Hitter:交给我吧！！！")
                        if choice4 == "1":
                            position = 9
                        if choice4 == "2":
                            position = 10
                        if choice4 == "3":
                            position = 8

                    break

        time.sleep(1)
        print("让球飞一会...", end="")
        time.sleep(1)
        print("\r\033[K", end="")
        time.sleep(1)
        print("还要再飞一会...")
        time.sleep(1)
        if position in blockpositionB:
            print("遇到拦网：")
            nums = range(1, 11)
            num1 = random.choice(nums)
            num2 = random.choice(nums)
            num3 = random.choice(nums)
            if attackA == 4:
                if num1 in [1, 2, 3]:
                    print("炸手出界")
                    board.add_score('A', 1)
                    attackteam = 0



                else:
                    if defenceA == 4:
                        if num2 in [1]:
                            print("保护成功！！！")
                            attackteam = 1
                        else:
                            print("...被拦网了")
                            board.add_score('B', 1)
                            attackteam = 1

                    elif defenceA == 5:
                        if num3 in [1, 2, 3]:
                            print("保护成功！！！")
                            attackteam = 1
                        else:
                            print("...被拦网了")
                            board.add_score('B', 1)
                            attackteam = 1
                    else:
                        print("...被拦网了")
                        board.add_score('B', 1)
                        attackteam = 1

            elif attackA == 5:
                if num1 in [1,2,3,4,5]:
                    print("炸手出界")
                    board.add_score('A', 1)
                    attackteam = 0
                else:
                    if defenceA == 4:
                        if num2 in [1]:
                            print("保护成功！！！")
                            attackteam = 1
                        else:
                            print("...被拦网了")
                            board.add_score('B', 1)
                            attackteam = 1
                    elif defenceA == 5:
                        if num3 in [1, 2, 3]:
                            print("保护成功！！！")
                            attackteam = 1
                        else:
                            print("...被拦网了")
                            board.add_score('B', 1)

                            attackteam =1
                    else:
                        print("...被拦网了")
                        board.add_score('B', 1)
                        attackteam = 1
            else:
                print("...被拦网了")
                board.add_score('B', 1)
                attackteam = 1

        else:
            print("避开拦网：")
            nums = range(1, 11)
            num1 = random.choice(nums)
            num2 = random.choice(nums)
            num3 = random.choice(nums)
            if attackA == 5:
                print("下球成功！！！")
                board.add_score('A', 1)
                attackteam = 0
            elif attackA == 4:
                if num1 in [1, 2, 3,4,5,6,7]:
                    print("下球成功！！！")
                    board.add_score('A', 1)
                    attackteam = 0
                else:
                    if defenceB == 5:
                        if num2 in [1,2,3]:
                            print("B队成功防起，B队机会球！！！")
                            attackteam = 0
                        else:
                            print("B队成功防起，A队机会球！！！")
                            attackteam = 1
                    if defenceB == 4:
                        if num2 in [1]:
                            print("B队成功防起，B队机会球！！！")
                            attackteam = 0
                        else:
                            print("B队成功防起，A队机会球！！！")
                            attackteam = 1
            elif attackA == 3:
                if num1 in [1, 2, 3,4,5]:
                    print("下球成功！！！")
                    board.add_score('A', 1)
                    attackteam = 0
                else:
                    if defenceB == 4 or defenceB == 5:
                        if num2 in [1, 2, 3]:
                            print("B队成功防起，B队机会球！！！")
                            attackteam = 0
                        else:
                            print("B队成功防起，A队机会球！！！")
                            attackteam = 1
                    elif defenceB == 3 or defenceB == 2:
                        print("B队成功防起，A队机会球！！！")
                        attackteam = 1
                    else:
                        print("下球成功！！！")
                        board.add_score('A', 1)
                        attackteam = 0











        time.sleep(2)
        board.show_score()

    elif attackteam == 0:
        print("现在请A队发球，B队接球")
        while True:
            if a2 == 1:
                if setB >= 2:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")
                    print("3-二次球")
                if setB == 0 or setB == 1:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")


            elif a2 == 0:
                if setB >= 2:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")
                    print("3-接应战术")
                if setB == 0 or setB == 1:
                    print("setter:你要把球传给谁？")
                    print("1-四号位战术")
                    print("2-副攻战术")

            if setB >= 2:
                choice1 = input("请输入选项数字：")
                if choice1 in ["1", "2", "3"]:
                    if choice1 == '1':
                        character = "OH"
                        print("setter:交给你了，主攻！！！")
                    elif choice1 == '2':
                        character = "MB"
                        print("setter:交给你了，副攻！！！")
                    else:
                        if a2 == 1:
                            print("setter:就喜欢偷：）")
                            character = "S"
                        else:
                            character = "OP"
                            print("setter:交给你了，接应！！！")
                    break
                else:
                    print("好好打球：（")
                    continue
            if setB == 0 or setB == 1:
                choice1 = input("请输入选项数字：")
                if choice1 in ["1", "2"]:
                    if choice1 == '1':
                        character = "OH"
                        print("setter:交给你了，主攻！！！")
                    elif choice1 == '2':
                        character = "MB"
                        print("setter:交给你了，副攻！！！")

                    break
                else:
                    print("好好打球：（")
                    continue

        while True:
            if character == "OH":
                if setB >= 3 and attackB >= 3:
                    print("Outside Hitter:你要扣哪条线路？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")
                    print("4-直线")
                    print("5-小斜线")
                choice2 = input("请输入选项数字：")
                if choice2 in ["1", "2", "3", "4,", "5"]:
                    print("Outside Hitter:交给我吧！！！")
                    if choice2 == "1":
                        position = 3
                    elif choice2 == "2":
                        position = 2
                    elif choice2 == "3":
                        position = 4
                    elif choice2 == "4":
                        position = 1
                    elif choice2 == "5":
                        position = 5

                elif     setB <= 2 or attackB <= 2:
                    print("Outside Hitter:你要扣哪条线路？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")

                choice2 = input("请输入选项数字：")
                if choice2 in ["1", "2", "3"]:
                    print("Outside Hitter:交给我吧！！！")
                    if choice2 == "1":
                        position = 3
                    elif choice2 == "2":
                        position = 2
                    elif choice2 == "3":
                        position = 4

                break
            if character == "MB":
                print("Middle Blocker:你要扣哪条线呢？")
                print("1-顺手线")
                print("2-回手线")
                choice3 = input("请输入选项数字：")
                if choice3 in ["1", "2"]:
                    print("Middle Blocker:交给我吧！！！")
                    if choice3 == "1":
                        position = 6
                    if choice3 == "2":
                        position = 4
                break
            if character == "S":
                position = 5
                break

            if character == "OP":
                if setB >= 3 and attackB >= 3:
                    print("Opposite Hitter:你要扣哪条线？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")
                    print("4-直线")
                    print("5-小斜线")
                    choice4 = input("请输入选项数字：")
                    if choice4 in ["1", "2", "3", "4", "5"]:
                        print("Opposite Hitter:交给我吧！！！")
                        if choice4 == "1":
                            position = 9
                        if choice4 == "2":
                            position = 10
                        if choice4 == "3":
                            position = 8
                        if choice4 == "4":
                            position = 11

                        if choice4 == "5":
                            position = 7
                    break

                if setB <= 2 or attackB <= 2:
                    print("Opposite Hitter:你要扣哪条线？")
                    print("1-大斜线")
                    print("2-二直线")
                    print("3-腰线")
                    choice4 = input("请输入选项数字：")
                    if choice4 in ["1", "2", "3", ]:
                        print("Opposite Hitter:交给我吧！！！")
                        if choice4 == "1":
                            position = 9
                        if choice4 == "2":
                            position = 10
                        if choice4 == "3":
                            position = 8

                    break

        time.sleep(1)
        print("让球飞一会...", end="")
        time.sleep(1)
        print("\r\033[K", end="")
        time.sleep(1)
        print("还要再飞一会...")
        time.sleep(1)
        if position in blockpositionB:
            print("遇到拦网：")
            nums = range(1, 11)
            num1 = random.choice(nums)
            num2 = random.choice(nums)
            num3 = random.choice(nums)
            if attackB == 4:
                if num1 in [1, 2, 3]:
                    print("炸手出界")
                    board.add_score('B', 1)
                    attackteam = 1



                else:
                    if defenceB == 4:
                        if num2 in [1]:
                            print("保护成功！！！")
                            attackteam = 0
                        else:
                            print("...被拦网了")
                            board.add_score('A', 1)
                            attackteam = 0

                    elif defenceB == 5:
                        if num3 in [1, 2, 3]:
                            print("保护成功！！！")
                            attackteam = 0
                        else:
                            print("...被拦网了")
                            board.add_score('A', 1)
                            attackteam = 0
                    else:
                        print("...被拦网了")
                        board.add_score('A', 1)
                        attackteam = 0

            elif attackB == 5:
                if num1 in [1,2,3,4,5]:
                    print("炸手出界")
                    board.add_score('B', 1)
                    attackteam = 1
                else:
                    if defenceB == 4:
                        if num2 in [1]:
                            print("保护成功！！！")
                            attackteam = 0
                        else:
                            print("...被拦网了")
                            board.add_score('A', 1)
                            attackteam = 0
                    elif defenceB == 5:
                        if num3 in [1, 2, 3]:
                            print("保护成功！！！")
                            attackteam = 0
                        else:
                            print("...被拦网了")
                            board.add_score('A', 1)

                            attackteam =0
                    else:
                        print("...被拦网了")
                        board.add_score('A', 1)
                        attackteam = 0
            else:
                print("...被拦网了")
                board.add_score('A', 1)
                attackteam = 0

        else:
            print("避开拦网：")
            nums = range(1, 11)
            num1 = random.choice(nums)
            num2 = random.choice(nums)
            num3 = random.choice(nums)
            if attackB == 5:
                print("下球成功！！！")
                board.add_score('B', 1)
                attackteam = 1
            elif attackB == 4:
                if num1 in [1, 2, 3,4,5,6,7]:
                    print("下球成功！！！")
                    board.add_score('B', 1)
                    attackteam = 1
                else:
                    if defenceA == 5:
                        if num2 in [1,2,3]:
                            print("A队成功防起，A队机会球！！！")
                            attackteam = 1
                        else:
                            print("A队成功防起，B队机会球！！！")
                            attackteam = 0
                    if defenceA == 4:
                        if num2 in [1]:
                            print("A队成功防起，A队机会球！！！")
                            attackteam = 1
                        else:
                            print("A队成功防起，B队机会球！！！")
                            attackteam = 0
            elif attackB == 3:
                if num1 in [1, 2, 3,4,5]:
                    print("下球成功！！！")
                    board.add_score('B', 1)
                    attackteam = 1
                else:
                    if defenceA == 4 or defenceA == 5:
                        if num2 in [1, 2, 3]:
                            print("A队成功防起，A队机会球！！！")
                            attackteam = 1
                        else:
                            print("A队成功防起，B队机会球！！！")
                            attackteam = 0
                    elif defenceA == 3 or defenceA == 2:
                        print("A队成功防起，B队机会球！！！")
                        attackteam = 0
                    else:
                        print("下球成功！！！")
                        board.add_score('A', 1)
                        attackteam = 1











        time.sleep(2)
        board.show_score()
    else:
        print("输入错误")




    if (board.score1 >= 25 or board.score2 >= 25) and abs(board.score1 - board.score2) >=2:
        if board.score1 > board.score2:
            board.show_score()
            gap = board.score1 - board.score2
            print(f"A队以{gap}优势获胜")
            break
        if board.score2 > board.score1:
            board.show_score()
            gap = board.score2 - board.score1
            print(f"B队以{gap}优势获胜")
            break





























