import hashlib
import os.path
import binascii
import random
import sys

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'english.txt'), mode="r") as file:
	wordlistdata = file.read()
wordlist_english = wordlistdata.split('\n')

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'french.txt'),mode="rb") as file:
	wordlistdata = file.read()
wordlist_french = wordlistdata.split('\n')

def eint_to_bytes(entint,entbits):
	a = hex(entint)[2:].rstrip('L').zfill( entbits//4 )
	return binascii.unhexlify(a)

def mnemonic_int_to_words(mint,mint_num_words,wordlist=wordlist_english):
	backwords = [wordlist[(mint >> (11*x)) & 0x7FF].strip() for x in range(mint_num_words)]
	return backwords[::-1]
	
def entropy_cs( entbytes ):
	entropy_size  = 8*len(entbytes)
	checksum_size = entropy_size//32
	hd = hashlib.sha256(entbytes).hexdigest()
	csint = int(hd,16) >> (256-checksum_size)
	return csint, checksum_size
	
def entropy_to_words(entbytes,wordlist=wordlist_english):
	if(len(entbytes) < 4 or len(entbytes) % 4 != 0):
		raise ValueError("The size of the entropy must be a multiple of 4 bytes (multiple of 32 bits)")
	entropy_size = 8*len(entbytes)
	csint,checksum_size = entropy_cs(entbytes)
	entint = int(binascii.hexlify(entbytes),16)
	mint = (entint << checksum_size) | csint
	mint_num_words = (entropy_size+checksum_size)//11
	return mnemonic_int_to_words(mint,mint_num_words,wordlist)

def words_split(wordstr, wordlist=wordlist_english):
	words = wordstr.split(" ")
	for w in words:
		if(w not in wordlist):
			raise Exception("Word %s not in wordlist" % (w.decode('utf8').encode(sys.stdout.encoding,'replace')))
	return words

def words_to_mnemonic_int(words,wordlist=wordlist_english):
	if(isinstance(words,basestring)):
		words = words_split(words,wordlist)
	return sum([wordlist.index(w) << (11*x) for x,w in enumerate(words[::-1])])

def words_verify( words, wordlist = wordlist_english ):
	if (isinstance(words,basestring)):
		words = words_split(words,wordlist)
	wordcount = len(words)
	assert 12 <= wordcount <= 24
	assert wordcount % 3 == 0
	mint = words_to_mnemonic_int(words, wordlist)
	mint_bits = len(words)*11
	cs_bits = mint_bits//32
	entropy_bits = mint_bits - cs_bits
	eint   = mint >> cs_bits
	csint  = mint & ( (1 << cs_bits)-1 )
	ebytes = eint_to_bytes(eint, entropy_bits)
	return (csint, cs_bits) == entropy_cs(ebytes)

def words_mine(prefix,entbits,satisfunction,wordlist=wordlist_english,randombits=random.getrandbits):
	if (isinstance(prefix,basestring)):
		prefix = words_split(prefix,wordlist)
	prefix_bits =len(prefix)*11
	mine_bits =entbits-prefix_bits
	pint =words_to_mnemonic_int(prefix,wordlist)
	pint <<= mine_bits
	dint = randombits(mine_bits)
	while(not satisfunction(entropy_to_words(eint_to_bytes(pint+dint,entbits)))):
		dint = randombits(mine_bits)
	return worldlist2string(entropy_to_words(eint_to_bytes(pint+dint,entbits)))

def worldlist2string(awordlist):
	return " ".join(awordlist)
