#!/usr/bin/env python
# coding=utf8

# pboywalltools : Tool code used for the Pboy wall paint bitcoin puzzle
# Copyright (C) 2019  Antoine FERRON
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
	mnemonicwl = [
					"mensonge usure banquier {0} conduire triomphe union citoyen horizon jaune {1} espoir",
					"{0} mensonge usure banquier conduire triomphe union citoyen horizon jaune {1} espoir",
					"mensonge usure banquier {0} union citoyen conduire triomphe horizon jaune {1} espoir",
					"{0} mensonge usure banquier union citoyen conduire triomphe horizon jaune {1} espoir",
					"banquier usure mensonge {0} union citoyen conduire triomphe horizon jaune {1} espoir",
					"banquier usure mensonge {0} conduire triomphe union citoyen horizon jaune {1} espoir",
					"banquier usure mensonge {0} espoir {1} union citoyen conduire triomphe horizon jaune",
					"banquier usure mensonge {0} espoir {1} conduire triomphe union citoyen horizon jaune",
					"banquier usure mensonge {0} {1} espoir union citoyen conduire triomphe horizon jaune",
					"banquier usure mensonge {0} {1} espoir conduire triomphe union citoyen horizon jaune"
				]
	motrl = [
			"parole",
			"unique",
			"favori",
			"peuple",
			"rincer",
			"rondin",
			"renard",
			"renvoi",
			"utopie",
			"public",
			"révolte",
			"poteau",
			"rideau",
			"rouleau",
			"absolu",
			"infini",
			"samedi",
			"ennemi",
			"fourmi",
			"thorax",
			"abolir",
			"croire",
			"époque",
			"étoile",
			"gloire",
			"isoler",
			"propre",
			"guide",
			"priver",
			"irréel",
			"libérer",
			"histoire",
			"civil",
			"social",
			"bataille",
			"victoire",
			"gloire",
			"combat",
			"courage",
			"drapeau",
			"incendier",
			"avancer",
			"flamme",
			"incendie",
			"lumière",
			"survie",
			"peintre",
			"réagir",
			"réaliser",
			"réclamer",
			"tolérant",
			"voter"
			]
	motxl = bitcoin.wordlist_french
	passphrase = ""
	network = 5
	i = 0
	for mnemonicw in mnemonicwl:
		for motr in motrl:
			for motx in motxl:
				mnemonic = mnemonicw.format(motr, motx)
				if i%1000==0:
					print i
					print mnemonic
				seedBIP39 = mnemonic2seed(mnemonic, passphrase, "PBKDF2-2048-HMAC-SHA512")
				seedBitAdr = mnemonic2seed(mnemonic, passphrase, "SHA256")
				seedBitAdrNFKD = mnemonic2seed(mnemonic, passphrase, "SHA256-NFKD")
				badr = seed2address(seedBitAdr, network, "", False)
				badrNFKD = seed2address(seedBitAdrNFKD, network, "", False)
				bcadrnh = seed2address(seedBIP39, network, "m/0'/0'/0")
				bcadr = seed2address(seedBIP39, network, "m/0'/0'/0'")
				bciadr = seed2address(seedBIP39, network, "m/44'/0'/0'/0")
				mbadr = seed2address(seedBIP39, network, "m/0'/0/0")
				b39 = seed2address(seedBIP39, network, "m")
				b44 = seed2address(seedBIP39, network, "m/44'/0'/0'/0/0")
				if "1NqPwPp7hEXZ3Atj77Ue11xAEMmXqAXwrQ" in ( badr, bcadr, bcadrnh, bciadr,mbadr, b44, badrNFKD, b39):
					print "  >>>>>>>>>>>>>>>      FOUND            <<<<<<<<<<<<<<<<<"
					print " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
					print " BRAVO !"
					print ""
					print mnemonic
					sys.exit(0)
				mnemonic2 = mnemonicw.format(motx, motr)
				seedBIP39 = mnemonic2seed(mnemonic2, passphrase, "PBKDF2-2048-HMAC-SHA512")
				seedBitAdr = mnemonic2seed(mnemonic2, passphrase, "SHA256")
				seedBitAdrNFKD = mnemonic2seed(mnemonic, passphrase, "SHA256-NFKD")
				badr = seed2address(seedBitAdr, network, "", False)
				badrNFKD = seed2address(seedBitAdrNFKD, network, "", False)
				bcadrnh = seed2address(seedBIP39, network, "m/0'/0'/0")
				bcadr = seed2address(seedBIP39, network, "m/0'/0'/0'")
				bciadr = seed2address(seedBIP39, network, "m/44'/0'/0'/0")
				mbadr = seed2address(seedBIP39, network, "m/0'/0/0")
				b39 = seed2address(seedBIP39, network, "m")
				b44 = seed2address(seedBIP39, network, "m/44'/0'/0'/0/0")
				if "1NqPwPp7hEXZ3Atj77Ue11xAEMmXqAXwrQ" in ( badr, bcadr, bcadrnh, bciadr,mbadr, b44, badrNFKD, b39):
					print "  >>>>>>>>>>>>>>>      FOUND            <<<<<<<<<<<<<<<<<"
					print " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
					print " BRAVO !"
					print ""
					print mnemonic2
					sys.exit(0)
				i += 1
				#raw_input("Press ENTER to quit")

