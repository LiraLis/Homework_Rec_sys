import math
import csv

my_user = 20
k = 5
list_data = []  # хранение данных из таблицы для первого задания
list_context = []

f_data = 'D:\\Studies\\7_semester\\Intellect\\data.csv'
f_context = 'D:\\Studies\\7_semester\\Intellect\\context.csv'

# Чтение данных из заданного файла в указанный список
def read_file(file_name, list):
    file = open(file_name)
    for row in csv.reader(file):
        list.append(row)
    file.close()

# метрика сходства для двух пользователей
def sim(u, v):
    sum_u = 0
    sum_v = 0
    sum_uv = 0
    for i in range(1, len(list_data[u])):
        if int(list_data[u][i]) > 0 and int(list_data[v][i]) > 0:
            sum_uv += int(list_data[u][i]) * int(list_data[v][i])
            sum_u += int(list_data[u][i]) * int(list_data[u][i])
            sum_v += int(list_data[v][i]) * int(list_data[v][i])
    if sum_u == 0 or sum_v == 0:
        return 0

    return round((sum_uv / (math.sqrt(sum_u) * math.sqrt(sum_v))),3)

#создание таблицы схожести пользователей
def simularity():
    simul = [[0] * (len(list_data) - 1) for i in range(len(list_data) - 1)]
    for i in range(1, len(list_data)-1):
        for j in range(1, len(list_data)-1):
            if i != j:
                simul[i][j] = sim(i,j)
            else: continue
    return simul

#поиск k схожих
def find_k_user(user, mas):
    similar_k = []
    for i in range(0, k):
        max = 0
        for i in range(1, len(mas[user])):
            if mas[user][i] > mas[user][max] and i not in similar_k:
                max = i
        similar_k.append(max)
    return similar_k

# средняя оценка у пользователя user
def srednee(user):
    sum = 0
    m = 0
    for i in range(1, len(list_data[user])):
        if int(list_data[user][i]) > 0:
            sum += int(list_data[user][i])
            m += 1
    return round((sum / m),3)


def main():
    # Читаю данные из таблиц
    read_file(f_data, list_data)
    read_file(f_context, list_context)

    mas_sim = simularity()#создаю таблицу схожести пользователей

    k_sim = find_k_user(my_user,mas_sim) #k похожих пользователей

    print(list_data)

    rating_film = []
    rating = 0
    k=0
    m=1
    rating_film.append([0,0])
    for i in range(1,len(list_data[2])):
        for j in range(0, len(k_sim)):
            t = k_sim[j]
            if int(list_data[t][i])!=-1:
                rating = rating + int(list_data[t][i])
                k=k+1
        rating = round(rating / k,3)
        rating_film.append([m,rating])
        m=m+1
        rating=0
        k=0

    rating_film = sorted([[ind,  val] for ind, val in rating_film], key=lambda x: x[1], reverse=True)

    print(rating_film)
    film = 0
    for i in range(0, len(rating_film)-1):
        if  list_data[my_user][rating_film[i][0]]==' -1' and list_context[rating_film[i][0]][1]!="-" and list_context[rating_film[i][0]][1]!="Sun" \
                and list_context[rating_film[i][0]][1]!="Sat":
            film = rating_film[i][0]
            break
    print(film)


    sum_1 = 0
    sum_2 = 0

    for j in range(0, len(k_sim)):
        t = k_sim[j]
        if int(list_data[t][5]) > 0:
            sum_1 += (sim(my_user, t) * (int(list_data[t][5]) - srednee(t)))
            sum_2 += math.fabs(sim(my_user, t))
        else:
            continue
    p = round(srednee(my_user) + (sum_1 / sum_2), 3)
    print(str(5) + '=>' + str(p))





if __name__ == "__main__":
    main()
