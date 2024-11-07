import requests
import time
import subprocess
import psutil



URL = 'http://localhost:9000/MobileSMARTS/api/v1/Devices'



list_of_licence = ["*Вставить лицензии ТСД*"]







def mskiller():

    request = requests.get(URL)
    response = request.json()

    tsd_json = response['value']

    tsd_id = set([id_t['deviceId'] for id_t in tsd_json])

    try:
        if sorted(tsd_id) == sorted(list_of_licence):
            print("Проблем не обнаружено")
            openl()
        else:
            print('')
            print("Найден сломанный ТСД")

            find_broke_tsd = tsd_id.symmetric_difference(list_of_licence)
            close()

            for i in find_broke_tsd:
                print("ID ТСД:")
                print(i)
                print('')
            requests.delete(f"{URL}('{i}')" )
            time.sleep(5)

    except:
        pass









def open():
    # Проверяем, запущена ли программа
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if proc.info['name'] == 'ИМЯ ПРОЦЕССА':

                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Программа не найдена, запускаем её
    try:
        print(f"Производится запуск ")
        subprocess.Popen(f'ВСТАВИТЬ ПУТЬ К  ПРОГРАММЕ')
        print(f"")
    except Exception as e:
        print(f"Не удалось запустить: {e}")

def close():

    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if proc.info['name'] == "ИМЯ ПРОЦЕССА":
                proc.terminate()  # Команда для завершения процесса
                proc.wait()  # Ждем завершения процесса
                print(f"Программа закрыта")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass



while True:
    mskiller()
    time.sleep(5)