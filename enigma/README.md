# Enigma Machine simulator in yolol

### Using Machine:
- Number goes in with :key and answer ends up in :out
- :log keeps track of all answers for easier debugging
- Refreshing and inputing the numbers from the log should result in the original inputs

### Implementation:
- Live reset sytem not yet implemented
- pw0-pw3 should be replaced with chipwait but that is untested
- generator.py can be used to create new randomized wheel and reflector files
- pw variables should go from 0 to the last chip and back again
- each chip has its own random values for o, reset, num, and add