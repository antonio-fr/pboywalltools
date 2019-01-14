#!/usr/bin/env python
# coding=utf8

# CryptoPlatinum : Easy and reliable handling of HD wallet account
# Copyright (C) 2018-2019  Antoine FERRON
#
#  Generates P2SH addresses from a passphrase
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#

import sys, pickle
from CryptoPlatinum import *

def testadrs():
	None

def sortalphabet():
	None

def pickwords(l1,l2):
	None

def remacc( stri ):
	return stri.decode("ascii","ignore")

if __name__ == '__main__':
	# mnemonic = raw_input("Please enter your letters: ").decode(sys.stdin.encoding) #.replace(" ","")
	with open('list6l',mode="rb") as filein:
		wlf = pickle.load(filein)
	mnemonicw = "banquier citoyen conduire espoir horizon jaune mensonge triomphe union usure rincer"
	mnemonicbaselist = mnemonicw.split(" ")
	passphrase = ""
	network = 5
	z = len(wlf)
	for i in xrange(0,249001):
		addedwords = [ wlf[i%z], wlf[i//z] ]
		if i%100==0:
			print i
			print addedwords
		mnemoniclist = mnemonicbaselist + addedwords
		mnemonic = " ".join( sorted(mnemoniclist, None, remacc) )
		seedBIP39 = mnemonic2seed(mnemonic, passphrase, "PBKDF2-2048-HMAC-SHA512")
		seedBitAdr = mnemonic2seed(mnemonic, passphrase, "SHA256")
		# seedBitAdrNFKD = mnemonic2seed(mnemonic, passphrase, "SHA256-NFKD")
		badr = seed2address(seedBitAdr, network, "", False)
		#badrNFKD = seed2address(seedBitAdrNFKD, network, "", False)
		bcadrnh = seed2address(seedBIP39, network, "m/0'/0'/0")
		bcadr = seed2address(seedBIP39, network, "m/0'/0'/0'")
		bciadr = seed2address(seedBIP39, network, "m/44'/0'/0'/0")
		mbadr = seed2address(seedBIP39, network, "m/0'/0/0")
		#b39 = seed2address(seedBIP39, network, "m")
		b44 = seed2address(seedBIP39, network, "m/44'/0'/0'/0/0")
		if "1NqPwPp7hEXZ3Atj77Ue11xAEMmXqAXwrQ" in ( badr, bcadr, bcadrnh, bciadr,mbadr, b44):
			print "  >>>>>>>>>>>>>>>      FOUND            <<<<<<<<<<<<<<<<<"
			print " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
			print " BRAVO !"
			print ""
		#raw_input("Press ENTER to quit")

