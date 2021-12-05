import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

# Creates the Block data class


@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    prev_hash: str = 0
    nonce: str = 0

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(data)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):
        calculated_hash = block.hash_block()
        num_of_zeros = '0' * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])


pychain = setup()

st.markdown("# PyChain")
st.markdown("## Store Data in the Chain")

input_data = st.text_input("Block Data")

slider_difficulty = st.slider("Blockchain Difficulty", 1, 5)
pychain.difficulty = slider_difficulty


if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    new_block = Block(data=input_data, creator_id=42,
                      prev_hash=prev_block_hash)

    pychain.add_block(new_block)

    st.write("Winning Hash", new_block.hash_block())

st.markdown("## PyChain Ledger")
pychain_df = pd.DataFrame(pychain.chain)

st.write(pychain_df)
