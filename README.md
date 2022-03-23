# ChaCha20-py
Python implementation of ChaCha20

This imeplentation uses:
- 2 * 32 bits nounce sub-blocks and 2*32 bits coutner sub-blocks in the ASCII space. These values are randomised on each run.
- 256bit randomised Key

Todo:
- [x] Generate values for Nounce and Key
- [x] Implent functions for ARX cycle
- [x] Quarter Round Funciton
- [x] Generate Key Stream
- [ ] Option to add text stream to be XORed with key stream
- [ ] Make program more modular

