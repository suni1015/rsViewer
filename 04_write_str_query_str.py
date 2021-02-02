"""
Basic string write_str / query_str
"""
from RsInstrument.RsInstrument import RsInstrument

instr = RsInstrument('TCPIP::100.100.100.100::INSTR', True, True)
instr.write_str('*RST')
response = instr.query_str('*IDN?')
print(response)

# Close the session
instr.close()
