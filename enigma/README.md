# Enigma Machine simulator in yolol
Attempt at simulating an enigma machine with a number of yolol chips.

### Using Machine:
1. Write message in `:msg` and set `:enigma` to 0
2. `:log` will show the output message
3. `:enigma` will reset to -1 to pause the machine when finished
4. `:reset=0` will restart machine with default settings
5. Wait till reset is -1 before moving on
6. Inputing the message from the log after a reset should restore the original message

### Formatting:
- By default the enigma machine supports 35 characters, ` #$+,-./_` and all the lowercase letters
- Setting `:format=1` will create issues during encryption, but will allow for other letters to be displayed in the log when decrypting the original
	1. Placing `$` before a letter will make the letter uppercase
	2. `$ ` will become tab
	3. `$,` will become enter

### Implementation:
- `:reset` should be used as `chipwait` for the reset chip
- The formatting chip should not use any `chipwait`
- All other chips should use `:enigma` as `chipwait`
- `:i`, `:c`, `:out`, `:msg`, `:log`, and `:format` should be placed in a storage chip or other device
- `ind` controls the order for each wheel, starting at 1 and ending at the reflector
- Each chip should have its own random starting values for `o`, `max`, `num` and `add`
- generator.py can be used to create new randomized wheel and reflector files
