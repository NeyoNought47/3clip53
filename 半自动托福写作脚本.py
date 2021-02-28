# 祖传开头（名称，日期，作者）
# 新版本(2.0)加入了 1. 判断第一段主题是短语还是句子||2. 判断有没有每一段的例子 没有的话留空||3. 简单修改
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
print("----------TOEFL Automatic Writing programme II Alpha----------")
print("                    Created on Oct 13, 2020")
print("                      @Author: NeyoNought")
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

# 让用户输入所有的主题句/例子
UsrRMT = input("Enter reading material's main topic here(P1): ")
UsrLMT = input(str("Enter listening material's main topic here(P1): "))
UsrRT1 = input(str("Enter reading topic sentence here(P2): "))
UsrLT1 = input(str("Enter listening topic sentence here(P2): "))
UsrLE1 = input(str("Enter listening example here(P2): "))
UsrRT2 = input(str("Enter reading topic sentence here(P3): "))
UsrLT2 = input(str("Enter listening topic sentence here(P3): "))
UsrLE2 = input(str("Enter listening example here(P3): "))
UsrRT3 = input(str("Enter reading topic sentence here(P4): "))
UsrLT3 = input(str("Enter listening topic sentence here(P4): "))
UsrLE3 = input(str("Enter listening example here(P4): "))

# 输出文档用的语句（前）
out = open("WritingOutput.txt", "w")

# 询问第一段的主题是短语还是句子 短语用of 句子用that 并打印出文章（Pt1）
Phase = "phase" or "Phase"
Sentence = "sentence" or "Sentence"
SenOrPha = input("The topic you entered in paragraph one is a Phase or Sentence?")
if SenOrPha == Phase:
    print("The reading passage explores the issue of " + UsrRMT + ".", file = out)
else:
    print("The reading passage explores the issue that " + UsrRMT + ".", file = out)

# 打印出文章（Pt2）
print("The listening material deals with the same issue; \nhowever, it thinks that "+ UsrLMT + ", which contradicts what the reading passage states.\n", file = out)
print("Firstly, the reading passage makes the point that " + UsrRT1 +".", file = out)
print("However, the listening material demonstrates a contradictory idea that " + UsrLT1 + ".", file = out)

# 例子判断1
Yes = "Yes" or "yes"
No = "No" or "no"
Example1 = input("Do you have example one in paragraph two? (Yes/No)")

if Example1 == Yes:
    print("For example, " + UsrLE1 + ".\n", file = out)
else:
    print("")

print("Secondly, according to the reading passage, " + UsrRT2 + ".", file = out)
print("The listening material refutes the idea by mentioning that " + UsrLT2 + ".", file = out)

# 例子判断2
Yes = "Yes" or "yes"
No = "No" or "no"
Example2 = input("Do you have example two in paragraph three? (Yes/No)")
if Example2 == Yes:
    print("To be specific, " + UsrLE2 + ".\n", file=out)
else:
    print("")

print("Thirdly, the reading passage makes it clear that " + UsrRT3 + ".", file = out)
print("The listening material holds a different perspective which is that " + UsrLT3 + ".", file = out)

# 例子判断3
Yes = "Yes" or "yes"
No = "No" or "no"
Example3 = input("Do you have example three in paragraph four? (Yes/No)")
if Example3 == Yes:
    print("For example, " + UsrLE3 + ".\n", file=out)
else:
    print("")

print("In conclusion, the points made in the listening material challenge the reading passage's claim.", file = out)

# 输出文档用的语句（后）
out.close()
print("\n")

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("\n")
print("Done! The file I generated will be saved as WritingOutput.txt")
print("Don't forget to double-check.")

