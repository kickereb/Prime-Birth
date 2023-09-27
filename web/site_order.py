from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        year = request.form.get('year')
        primes = read_primes('prime1.txt')
        primes.update(read_primes('prime2.txt'))
        prime_birthdays = generate_prime_birthdays(int(year), primes)
        return render_template('results.html', prime_birthdays=prime_birthdays)
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
