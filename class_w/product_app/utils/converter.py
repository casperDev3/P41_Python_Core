import requests

def converter():
      print("Оtримуємо актуальнийц курс валют...")
      r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()
      user_val_uah = int(input("Введіть к-ть гривень, що хочете поміняти: "))

      data_usd = list(filter(lambda x: x["cc"] == "USD", r))[0]
      usd_result = round(user_val_uah / data_usd["rate"], 2)

      data_euro = list(filter(lambda x: x["cc"] == "EUR", r))[0]
      euro_result = round(user_val_uah / data_euro["rate"], 2)

      data_ster = list(filter(lambda x: x["cc"] == "GBP", r))[0]
      ster_result = round(user_val_uah / data_ster["rate"], 2)

      data_zln = list(filter(lambda x: x["cc"] == "PLN", r))[0]
      zln_result = round(user_val_uah / data_zln["rate"], 2)

      print("----- Результати ----- \n\n"
            f"{data_usd['txt']}: {usd_result} {data_usd['cc']}\n"
            f"{data_euro['txt']}: {euro_result} {data_euro['cc']}\n"
            f"{data_ster['txt']}: {ster_result} {data_ster['cc']}\n"
            f"{data_zln['txt']}: {zln_result} {data_zln['cc']}")
