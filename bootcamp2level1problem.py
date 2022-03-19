def master_yoga(sentence):
	#RETURN A PALINDROME FOR THE GIVEN SENTENCE(REVERSE OF THE GIVEN SENTENCE FROM THE BACK)

	wordlist = sentence.split()
	reverse_wordlist = wordlist[::-1]
	#WE USE THE ' '.join METHOD SO THAT THE RESULTING CODE WILL NOT BE A LIST RATHER A PALINDROME

	return ' '.join(reverse_wordlist)
