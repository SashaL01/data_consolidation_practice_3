"""
Генератор тестовых данных для задания : Анализ client payment for client
Создает три файла:

csv 
1 client_id
2 age 
3 credit_score

xl 
client_id
credit_amount

json
credit_score_range
interest_rate
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta
import random

# Настройка генератора случайных чисел для воспроизводимости
np.random.seed(42)
random.seed(42)


# generate danyh dla csv

def generate_client_data(num_clients=1000):
    """Генерация данных об clients (CSV)"""
    
    client_data = []
    
    for i in range(1,num_clients+1):
        client_id = f"client{i:05d}"
        age = random.randint(18,70)
        credit_score = random.randint(100,850)

        client_data.append({
            "client_id":client_id,
            "age": age,
            "credit_score": credit_score
        })


    df_client = pd.DataFrame(client_data)
    df_client.to_csv('data/client.csv', index=False, encoding='utf-8')
    print("✓ Файл clients.csv создан")
    return client_data










#generate danyh dla xl

def generate_credits_data(clients_data):
    """Генерация данных о credits (Excel)"""
    credits_data = []
    
    for client in clients_data:  
        client_id = client['client_id']
        

        # summa credita v zavisimosti ot credit_score
        if client ["credit_score"] >= 750:
            credit_amount = random.randint(100000, 1000000)
        elif client["credit_score"] >= 600:
            credit_amount = random.randint(70000,100000)
        else:
            credit_amount = random.randint(50000,300000)

        credits_data.append({
            "client_id": client_id,
            "credit_amount": credit_amount
        })


    df_credits = pd.DataFrame(credits_data)
    df_credits.to_excel('data/credits.xlsx', index=False)

    print("✓ Файл credits.xlsx создан")

    return credits_data


# generate danyh dla json

def generate_rates_data():

    """Генерация данных о credit rating  (JSON)"""


    rates_data = [
        {"credit_score_range": "100-300","interest_rate":round(random.uniform(15, 25), 2)},
        {"credit_score_range": "300-500","interest_rate":round(random.uniform(10, 15), 2)},
        {"credit_score_range": "500-700","interest_rate":round(random.uniform(7, 10), 2)}, 
        {"credit_score_range": "700-800","interest_rate":round(random.uniform(4, 7), 2)},
        {"credit_score_range": "800-850","interest_rate":round(random.uniform(2, 4), 2)}
    ]

    
    # Сохраняем в JSON
    with open('data/rates.json', 'w', encoding='utf-8') as f:
        json.dump(rates_data, f, ensure_ascii=False, indent=2)
    
    print("✓ Файл rates.json создан")

    return rates_data

def main():
    """Основная функция генерации данных"""
    print("Генерация тестовых данных для анализа авиакомпаний...")
    print("=" * 50)
    
    # Создаем папку data если её нет
    if not os.path.exists('data'):
        os.makedirs('data')
        print("✓ Создана папка 'data'")
    
    # Генерируем данные
    client_data = generate_client_data()
    generate_credits_data(client_data)
    generate_rates_data()
    
    print("=" * 50)
    print(f"Сгенерировано:")
    print(f"- client: {len(client_data)}")
    print("\nВсе файлы сохранены в папке 'data/'")

if __name__ == "__main__":
    main()
