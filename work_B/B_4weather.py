def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    temp_list = [d.get('temperature') for d in weather_information]
    sum_list = sum(temp_list)
    volume_list = len(temp_list)
    temp_mean = sum_list / volume_list
    print(temp_mean)
    
    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    for r in range(0, volume_list):
        # i = i + 1
        if weather_information[r]["prefecture"] == "大阪府":
            # if i == 1:
            #   print("'", end="")

            print(weather_information[r]["station"], end=",")

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)

    count = 0
    sum_temp_fukuoka = 0
    for r in range(0, volume_list):
        if weather_information[r]["prefecture"] == "福岡県":
            temp_fukuoka = weather_information[r]["temperature"]
            sum_temp_fukuoka += temp_fukuoka
            count = count + 1

    ave_temp_fukuoka = sum_temp_fukuoka / count
    print(ave_temp_fukuoka)


if __name__ == "__main__":
    main()