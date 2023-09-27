def generate_zodiac_prime_birthdays(primes):
    zodiacs = {
        'Capricorn': [(1, 1, 19)],
        'Aquarius': [(1, 20, 31), (2, 1, 18)],
        'Pisces': [(2, 19, 28), (2, 19, 29), (3, 1, 20)],
        'Aries': [(3, 21, 31), (4, 1, 19)],
        'Taurus': [(4, 20, 30), (5, 1, 20)],
        'Gemini': [(5, 21, 31), (6, 1, 20)],
        'Cancer': [(6, 21, 30), (7, 1, 22)],
        'Leo': [(7, 23, 31), (8, 1, 22)],
        'Virgo': [(8, 23, 31), (9, 1, 22)],
        'Libra': [(9, 23, 30), (10, 1, 22)],
        'Scorpio': [(10, 23, 31), (11, 1, 21)],
        'Sagittarius': [(11, 22, 30), (12, 1, 21)]
    }
    total_prime_birthdays = {zodiac:0 for zodiac in zodiacs.keys()}
    for year in range(0,10000):
        for zodiac in zodiacs.keys():
            for month_start_day_end in zodiacs[zodiac]:
                month = month_start_day_end[0]
                start_day = month_start_day_end[1]
                end_day = month_start_day_end[2]
                if month ==2 and end_day ==29 and year%4 !=0:
                    continue
                for day in range(start_day,end_day+1):
                    try:
                        date = datetime.datetime(year ,month ,day)
                        date_str = date.strftime('%d%m%Y')
                        if int(date_str) in primes:
                            total_prime_birthdays[zodiac] +=1
                    except ValueError:
                        pass
    return total_prime_birthdays

def main():
    primes = read_primes('prime1.txt')
    primes.update(read_primes('prime2.txt'))
    
    year = int(input("Enter the year: "))
    prime_birthdays = generate_prime_birthdays(year ,primes)
    
    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in prime_birthdays.items() ]))
    print(df)
    
    total_zodiac_prime_birthdays = generate_zodiac_prime_birthdays(primes)
    print("\nTotal number of prime birthdays for each Zodiac sign from the year 0000 to the year of interest are:")
    for zodiac in total_zodiac_prime_birthdays.keys():
        print(f"{zodiac}: {total_zodiac_prime_birthdays[zodiac]}")

if __name__ == "__main__":
    main()
