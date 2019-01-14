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

import sys
from CryptoPlatinum import *

if __name__ == '__main__':
	mnemonic = raw_input("Please enter your letters: ").decode(sys.stdin.encoding) #.replace(" ","")
	passphrase = ""
	network = 5
	seedBIP39 = mnemonic2seed(mnemonic, passphrase, "PBKDF2-2048-HMAC-SHA512")
	seedBitAdr = mnemonic2seed(mnemonic, passphrase, "SHA256")
	seedBitAdrNFKD = mnemonic2seed(mnemonic, passphrase, "SHA256-NFKD")
	print "\nAddress : "
	print "bitaddress"
	badr = seed2address(seedBitAdr, network, "", False)
	print ">>    "+badr
	print ""
	print "bitaddress NFKD"
	badrNFKD = seed2address(seedBitAdrNFKD, network, "", False)
	print ">>    "+badrNFKD
	print ""
	bcadrnh = seed2address(seedBIP39, network, "m/0'/0'/0")
	print "Bitcoin Core (non-hardened)"
	print ">>    "+bcadrnh
	print ""
	bcadr = seed2address(seedBIP39, network, "m/0'/0'/0'")
	print "Bitcoin Core"
	print ">>    "+bcadr
	print ""
	bciadr = seed2address(seedBIP39, network, "m/44'/0'/0'/0")
	print "blockchain.info"
	print ">>    "+bciadr
	print ""
	mbadr = seed2address(seedBIP39, network, "m/0'/0/0")
	print "MultiBit HD / Hive"
	print ">>    "+mbadr
	print ""
	b39 = seed2address(seedBIP39, network, "m")
	print "BIP39 only, seed = pvkey"
	print ">>    "+b39
	print ""
	b44 = seed2address(seedBIP39, network, "m/44'/0'/0'/0/0")
	print "BIP39 + BIP44"
	print ">>    "+b44
	print ""
	if "1NqPwPp7hEXZ3Atj77Ue11xAEMmXqAXwrQ" in ( badr, bcadr, bcadrnh, bciadr,mbadr, b39, b44, badrNFKD ):
		print "  >>>>>>>>>>>>>>>      FOUND            <<<<<<<<<<<<<<<<<"
		print " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		print " BRAVO !"
		print ""
	#raw_input("Press ENTER to quit")

