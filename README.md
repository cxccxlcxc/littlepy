# Little py

Provide python utility in linux pipe, takes commands from stdin and parse into pandas dataframe variable X

## Installation

   python setup.py install

## Usage

	#count how many process running by each USER
	ps -aux | tr -s " " | awk '{print $1,$2}' | py -d 'print X.groupby("USER").count()'

	#sum up how many cpu resource used by each USER
	ps -aux | tr -s " " | awk '{print $1,$3}' | py -d 'print X.groupby("USER")["%CPU"].sum()'

	#quick data analysis on a csv file
	cat ../data/test.csv | py -d -s, "print X.describe()"


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
