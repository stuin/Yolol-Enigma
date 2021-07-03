# Enigma Machine simulator in yolol
Attempt at simulating an enigma machine with a number of yolol chips

### Using Machine:
- Number goes in and out through `:key`
- `:log` keeps track of output numbers for easier debugging
- `:reset=0` will restart machine with default settings, allowing for decryption or a new message
- wait till reset is -1 before moving on
- Resetting and inputing the numbers from the log should result in the original inputs
- generator.py can be used to create new randomized wheel and reflector files

### Implementation:
- `reset` should be used as `chipwait` for the reset chip
- `i`, `c`, `log`, `key` should be placed in a storage chip
- `ind` controls the order for each wheel, starting at 1 and ending at the reflector
- each chip should have its own random starting values for `o`, `max`, `num` and `add`