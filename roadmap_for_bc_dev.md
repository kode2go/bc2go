BC1

Different types of BC developers

DAPP - Decentralized Application

3 parts to DAPP:

1. SC - Runs on BC
- decide how money flows
- accpet money
- who get money
- who mus get paid
- for example if you ahve a NFT marketplace your SC
will receive transactions from buyer and send NFT to buyer.

CFD

SC - with ethereum - needs solidity, use remix IDE to 
develop SC. See examples of SC on solidity IDE (See basic
tutorial on how to run SC on Remix)

What is SC developer:
1. easy to get started, difficult to master
- programming language
- security

3 Types of SC Dev:
A. What does a SC "CORE" developer need using Ethereuem BC to develop SC:
1. Remix 
2. Truffle - IDE on PC
3. Ganache - local EVM blockchain
4. MetaMask
5. Complete environment - Moralis - https://moralis.io/
~ 5/10% of code

B. Frontend Dev / SC App Developer - Fetch users/tokens/ NFTS - JavaScript/Python
~ majority of code
~ easiest way to get started as SC exists, you just 
develop FE to test, show others, and develop interfaces.
~ start with SC App Development:
- one path:
Moralis + JS 
- easy to fetch and update data from BChain
- Can watch and monitor SC events
-- usage: supply chain mgt
-- show ideas quickly

Example with JS: NFT game - 
1. setup SC with leaderboard
2. FE - login to App and fetch highscore to show on leaderboard.

C. Backend Dev - NodeJS/Django


Note there are about 9k cryptocurrencies but use dont all use their own BC

Check
EtherScan - verify transactions
Infura - builds ethereum clients
CoinDesk
Dapp Radar

Key Terms:
POW - Proof of work
POS - Proof of stake
Note data structure of Ethereuem BC
Public (username) and Private Key (pwd)
Addresses
Wallets (Accounts)
Transactions

Note BC are slower than standard databases

~~~~~~~~~

Note BC tech is built on top of web tech stack

First understand FE - HTML, CSS, JS, FW ~ React/Django 

BE (server side) - NodeJS (npm)/Django

~~~~~~~ SC / Tools ~~~~~~~~

Most important part of DAPP is the SC
SC - small programs that live/work with BC
Note you can only append to BC, immutable cant update like traditional databases
Note - any change to SC costs GAS
Note you can have bugs in SC which can open you up to hackers
Solidity language used to develop SC for EVM, solidity is like BE lang for BC
Truffle - Solidity Local IDE
- Good to test in local environment
- Then run local ethereum network using truffle app called ganache,  not live like mainnet.
Remix - Web IDE for SC
API, Allows you to connect to eth using web3 libraries:
https://infura.io/

Note if you deployed SC on BC only way to interact with it is via CMD line, so build FE 
to make it easier.

So: SC + FE (web/mobile) = DAPP

Steps:
1. Integ FE with BC, use web3 for JS library or Python
2. Integ with wallet like MetaMask - note no pwds in DAPP only Private and public keys

Note: BC like a Database



~~~~~~~ Side Notes ~~~~~~~~~~

Issues with Ethereum:
- costs and fees - gas fees (each write will cost you)
- slow transaction rate
-- both this should be fixed by ether 2.0, but competetors are doing this already by having less "nodes" which is a tradoff to security...as ether has a huge network of notes so is more secure
but takes longer.
- centralized decentralization - force you to know personal info
- solidity language always changing - code reusable difficult - easier to use remix IDE, goes
the same for truffle. Old code from truffle 4.0 wont work on truffle 5.0.

~~~~~~~~ Moralis ~~~~~~~~~~
MetaMask2022
Build Serverless web3 apps without having to worry about backend infrastructure.

Simple Setup:
https://docs.moralis.io/guides/build-a-simple-dapp-in-3-minutes

~~~~~~~ Dapp University ~~~~~~~~~~~~
https://www.youtube.com/watch?v=SAi5rYFh7yw&list=PLS5SEs8ZftgVn38FOhXvLc0PoX_0hnJO9
Web3.py Dapp University

Check etherscan and get code of smart contract and interact with it:
https://www.youtube.com/watch?v=prInJEq6JeI&list=PLS5SEs8ZftgVn38FOhXvLc0PoX_0hnJO9&index=2

Personal BlockChain EVM - ganache:
https://www.youtube.com/watch?v=jA0sL3PM2DE&list=PLS5SEs8ZftgVn38FOhXvLc0PoX_0hnJO9&index=3

Local SC:
https://www.youtube.com/watch?v=p5W67zTQFRM&list=PLS5SEs8ZftgVn38FOhXvLc0PoX_0hnJO9&index=4
https://www.youtube.com/watch?v=UGcInULTCwU&list=PLS5SEs8ZftgVn38FOhXvLc0PoX_0hnJO9&index=5

~~~~~~~~~~Django - Proj~~~~~~~~
https://medium.com/coinmonks/how-i-integrated-django-with-blockchain-and-built-a-decentralized-application-dapp-f104ae551e12

~~~~~~~~~ Ethereum Ecosystem ~~~~~~~

https://www.youtube.com/watch?v=uGPC9wNTBbw

Solidity / JS
Truffle (uses web3) / Hardhat (uses ethers JS)
Remix
Web3.JS / Ethers JS / Python Web3
MetaMask
- Most browsers dont support connect to BC thats why you need MetaMask
- Converts normal browser to blockchain browser
Ganache
React JS (Website - web framework)
Node JS

~~~~~~~~~process ~~~~~~~~~
By crypto on coinbase exchange and withdraw it metamask wallet

~~~~~~~ crypto exchange ~~~~~
 build something like uniswap
 
~~~~~~ HOW TO LEARN ~~~~~~~~

Emmersion Learing:
1. Do a tutorial where they hold your hand
2. Then try and something new or unique
3. Then most important part is - learning the skill to solve problems,
ask the right questions to get the solution, you will need to know how
to use google well, and community forums. You will need to get stuck, figure it out - that is when you truly start learning! 
4. Then when things work, then you get motivated to do more and you learn quicker than just starting to learn A-Z of a language and then only after
do projects. Rather, do the projects and learn as you go along what you need
to know.
5. Expect failure to happen its part of learning

https://www.youtube.com/watch?v=uGPC9wNTBbw&t=2874s

~~~~~~~BC~~~~~~~~~

https://medium.com/coinmonks/ethereum-blockchain-hello-world-smart-contract-with-java-9b6ae2961ad1

Types of Blockchains: Mainly there are two types of blockchain implementations. Open/Public and enterprise. In an open and public blockchain such as BitCoin or Ethereum anyone can join as a node to the main network. But in an enterprise blockchain such as Hyperledger fabric only authorized nodes can enter into the network.

Ethereum is written using Go programming language. Geth is the command line tool/interface for running a full ethereum node. You have the option of connecting to main ethereum network or create your own private network. If you are connected to main network then entire block chain data (~45GB) will be downloaded to your machine. Therefore we are going to setup our own network with one node.

Smart Contract in ethereum is a piece of code that can be deployed and executed to perform business functions. The compiled code is run on every node using ethereum JVM. Contract has its own account address. The caller should pay ether to deploy and execute smart contracts in nodes. A token (Currency) is also a smart contract. These contracts are written using Solidity language. You can define your own currency as a smart contract.

Account in ethereum is a combination of account address, a public key and a private key. Address is used to when performing transactions such as fund transfer. Account address is derived from public key. Private key is used to sign the transactions.

Wallet is used to create/manage your accounts. Wallet can have multiple accounts.

MetaMask is a wallet manager app which can be downloaded as a Chrome extension. You will have to trust them to keep your private key.

Remix is an online IDE for solidity language. Remix runs it own ethereum node for testing purposes.

web3js is a java script framework which can be used to interact with the ethereum node

web3j is a java API which can be used to interact with the node

Mist is a browser to browse dApps hosted in cloud. It can be used as a wallet manage as well.

Geth is the command line tool which is used to interact with the blockchain

Transaction is the fundamental message structure in blockchain.

~~~~~~~ DAPP ~~~~~~~~~~~~~~~~~

pancakeswap (website)/quickswap <-> Javascript/Python <-> web3.0 JS/python <-> smart contract <-> blockchain (eth)

DAPP - decentralized application

~~~~~~~~ Tutorials to try ~~~~~~
https://cryptosoc.github.io/tutorials/make-a-dapp/

https://blog.logrocket.com/building-dapp-ethers-js/
https://dev.to/wasimcodex/building-a-frontend-react-app-for-dapp-part-34-5cah
