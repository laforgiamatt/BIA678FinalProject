import sys

import scraper as Scraper
import SentimentAnalysis_2labels as SA2
import NeuralNetwork_2labels as nn2

def main():
	params = sys.argv[1:]
	#TODO: set up params to scrape each social network

	Scraper.run_twitter()

if __name__ == "__main__":
	main()