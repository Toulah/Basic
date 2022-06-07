# Assignment: count the number of a given word appears in a text
# specimen adhan (islamic call to prayer)
# Objective: to count the number of time ALLAH appears in the call to prayer

adhan = """Allahu Akbar! Allahu Akbar! Allahu Akbar! Allahu Akbar!
Ashhadu an la ilaha illa Allah. Ashhadu an la ilaha illa Allah.
Ashadu anna Muhammadan Rasool Allah. Ashadu anna Muhammadan Rasool Allah.
Hayya 'ala-s-Salah. Hayya 'ala-s-Salah.
Hayya 'ala-l-Falah. Hayya 'ala-l-Falah.
Allahu Akbar! Allahu Akbar!
La ilaha illa Allah."""

# replace "Allahu" with "Allah
adhan_mod = adhan.replace("Allahu", "Allah")

# Split `a_string` by whitespace
word_list = adhan.split()
almighty = "Allah"
# count the number of times Allah appears in the text
almighty_count = adhan_mod.count("Allah")
print(almighty_count)

# Extra :-)
print("")
number_of_words = len(word_list)
print(number_of_words)
