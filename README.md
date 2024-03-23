# HackTheBox Challenge - Secure Signing Writeup (Easy)

## About this challenge
I started with some code review and found that signing logic is vulnerable with improper length validation. This allow the incremental brute force attacks to guess flag (xor secret key) with only few attemps. 

## Installation

```sh
pip install pwntools
git clone https://github.com/mh0mm/HTB-Challenge-Secure-Signing-Writeup.git
cd HTB-Challenge-Secure-Signing-Writeup
chmod +x htb_secure_signing_writeup.py
```

## Running

Modify IP address and some obfuscation codes to run it with

```sh
nano htb_secure_signing_writeup.py 
python3 htb_secure_signing_writeup.py
```

Official HTB Secure Signing Challenge Discussion : 

https://forum.hackthebox.com/t/official-secure-signing-discussion/289591

