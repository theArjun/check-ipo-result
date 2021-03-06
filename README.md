# IPO Result Checker

## Installation Instructions
```
pip install -r requirements.txt
python main.py
```

## Usage
```
usage: main.py [-h] [-f] [-a] [-l]

IPO Result Checker

optional arguments:
  -h, --help    show this help message and exit
  -f, --fast    Fast Mode
  -a, --all     Check All
  -l, --latest  Fetch Latest Result
```

`-f` or `--fast` mode means it reads the data from `companies.json` file.  
`-l` or `--latest` mode means it checks the result of latest scrip only.  
`-a` or `--all` mode means it will check the result of every BOID with every scrips.  

### Demo
#### Single Company Mode
```
> [master ≡]python main.py -f 
1. MAHILA LAGHUBITTA BITTIYA SANSTHA LTD.
2. Sunrise Bluechip Fund
3. Jyoti Life Insurance Ltd
4. NIBL Samriddhi Fund -2
5. CEDB Hydropower Development Company Ltd
6. Prabhu Select Fund
7. 4% NMB Energy Bond 2092/93
8. 8.5 % PRVU Debenture 2087
9. Mailung Khola Jal Vidhyut Company Ltd.
10. Sanima Life Insurance Limited
11. 8% Nabil Debenture 2085
12. Manushi Laghubitta Bittiya Sanstha Limited     
13. Mega Mutual Fund -1
14. Terhathum Power Company Ltd
15. NMB Saral Bachat Fund - E
16. Nabil Balanced Fund 3
17. Sahas Urja Ltd.
18. Buddhabhumi Nepal Hydro Power Co. Ltd.
19. Nyadi Hydropower Limited
20. Madhya Bhotekoshi Jalabidhyut Company Ltd.     
21. Samling Power Company Ltd.
22. Civil Bank Debenture 2088
23. Jalpa Samudayik Laghubitta Bittiya Sanstha Ltd.
24. Emerging Nepal Limited
25. Rastra Utthan Laghubitta Bittiya Sanstha Ltd.  

Enter company index: 5 

Selected company: CEDB Hydropower Development Company Ltd

+--------------+------------------+-------------+--------------------------------------------------+
|     Name     |       Boid       |    Result   |                     Remarks                      |
+--------------+------------------+-------------+--------------------------------------------------+
|    Myself    | 130137000XXXXXXX |   Alloted   | Congratulation Alloted !!! Alloted quantity : 10 |
|     Mom      | 130126000XXXXXXX | Not Alloted |    Sorry, not alloted for the entered BOID.      |
|    Sister    | 130157000XXXXXXX | Not Alloted |    Sorry, not alloted for the entered BOID.      |
+--------------+------------------+-------------+--------------------------------------------------+
```

### Multi Company Mode 
```
⠼ Checking results...
+--------------+------------------+------------------------+
|     Name     |       Boid       |   Alloted Companies    |
+--------------+------------------+------------------------+
|    Myself    | 130137000XXXXXXX |  CHDC (10), SLIL (10)  |
|     Mom      | 130126000XXXXXXX |       MKJCL (10)       |
|    Sister    | 130157000XXXXXXX | SLIL (10), MBKJCL (10) |
+--------------+------------------+------------------------+
```
