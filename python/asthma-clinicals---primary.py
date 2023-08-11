# Evangelos Kontopantelis, David Springate, David Reeves, Darren M Ashcroft, Jose M Valderas, Tim Doran, 2023.

import sys, csv, re

codes = [{"code":"173c.00","system":"readv2"},{"code":"173d.00","system":"readv2"},{"code":"1O2..00","system":"readv2"},{"code":"663V000","system":"readv2"},{"code":"663V100","system":"readv2"},{"code":"663V200","system":"readv2"},{"code":"663V300","system":"readv2"},{"code":"663j.00","system":"readv2"},{"code":"H312000","system":"readv2"},{"code":"H33..11","system":"readv2"},{"code":"H330.12","system":"readv2"},{"code":"H330.14","system":"readv2"},{"code":"H331.11","system":"readv2"},{"code":"H332.00","system":"readv2"},{"code":"H334.00","system":"readv2"},{"code":"H33z.00","system":"readv2"},{"code":"H33z.11","system":"readv2"},{"code":"H33z200","system":"readv2"},{"code":"H33zz00","system":"readv2"},{"code":"H35y700","system":"readv2"},{"code":"H47y000","system":"readv2"},{"code":"3052AT","system":"oxmis"},{"code":"493 AA","system":"oxmis"},{"code":"493 AB","system":"oxmis"},{"code":"493 AD","system":"oxmis"},{"code":"493 AE","system":"oxmis"},{"code":"493 AR","system":"oxmis"},{"code":"493 BD","system":"oxmis"},{"code":"493 BR","system":"oxmis"},{"code":"493 C","system":"oxmis"},{"code":"493 CH","system":"oxmis"},{"code":"493 EP","system":"oxmis"},{"code":"493 GR","system":"oxmis"},{"code":"493 GS","system":"oxmis"},{"code":"493 HT","system":"oxmis"},{"code":"493 JC","system":"oxmis"},{"code":"493 NA","system":"oxmis"},{"code":"691 TM","system":"oxmis"},{"code":"L4930LO","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-clinicals-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-clinicals---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-clinicals---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-clinicals---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
