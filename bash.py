import os
  
os.system('python categorize.py ann_consum_36820 cement .*cement.* O')

os.system('python categorize.py ann_consum_36820 ceramic .*ceramic.* O')

os.system('python categorize.py ann_consum_36820 chem_fert .*fert.* O')

os.system('python categorize.py ann_consum_36820 food .*food.*^|.*confect.*^|.*bread.*^|.*biscuit.*^|.*baker.*^|.*bekary.*^|.*backery.*^|.*dairy.*^|.*beverage.*^|.*chira.*^|.*muri.*^|.*moure.*^|.*chanach.*^|.*agri.*^|.*agro.*^|.*sweet.* O')

os.system('python categorize.py ann_consum_36820 garment .*garment.*^|.*appar.*^|.*sweat.*^|.*stitch.*^|.*fashion.*^|.*denim.*^|.*jean.*^|.*wash.*^|.*dyeing.*^|.*dying.*^|.*fabric.*^|.*apperals.*^|.*clothing.*^|.*dress.*^|.*wear.*^|.*wool.*^|.*style.*^|.*towel.*^|.*shirt.* O')

os.system('python categorize.py ann_consum_36820 glass .*glass.* O')

os.system('python categorize.py ann_consum_36820 iron_steel .*iron.*^|.*steel.*^|.*roll.*^|.*ispat.*^|.*re-rol.* O')

os.system('python categorize.py ann_consum_36820 jute .*jute.* O')

os.system('python categorize.py ann_consum_36820 paper_pulp .*paper.*^|.*pulp.*^|.*tissue.*^|.*newsprint.* O')

os.system('python categorize.py ann_consum_36820 pharma .*phar.*^|.*farma.*^|.*sanofi.*^|.*eskayef.*^|.*s\.k\.f.*^|.*acme* O')

os.system('python categorize.py ann_consum_36820 sugar .*sugar.* O')

os.system('python categorize.py ann_consum_36820 tex .*tex.*^|.*knit.*^|.*spin.*^|.*yarn.*^|.*cotton.*^|.*composite.*^|.*weav.* O')

os.system('python categorize.py ann_consum_36820 lime .*lime.* O')

os.system('python categorize.py ann_consum_36820 hotel_resort .*hotel.*^|.*resort.*^|.*restaurant.*^|.*restaurent.*^|.*rest\..*^|.*restora.*^|.*cafe.*^|.*kabab.*^|.*restaura.*^|.*restt.*^|.*chi.*^&.*thai.*^|.*thai.*^&.*chi.* O')

os.system('python categorize.py ann_consum_36820 leather .*leath.*^|.*tann.* O')

os.system('python categorize.py ann_consum_36820 chemical .*chem.* O')

os.system('python categorize.py ann_consum_36820 metal .*metal.* O')

os.system('python categorize.py ann_consum_36820 cng .*cng.* O')

os.system('python categorize.py ann_consum_36820 hospital .*hospital.*^|.*B\.I\.R\.D\.E\.M.*^|.*cancer.*^|.*heart.*^|.*kidney.* O')

os.system('python categorize.py ann_consum_36820 filling .*filling.* O')

os.system('python categorize.py ann_consum_36820 tea .*_tea_.* O')

os.system('python categorize.py ann_consum_36820 brick .*brick.* O')

os.system('python categorize.py ann_consum_36820 edu .*school.*^|.*college.*^|.*madrasa.*^|.*madrasha.*^|.*university.*^|.*principal.*^|.*buet.*^|.*hall.*^|.*academ.* O')

os.system('python check_uncategorized.py ann_consum_36820 uncategorized O')

os.system('python list_words.py uncategorized word_freq O')