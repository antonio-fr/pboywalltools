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

import bitcoin
import hashlib
#import scrypt
import sys
import unicodedata
import coincurve

def path2list(path):
	def readpathunit(x):
		if x[-1] == "'": out=int(x[:-1])+2147483648
		else : out=int(x)
		return out
	assert path[:1] == "m"
	return map(readpathunit, path.split("/")[1:])

def mnemonic2seed( mnemonic, passphrase="", method="PBKDF2-2048-HMAC-SHA512"):
	msg = u"mnemonic"+passphrase
	msgenc = unicodedata.normalize("NFKD", msg).encode('utf8', 'strict')
	# key = unicodedata.normalize("NFKD", mnemonic).encode('utf8', 'strict')
	key = mnemonic
	#bitcoin.words_verify( key, bitcoin.wordlist_french )
	if method == "PBKDF2-2048-HMAC-SHA512":
		return hashlib.pbkdf2_hmac("sha512", key, msgenc, 2048)
	if method == "SHA256":
		# return hashlib.sha256(mnemonic.encode('utf8')).hexdigest()
		return hashlib.sha256(mnemonic).hexdigest()
	if method == "SHA256-NFKD":
		return hashlib.sha256(key).hexdigest()
	if method == "PBKDF2-50000-HMAC-SHA256":
		return hashlib.pbkdf2_hmac("sha256", key, msgenc, 50000)
	if method == "Scrypt":
		return scrypt.hash(key, msgenc, 1<<14, 8, 8, 64)
	if method == "Bitbox":
		passphrenc = passphrase.encode('utf8', 'strict')
		seed1 = hashlib.pbkdf2_hmac("sha512", passphrenc, 'Digital Bitbox', 20480).encode('hex')
		return hashlib.pbkdf2_hmac("sha512", hashlib.sha256(key).hexdigest(), "mnemonic"+seed1, 2048)
	raise "Error: Wrong seed processing type"

def seed2pvkey(seed, path, bip44=True):
	if bip44:
		master_xprv = bitcoin.bip32_master_key(seed, b'\x04\x88\xAD\xE4')
		path_list = path2list(path)
		return bitcoin.bip32_descend(master_xprv,path_list)
	else:
		return seed+"00"

def pkvkey2adrw(pvkey, network=5):
	pub_hex = bitcoin.privtopub(pvkey)
	pub_bin = bitcoin.encode_pubkey(pub_hex, "bin_compressed")
	PKH = bitcoin.bin_hash160(pub_bin)
	script = "\0\x14" + PKH
	address_bin = bitcoin.bin_hash160(script)
	address = bitcoin.bin_to_b58check(address_bin,network)
	assert bitcoin.p2sh_scriptaddr(script,network) == address
	return address

def pvkey2adr(pvkey, network=5):
	pub_hex = bitcoin.privtopub(pvkey)
	pub_bin = bitcoin.encode_pubkey(pub_hex, "bin_compressed")
	PKH = bitcoin.bin_hash160(pub_bin)
	# script = "\0" + PKH
	# address_bin = bitcoin.bin_hash160(script)
	address = bitcoin.bin_to_b58check(PKH,0)
	#assert bitcoin.p2sh_scriptaddr(script,network) == address
	return address

def pubkey2adr(pub_hex, network=5):
	pub_bin = bitcoin.encode_pubkey(pub_hex, "bin_compressed")
	PKH = bitcoin.bin_hash160(pub_bin)
	# script = "\0" + PKH
	# address_bin = bitcoin.bin_hash160(script)
	address = bitcoin.bin_to_b58check(PKH,0)
	#assert bitcoin.p2sh_scriptaddr(script,network) == address
	return address

def pvkeytoWIF(pvkey, network):
	assert pvkey[-2:] == "01"
	priv = int( pvkey[:-2], 16 )
	pvkeyWIF = bitcoin.encode_privkey(priv,'wif_compressed', network)
	assert bitcoin.decode_privkey(pvkeyWIF) == priv
	return pvkeyWIF

def seed2address(seed, network=5, path="m/49'/0'/0'/0/0", bip44=True):
	# MAINNET network=5 - TESTNET network=196
	if path=="m/49'/0'/0'/0/0" and network==196:
		path = "m/49'/1'/0'/0/0"
	pvkey = seed2pvkey(seed, path, bip44)
	pubkey = coincurve.PrivateKey.from_hex(pvkey[:-2]).public_key.format(True).encode('hex')
	return pubkey2adr(pubkey, network)

def seed2WIF(seed, network=0, path="m/49'/0'/0'/0/0"):
	# MAINNET network=0 - TESTNET network=111
	if path=="m/49'/0'/0'/0/0" and network==111:
		path = "m/49'/1'/0'/0/0"
	pvkey = seed2pvkey(seed, path)
	return pvkeytoWIF(pvkey, network)
