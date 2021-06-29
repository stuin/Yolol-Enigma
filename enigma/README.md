# Enigma Machine simulator in yolol
Attempt at simulating an enigma machine with a number of yolol chips

### Using Machine:
- Number goes in with `:key` and answer ends up in `:out`
- `:log` keeps track of all answers for easier debugging
- `:reset=0` will restart machine with default settings, allowing for decryption or a new message
- Refreshing and inputing the numbers from the log should result in the original inputs

### Implementation:
- `:pw` variables and `:reset` should be replaced with `chipwait` in game but that is untested
- generator.py can be used to create new randomized wheel and reflector files
- `:pw` variables should go from 0 to the last chip and back again
- each chip should have its own random starting values for `o`, `max`, `num` and `add`