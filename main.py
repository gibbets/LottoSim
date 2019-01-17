import pandas
df = pandas.read_csv('LOTTO.csv')

my_list = [[41, 34, 28, 24, 44, 47, 4]]

sum = 0;

for index, row in df.iterrows():
	
	
	for my_numbers in my_list:
		i = 0;
		s = 0;
		
		if row['Zahl1'] in my_numbers:
			i += 1
		if row['Zahl2'] in my_numbers:
			i += 1
		if row['Zahl3'] in my_numbers:
			i += 1
		if row['Zahl4'] in my_numbers:
			i += 1
		if row['Zahl5'] in my_numbers:
			i += 1
		if row['Zahl6'] in my_numbers:
			i += 1
		if row['S'] in my_numbers:
			s = 1
		
		if i == 6 and s == 1:
			sum += row['Quote Kl 1']
		if i == 6 and s == 0:
			sum += row['Quote Kl 2']
		if i == 5 and s == 1:
			sum += row['Quote Kl 3']
		if i == 5 and s == 0:
			sum += row['Quote Kl 4']
		if i == 4 and s == 1:
			sum += row['Quote Kl 5']
		if i == 4 and s == 0:
			sum += row['Quote Kl 6']
		if i == 3 and s == 1:
			sum += row['Quote Kl 7']
		if i == 3 and s == 0:
			sum += row['Quote Kl 8']
		if i == 2 and s == 1:
			sum += row['Quote Kl 9']
			
		sum -= 1

print(sum)