# ExcelSQl
Simple Api for using SQL commands with group of excel files
 
## Installing
### Windows
1. download python from https://www.python.org/ftp/python/3.8.9/python-3.8.9-amd64.exe and install
2. open terminal (cmd) and verify installation with typing ```python3 --version```. You should get output telling You that you have python 3.8.9
3. download repository via ```git clone https://github.com/Ardiegon/ExcelSQl.git"``` or downloading zip and unzip it to directory.
4. With terminal, open directory and type ``` pip3 install -r requirements.txt ```
5. Run ``` python3 pandassql.py -h ```
6. If you get prompted with program help, program is ready to use.

## Use

To run sql for excel files please run:
```
python3 pandassql.py --sql <command> --excels <first/excel/path.xmls> <second/excel/path.xmls> <...> 
```

It will allow you to create output excel that answers to query from "sql" argument.

## Demo

While being in project directory, run: 
```
python3 pandassql.py --sql  "SELECT pracownicy.id, team, COALESCE(done, 'nie' ) AS wynik FROM pracownicy LEFT JOIN podeszli ON pracownicy.id = podeszli.id" --excels "example_files\podeszli.xlsx" "example_files\pracownicy.xlsx" 
```
It will create output excel, that connects together data from list of all workers in company S (pracownicy.xlsx), with incomplete list of all workers that started working with compliance training (podeszli.xmls).