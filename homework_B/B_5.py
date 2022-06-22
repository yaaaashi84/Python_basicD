ip = input("データを入力してください(スペース区切り) >")

sp = ip.split(" ")
int_sp = [int(s) for s in sp]
print(int_sp)

i_sp = len(int_sp)
print(i_sp)

i = 0
total_sp = 0

for sum_sp in int_sp:
    if i < i_sp:
        total_sp = int_sp[i] + total_sp
        i += 1
    else:
        break

print("合計値：" + str(total_sp))

i = 0
m_sp = int_sp[i]

for r in int_sp:
    if i < i_sp - 1:
        if m_sp < int_sp[i + 1]:
            m_sp = int_sp[i + 1]
            i += 1
        else:
            i += 1
    # else:
    # break

print("最大値：" + str(m_sp))

i = 0
mi_sp = int_sp[i]

for mi_sp in int_sp:
    if i < i_sp - 1:
        if mi_sp < int_sp[i+1]:
            mi_sp = int_sp[i+1]
            i += 1
        else:
            i += 1
    else:
        break

print("最小値：" + str(mi_sp))

average_sp = total_sp / i_sp

print("平均値：" + str(average_sp))
