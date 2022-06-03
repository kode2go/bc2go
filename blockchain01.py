# import libraries
# https://www.youtube.com/watch?v=pYasYyjByKI
import hashlib

class NeuralCoinBlock:
	def __init__(self, previous_block_hash, transaction_list):
		self.previous_block_hash = previous_block_hash
		self.transaction_list = transaction_list

		self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2.1 NC to Mike"
t2 = "Anna1 sends 2.1 NC to Mike1"
t3 = "Anna2 sends 0.2 NC to Mike2"
t4 = "Anna1 sends 12 NC to Mike3"
t5 = "Anna4 sends 2.1 NC to Mike"
t6 = "Anna sends 2.1 NC to Mike2"

initial_block = NeuralCoinBlock("initial string", [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)