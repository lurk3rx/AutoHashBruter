# AutoHashBruter
AutoHashBruter - скрипт для автоматического перебора хэшей из TXT-файлов через hashcat и словарь rockyou.txt.

Данный скрипт создан в учебных целях и будет дорабываться по мере возможности.


## Как использовать скрипт


```bash
python3 autohashbruter.py -h
usage: autohashbruter.py [-h] [-d путь] [-o файл] [-w словарь]

options:
  -h, --help            show this help message and exit
  -d, --directory путь  Директория TXT файлов с хэшами. По умолчанию текущая директория
  -o, --output файл     Вывод данных в файл. По умолчанию cracked_hashes.txt
  -w, --wordlist словарь
                        Путь до словаря. По умолчанию /usr/share/wordlists/rockyou.txt
```
Данный скрипт расчитан на работу в ОС Kali Linux (Изначально в нем есть Hashcat и rockyou.txt)


Содержимое директории test_hashes/:
```bash
┌──(lurk3r㉿kali)-[~/AutoHashBruter]
└─$ ls test_hashes/
hashes_to.txt  hashes.txt
```

### ВАЖНО!!!

В нужной директории все TXT-файлы должны содержать только хэши построчко, как указано в примере выше.

Содержимое тестовых TXT-файлов:
```bash
┌──(lurk3r㉿kali)-[~/AutoHashBruter]
└─$ cat test_hashes/hashes.txt cat test_hashes/hashes_to.txt
d033e22ae348aeb5660fc2140aec35850c4da997
2f268353eebd6193326100692a509847
25d55ad283aa400af464c76d713c07ad
feb8dc0697a2e0a947c6e20dc4ec3ebc
5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
┌──(lurk3r㉿kali)-[~/AutoHashBruter]
└─$ cat test_hashes/hashes.txt 
21232f297a57a5a743894a0e4a801fc3
c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec
1a47e74e0e6ad208c19efb42c0fefded43f07b037a3c552ad04ae8b167417e5612556641c0df4da77643e027b030e6ebcb9264dda9e8db3522952bec751d3b92
775bb961b81da1ca49217a48e533c832c337154a
```
Демонстрация работы скрипта:
```bash
┌──(lurk3r㉿kali)-[~/AutoHashBruter]
└─$ python3 autohashbruter.py -d test_hashes/
Словарь /usr/share/wordlists/rockyou.txt
Итоговый список хешей: ['d033e22ae348aeb5660fc2140aec35850c4da997', '2f268353eebd6193326100692a509847', '25d55ad283aa400af464c76d713c07ad', 'feb8dc0697a2e0a947c6e20dc4ec3ebc', '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8', '21232f297a57a5a743894a0e4a801fc3', 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', '1a47e74e0e6ad208c19efb42c0fefded43f07b037a3c552ad04ae8b167417e5612556641c0df4da77643e027b030e6ebcb9264dda9e8db3522952bec751d3b92', '775bb961b81da1ca49217a48e533c832c337154a']
Брутим хэш d033e22ae348aeb5660fc2140aec35850c4da997
Успешно!
Брутим хэш 2f268353eebd6193326100692a509847
Успешно!
Брутим хэш 25d55ad283aa400af464c76d713c07ad
Успешно!
Брутим хэш feb8dc0697a2e0a947c6e20dc4ec3ebc
Успешно!
Брутим хэш 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
Успешно!
Брутим хэш 21232f297a57a5a743894a0e4a801fc3
Успешно!
Брутим хэш c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec
Успешно!
Брутим хэш 1a47e74e0e6ad208c19efb42c0fefded43f07b037a3c552ad04ae8b167417e5612556641c0df4da77643e027b030e6ebcb9264dda9e8db3522952bec751d3b92
Успешно!
Брутим хэш 775bb961b81da1ca49217a48e533c832c337154a
Успешно!
```
Результат работы скрипта:
```bash
┌──(lurk3r㉿DENIS-PC)-[~/AutoHashBruter]
└─$ cat cracked_hashes.txt 
d033e22ae348aeb5660fc2140aec35850c4da997:admin
2f268353eebd6193326100692a509847:admin1232
25d55ad283aa400af464c76d713c07ad:12345678
feb8dc0697a2e0a947c6e20dc4ec3ebc:123456781
5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8:password
21232f297a57a5a743894a0e4a801fc3:admin
c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec:admin
1a47e74e0e6ad208c19efb42c0fefded43f07b037a3c552ad04ae8b167417e5612556641c0df4da77643e027b030e6ebcb9264dda9e8db3522952bec751d3b92:princess
775bb961b81da1ca49217a48e533c832c337154a:princess
```
